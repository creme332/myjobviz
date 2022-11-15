# -*- coding: utf-8 -*-
#!venv/bin/python3

"""
Created on Fri May 2022
BeautifulSoup version : 4.10.0
Python Version : 3.9.7
Panda version : 1.3.3
Summary : Job data from website is scraped and saved to a .csv file.
@author: creme332
"""

from bs4 import BeautifulSoup
import requests
from csv import writer
import pandas as pd


# default url for IT jobs sorted by most recent
default_page_url = ('https://www.myjob.mu/ShowResults.aspx?'
                    'Keywords=&Location=&Category=39&Recruiter=Company&'
                    'SortBy=MostRecent&Page=')

# header of csv file
header = ['job_title', 'date_posted',
          'closing date', 'URL',
          'location', 'employment_type',
          'company', 'salary', 'job_details'
          ]
filename = 'RawScrapedData.csv'  # initially empty

jobs_df = pd.read_csv(filename)  # create a dataframe from current csv file
#jobs_df['date_posted'] = pd.to_datetime(jobs_df['date_posted'], dayfirst=True)
#jobs_df = jobs_df.sort_values('date_posted', ascending=False, inplace=True)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


def WebScraping():
    # look for jobs not currently in csv file and append them to csv file
    jobs_added_count = 0
    last_page = 7  # upperbound for last page. invalid last page will not cause any error
    total_job_modules_seen = 0
    with open(filename, 'a', encoding='utf-8-sig', newline='') as f:
        thewriter = writer(f)

        for page_number in range(1, last_page + 1):
            current_url = default_page_url + str(page_number)
            html_text = requests.get(current_url).text
            soup = BeautifulSoup(html_text, 'lxml')

            # find all job modules on current page
            job_modules = soup.find_all('div', class_='module job-result')
            for job_module in job_modules:
                total_job_modules_seen += 1
                # =============================================================================
                #                 if(jobs_added_count > 2):
                #                     break
                # =============================================================================
                show_more_url = "http://myjob.mu" + \
                    job_module.find('a', href=True, class_='show-more')['href']

                if show_more_url not in jobs_df.values:  # new job found
                    jobs_added_count += 1

                    job_title = job_module.find(
                        'h2', itemprop='title').text.lower()

                    # extract company name
                    company_name = "None"
                    if(job_module.find('a', itemprop='hiringOrganization')  # may evaluate to None
                       is not None):
                        company_name = job_module.find(
                            'a', itemprop='hiringOrganization').text

                    # extract date posted and closing date
                    date_posted = job_module.find(
                        'li', itemprop='datePosted').text.replace('Added ', '')
                    closing_date = job_module.find(
                        'li', class_='closed-time').text.replace('Closing ', '')

                    # extract job location
                    location = job_module.find(
                        'li', itemprop='jobLocation').text

                    # extract salary
                    salary = job_module.find('li', itemprop='baseSalary').text

                    # Extract all job details from Show More option
                    show_more_page_text = requests.get(show_more_url).text
                    show_more = BeautifulSoup(show_more_page_text, 'lxml')
                    job_detail_text = show_more.find(
                        'div', class_='job-details').text

                    # extract employment type
                    employment_type = "None"
                    if(show_more.find('li', class_='employment-type') is not None):
                        employment_type = show_more.find(
                            'li', class_='employment-type').text

                    info = [job_title,
                            date_posted, closing_date, show_more_url, location,
                            employment_type,
                            company_name, salary, job_detail_text]
                    thewriter.writerow(info)  # add new job info to CSV file

    print("New jobs added = ", jobs_added_count)
    print("Seen modules = ", total_job_modules_seen)


WebScraping()
new_jobs_df = pd.read_csv(filename)  # read updated csv file
