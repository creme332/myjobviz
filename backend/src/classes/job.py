from datetime import datetime
from firebase_admin import firestore
from typing import Optional


class Job:
    def __init__(self):
        self.job_title: str = ""
        self.url: str = ""
        self.location: str = ""
        self.employment_type: str = ""
        self.company: str = ""
        self.salary: str = ""
        self.job_details: str = ""

        # datetime format: DD/MM/YYYY
        self.date_posted: Optional[datetime] = None
        self.closing_date: Optional[datetime] = None

        # Store time when the server receives the Job.
        self.timestamp = firestore.SERVER_TIMESTAMP  # type: ignore


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
