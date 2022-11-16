#!venv/bin/python3
import library
class Job:
    def __init__(self):
        self.job_title = None  # string
        self.date_posted = None  # # string : DD/MM/YYYY
        self.closing_date = None  # # string : DD/MM/YYYY
        self.url = None  # string
        self.location = None  # string
        self.employment_type = None  # string
        self.company = None  # string
        self.salary = None  # string
        self.job_details = None  # string


if __name__ == "__main__":
    x = Job()
    x.job_title = 'software developer'  
    x.date_posted = '12/10/2022' 
    x.closing_date = '22/10/2022'  
    x.url = 'a@gmail.com'  
    x.location = 'Moka'  
    x.employment_type = 'Permanent'  
    x.company = 'company' 
    x.salary = '10000-20000' 
    x.job_details = 'details'  

    library.uploadJob(x.__dict__)
    print(x.__dict__)
