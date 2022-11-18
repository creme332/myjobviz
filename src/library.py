#!venv/bin/python3
"""This module is responsible for managing the Firestore database which
contains all scraped jobs' data.
"""
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime


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
app = firebase_admin.initialize_app(cred)
db = firestore.client()
job_collection = db.collection(u'jobs')


def uploadJob(jobDictionary):
    """Takes as argument a single python dictionary and uploads
    it to my Firestore database.

    Args:
        jobDictionary (dictionary): A dictionary with the following keys :
        `job_title`, `date_posted`, `closing_date`, `url`, `location`,
        `employment_type`, `company`, `salary`, `job_details`
    """
    update_time, job_ref = job_collection.add(jobDictionary)
    # print(f'Added document with id {job_ref.id} at: {update_time}')


def getAsDataframe():
    """Returns my Firestore database as a panda dataframe

    Returns:
        dataframe: A 2D panda dataframe
    """

    # data_source_filename = 'data/RawScrapedData.csv'  # raw data
    # df = pd.read_csv(data_source_filename, header=0)
    # print(len(df))

    jobs = job_collection.stream()
    jobs_dict = list(map(lambda x: x.to_dict(), jobs))
    df = pd.DataFrame(jobs_dict)

    if (len(df) > 0):
        # drop duplicates if any
        df.drop_duplicates(subset=None, keep='first', inplace=False)

        # parse dates and sort df
        df['date_posted'] = pd.to_datetime(
            df['date_posted'], format="%d/%m/%Y")
        df['closing_date'] = pd.to_datetime(
            df['closing_date'], format="%d/%m/%Y")
        df.sort_values('date_posted', ascending=False, inplace=True)

    return df


def changeDatatype():
    jobs = job_collection.stream()
    for job in jobs:
        job_ref = job_collection.document(job.id)
        job_doc = job_ref.get()

        # get date field values
        closingDate = job_doc.to_dict()['closing_date']
        datePosted = job_doc.to_dict()['date_posted']

        # update
        job_ref.update(
            {u'closing_date': datetime.strptime(closingDate, '%d/%m/%Y'),
             u'date_posted': datetime.strptime(datePosted, '%d/%m/%Y')
             })


# changeDatatype()

# print(getAsDataframe().head()['job_title'].values)
# data = {
#     u'name': u'Los Angeles',
#     u'state': u'CA',
#     u'country': u'USA',
#     u'date_posted': datetime.strptime('18/11/2022', '%d/%m/%Y')
# }

# # Add a new doc in collection 'cities' with ID 'LA'
# # db.collection(u'cities').add(data)
y = getAsDataframe()
print(y['date_posted'].values)

# print(db.collection(u'cities').document(u'LA'))
# x = db.collection(u'cities').document(u'LA').get().to_dict()['date_posted']
# print(x)
