#!venv/bin/python3
from datetime import datetime
from firebase_admin import firestore


class Job:
    def __init__(self):
        self.job_title = None  # string
        self.date_posted = None  # datetime format: DD/MM/YYYY
        self.closing_date = None  # datetime format: DD/MM/YYYY
        self.url = None  # string
        self.location = None  # string
        self.employment_type = None  # string
        self.company = None  # string
        self.salary = None  # string
        self.job_details = None  # string

        # track when the server receives the Job.
        self.timestamp = firestore.SERVER_TIMESTAMP


if __name__ == "__main__":
    x = Job()
    x.job_title = 'software developer'
    x.date_posted = datetime.strptime('5/10/2022', '%d/%m/%Y')
    x.closing_date = datetime.strptime('12/10/2022', '%d/%m/%Y')
    x.url = 'a@gmail.com'
    x.location = 'Moka'
    x.employment_type = 'Permanent'
    x.company = 'company'
    x.salary = '10000-20000'
    x.job_details = 'details'

    print(x.__dict__)
