# -*- coding: utf-8 -*-
"""
Created on Fri May 2022
BeautifulSoup version : 4.10.0
Python Version : 3.9.7
Summary : Job data from website is scraped and then saved to a .csv file.
@author: me
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from csv import writer


# default url for IT jobs
default_page_url = 'https://www.myjob.mu/ShowResults.aspx?Keywords=&Location=&Category=39&Recruiter=Company&Page=' 

#keywords = ["developer", "développeur", "engineer", "ingénieur"] # keywords for job title

# =============================================================================
# header = ['job_title','show_more_page_text', 'date_posted','URL', # header of csv file 
#           'location',
#           'job_details', 'employment_type','company','salary'
#           ]
# =============================================================================
header = ['job_title', 'date_posted', 'closing date', 'URL', # header of csv file 
           'location', 'employment_type','company','salary','job_details'
           ]

def SaveDataToFile():

    developer_jobs_count = 0
    last_page = 1
    
    with open('data.csv','w', encoding = 'utf-8-sig', newline='' ) as f:
        thewriter = writer (f)
        thewriter.writerow(header)
        
        for page_number in range(1,last_page + 1):
            current_url = default_page_url + str(page_number)
            html_text = requests.get(current_url).text
            soup =  BeautifulSoup(html_text,'lxml')
            job_modules = soup.find_all('div',class_='module job-result') # find all job modules on current page
            
            i = 0
            for job_module in job_modules :
                i+=1
                if i>2 :
                    break
                job_title = job_module.find('h2',itemprop='title').text.lower()
                
                developer_jobs_count+=1
                
                #extract company name
                company_name = "None"
                if(job_module.find('a',itemprop='hiringOrganization') != None):
                    company_name = job_module.find('a',itemprop='hiringOrganization').text
                    
                # extract date posted and closing date
                date_posted = job_module.find('li',itemprop='datePosted').text.replace('Added ','')
                closing_date = job_module.find('li',class_='closed-time').text.replace('Closing ','')

                #print(date_posted)
                 
                #extract location
                location = job_module.find('li',itemprop='jobLocation').text
                
                #extract salary
                salary = job_module.find('li',itemprop='baseSalary').text
                
                # Extract all job details from Show More option
                show_more_url = "http://myjob.mu" + job_module.find('a', href = True, class_='show-more')['href']
                show_more_page_text = requests.get(show_more_url).text
                show_more =  BeautifulSoup(show_more_page_text,'lxml')
                job_detail_text = show_more.find('div', class_='job-details').text
                
                #extract employment type
                employment_type = "None"
                if(show_more.find('li', class_='employment-type') != None):
                    employment_type = show_more.find('li', class_='employment-type').text
                #print(employment_type)
                #save to file
# =============================================================================
# ['job_title', 'show_more_page_text', 'date_posted','URL', 
# 'location', 'job_details', 'employment_type','company','salary']
# =============================================================================
                info = [job_title, 
                            date_posted, closing_date, show_more_url,location,
                             employment_type,
                            company_name, salary,job_detail_text ]
                thewriter.writerow(info)

                    
    print(developer_jobs_count)


#SaveDataToFile()
jobs_df = pd.read_csv("data.csv")
print(jobs_df.iloc[3,8])
