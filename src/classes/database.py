#!venv/bin/python3
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from analyser.dictionaryUtils import merge_dicts


class Database:
    """This class is responsible for managing the Firestore database which
    contains all scraped jobs' data.
    """

    def __init__(self):
        """Initialises firestore client
        """
        def getServiceAccountKey():
            load_dotenv(find_dotenv())
            variables_keys = {
                "type": os.getenv("TYPE"),
                "project_id": os.getenv("PROJECT_ID"),
                "private_key_id": os.getenv("PRIVATE_KEY_ID"),
                "private_key": os.getenv("PRIVATE_KEY"),
                "client_email": os.getenv("CLIENT_EMAIL"),
                "client_id": os.getenv("CLIENT_ID"),
                "auth_uri": os.getenv("AUTH_URI"),
                "token_uri": os.getenv("TOKEN_URI"),
                "auth_provider_x509_cert_url": os.getenv(
                    "AUTH_PROVIDER_X509_CERT_URL"),
                "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL")
            }
            return variables_keys

        cred = credentials.Certificate(getServiceAccountKey())
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.job_collection_ref = self.db.collection(u'jobs')
        self.stats_collection_ref = self.db.collection(u'statistics')

        # initialise references to documents in stats_collection
        self.db_size_ref = self.stats_collection_ref.document(
            u'database_size')
        self.cloud_data_ref = self.stats_collection_ref.document(u'cloud_data')
        self.db_data_ref = self.stats_collection_ref.document(u'db_data')
        self.lang_data_ref = self.stats_collection_ref.document(u'lang_data')
        self.lib_data_ref = self.stats_collection_ref.document(u'lib_data')
        self.loc_data_ref = self.stats_collection_ref.document(u'loc_data')
        self.os_data_ref = self.stats_collection_ref.document(u'os_data')
        self.salary_data_ref = self.stats_collection_ref.document(
            u'salary_data')
        self.tools_data_ref = self.stats_collection_ref.document(u'tools_data')
        self.web_data_ref = self.stats_collection_ref.document(u'web_data')

    def get_dataframe(self):
        """Gets the entire database from firestore and returns it as
        a Panda dataframe.
        WARNING : Use this function sparingly as it will
        heavily impact the quota usage for number of reads.
        """
        jobs = self.job_collection_ref.stream()
        jobs_dict = list(map(lambda x: x.to_dict(), jobs))
        return pd.DataFrame(jobs_dict)

    def get_sample_dataframe(self):
        """Get a sample dataframe containing scraped data for testing purposes.

        Returns:
            dataframe: A 2D panda dataframe
        """

        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # parse dates and sort df
        df['date_posted'] = pd.to_datetime(
            df['date_posted'], format="%d/%m/%Y")
        df['closing_date'] = pd.to_datetime(
            df['closing_date'], format="%d/%m/%Y")
        df.sort_values('date_posted', ascending=False, inplace=True)

        return df

    def get_recent_urls(self, LIMIT=200) -> list:
        """Returns a list of the urls of recently scraped jobs. This function
        can be used to preventing adding duplicates when scraping.

        - Keep 5 <`LIMIT` < 1000 to avoid exceeding read quotas.

        Args:
            LIMIT (int, optional): Maximum number of urls to be
            returned. Defaults to 200.

        Returns:
            list[str]: A list urls
        """
        # get the most recent scraped jobs
        jobs = (self.job_collection_ref
                .order_by("date_posted", direction=firestore.Query.DESCENDING)
                .limit(LIMIT)
                .stream())
        # return only the urls
        jobs_dict = list(map(lambda x: x.to_dict(), jobs))
        return pd.DataFrame(jobs_dict)['url'].values.tolist()

    def add_job(self, jobDictionary):
        """Takes as argument a single python dictionary and uploads
        it to my Firestore database.

        Args:
            jobDictionary (dictionary): A dictionary with the following keys :
            `job_title`, `date_posted`, `closing_date`, `url`, `location`,
            `employment_type`, `company`, `salary`, `job_details`
        """
        update_time, job_ref = self.job_collection_ref.add(jobDictionary)
        # print(f'Added document with id {job_ref.id} at: {update_time}')

        # increment database size counter
        self.increment_size_counter()

    def update_all_documents(self):
        """This function can be extended to update any fields of all documents.

        WARNING : Use this function sparingly as it will
        heavily impact the quota usage for number of reads.
        """
        return
        jobs = self.get_dataframe()
        for job in jobs:
            job_ref = self.job_collection_ref.document(job.id)
            job_doc = job_ref.get()

            # get date field values
            closingDate = job_doc.to_dict()['closing_date']
            datePosted = job_doc.to_dict()['date_posted']
            print(closingDate, datePosted)
            # update
            # job_ref.update({})

    def check_duplicates(self):
        """Uses `url` as primary key and checks for duplicate jobs in database.
        Result is printed out.

        WARNING : Use this function sparingly as it will
        heavily impact the quota usage for number of reads.
        """
        # https://stackoverflow.com/a/14657511/17627866
        df = self.get_dataframe()
        ids = df["url"]
        df = df[ids.isin(ids[ids.duplicated()])].sort_values("url")
        if (len(df) > 0):
            print(df)
        else:
            print('No duplicate jobs found.')

    def increment_size_counter(self):
        """Increments the counter which keeps tracks of the
        number of jobs in database.
        """
        new_size = int(self.db_size_ref.get().to_dict()['size']) + 1
        self.db_size_ref.update({'size': new_size})

    def recalculate_size_counter(self):
        """Initialises  the counter which keeps tracks of the
        number of jobs in database to its true value.

        WARNING : Use this function sparingly as it will
        heavily impact the quota usage for number of reads.
        """
        new_size = len(self.get_dataframe())
        self.db_size_ref.update({'size': new_size})

    def doc_exists(self, collectionRef, docName):
        """Given a valid collection, check if a document is present in it.

        Args:
            docName (_type_): _description_

        Returns:
            _type_: _description_
        """
        doc_ref = collectionRef.document(docName)
        doc = doc_ref.get()
        if doc.exists:
            return True
        else:
            return False

    def sanitizeDict(self, dict):
        """Dictionary keys containing chars other than
        letters, numbers, and underscores must be sanitized
        before uploading a dictionary to firestore.
        """
        new_dict = {}
        for key in dict.keys():
            new_dict[self.db.field_path(key)] = dict[key]
        return new_dict

    def update_filtered_statistics(self, incrementDict, document_ref):
        """Updates filtered statistics on Firestore.

        Args:
            incrementDict (dict): A dictionary where the values are boolean.
            documentName (dict): Name of document in the `statistics`
            collection containing a dictionary.
        """

        # if (not self.doc_exists(self.stats_collection_ref, documentName)):
        #     raise Exception(f"{documentName} document"
        #                     "is not found in statistics collection")

        # get dictionary currently stored on Firestore
        # ! add try catch here
        current_dict = self.sanitizeDict(document_ref.get().to_dict())

        # combine dictionaries by adding values
        resultDict = merge_dicts(
            current_dict, self.sanitizeDict(incrementDict))

        # if there's no change do nothing
        if (resultDict == current_dict):
            return

        # save changes
        document_ref.update(resultDict)

    def initialise_stats_collection(self):
        # set database size to 0
        self.db_size_ref.set({'size': 0})

        # create other documents which will store filtered data
        self.cloud_data_ref.set({})
        self.db_data_ref.set({})
        self.lang_data_ref.set({})
        self.lib_data_ref.set({})
        self.loc_data_ref.set({})
        self.os_data_ref.set({})
        self.salary_data_ref.set({})
        self.tools_data_ref.set({})
        self.web_data_ref.set({})

    def get_filtered_statistics(self, document_ref, header):
        dict = document_ref.get().to_dict()
        df = pd.DataFrame.from_dict(dict, orient='index')
        df = df.reset_index()
        df.columns = [header, 'Frequency']
        return df
