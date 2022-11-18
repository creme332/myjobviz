#!venv/bin/python3
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv


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
        db = firestore.client()
        self.job_collection_ref = db.collection(u'jobs')

    def get_dataframe(self):
        """Gets the entire database from firestore and returns it as
        a Panda dataframe.
        WARNING : Use this function sparingly as it will
        heavily impact the quota usage for number of reads.
        """
        jobs = self.job_collection_ref.stream()
        jobs_dict = list(map(lambda x: x.to_dict(), jobs))
        return pd.DataFrame(jobs_dict)

    def get_dataframe_from_file(self):
        """Get a sample dataframe containing scraped data for testing purposes.

        Returns:
            dataframe: A 2D panda dataframe
        """

        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # parse dates and sort df
        df['date_posted'] = pd.to_datetime(
            df['date_posted'], format="%d/%m/%Y")
        df['closing_date'] = pd.to_datetime(
            df['closing_date'], format="%d/%m/%Y")
        df.sort_values('date_posted', ascending=False, inplace=True)

        return df

    def get_recent_urls(self, LIMIT=200):
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
        return pd.DataFrame(jobs_dict)['url'].values

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


if __name__ == "__main__":
    my_database = Database().get_dataframe_from_file()
    print(my_database.head())
    # x = my_database.get_recent_urls(2)
    # print(x)
