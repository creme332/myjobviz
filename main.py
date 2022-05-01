# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.myjob.mu/ShowResults.aspx?Category=39&dup=on&SortBy=Relevance&rbloc=99&lr=4').text
soup =  BeautifulSoup(html_text,'lxml')

job= soup.find('div',class_='module job-result')
#job= soup.find('div',class_='job-result-title')

job_title = job.find('h2',itemprop='title').text
company_name = job.find('a',itemprop='hiringOrganization').text
show_more_link = job.find('a',class_='show-more').text

print(job_title)
print(company_name)
print(show_more_link)
