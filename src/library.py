"""This module is responsible for managing the Firestore database which
contains all scraped jobs' data.
"""
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
import pandas as pd

cred = credentials.Certificate('src/serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
job_collection = db.collection(u'jobs')


def uploadJob(jobDictionary):
    """Takes as argument a single python dictionary and uploads
    it to my Firestore database.

    Args:
        jobDictionary (dictionary): A dictionary with the following keys : `job_title`,
        `date_posted`, `closing_date`, `url`, `location`,
        `employment_type`, `company`, `salary`, `job_details`
    """
    update_time, city_ref = job_collection.add(jobDictionary)
    print(f'Added document with id {city_ref.id} at: {update_time}')


def getAsDataframe():
    """Returns my Firestore database as a panda dataframe

    Returns:
        dataframe: A 2D panda dataframe
    """
    jobs = job_collection.stream()
    jobs_dict = list(map(lambda x: x.to_dict(), jobs))
    df = pd.DataFrame(jobs_dict)
    df['date_posted'] = pd.to_datetime(df['date_posted'], dayfirst=True)
    df.sort_values('date_posted', ascending=False, inplace=True)
    return df
