#!venv/bin/python3
"""This module is responsible for scraping the latest IT jobs
from myjob.mu website.
"""

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import library
from jobClass import Job


def scrapeJobModules(html_text, scraped_urls, session):

    # get all job modules on current page
    soup = BeautifulSoup(html_text, 'lxml')
    job_modules = soup.find_all('div', class_='module job-result')
    print(len(job_modules))
    jobs_added_count = 0

    for job_module in job_modules:
        jobObj = Job()

        # get url of job page
        jobObj.url = "http://myjob.mu" + \
            job_module.find('a', href=True, class_='show-more')['href']

        # ignore already scraped jobs
        if jobObj.url in scraped_urls:
            continue

        # else new job found
        jobs_added_count += 1

        jobObj.job_title = job_module.find(
            'h2', itemprop='title').text.lower()

        # extract company name
        if (job_module.find('a', itemprop='hiringOrganization')  # may evaluate to None
                is not None):
            jobObj.company = job_module.find(
                'a', itemprop='hiringOrganization').text

        # extract date posted and closing date
        jobObj.date_posted = job_module.find(
            'li', itemprop='datePosted').text.replace('Added ', '')
        jobObj.closing_date = job_module.find(
            'li', class_='closed-time').text.replace('Closing ', '')

        # extract job location
        jobObj.location = job_module.find(
            'li', itemprop='jobLocation').text

        # extract salary
        jobObj.salary = job_module.find('li', itemprop='baseSalary').text

        # Extract job description from Show More option
        r = session.get(jobObj.url)
        show_more = BeautifulSoup(r.html.html, 'lxml')
        jobObj.job_details = show_more.find(
            'div', class_='job-details').text

        # extract employment type
        if (show_more.find('li', class_='employment-type') is not None):
            jobObj.employment_type = show_more.find(
                'li', class_='employment-type').text

        # save job in database
        print(jobObj.__dict__)
        library.uploadJob(jobObj.__dict__)
        return

    return jobs_added_count


def scrapeWebsite():
    # get already scraped urls from library
    scraped_urls = library.getAsDataframe()['url'].values
    
    # default url for IT jobs sorted by most recent
    default_page_url = ('https://www.myjob.mu/ShowResults.aspx?'
                        'Keywords=&Location=&Category=39&Recruiter=Company&'
                        'SortBy=MostRecent&Page=')
    # start a session
    session = HTMLSession()
    r = session.get(default_page_url+'1')

    # sleep for some time to wait for loading page to disappear
    r.html.render(sleep=7)

    # get number of pages that must be scraped
    soup = BeautifulSoup(r.html.html, 'lxml')
    last_page = int(soup.find('ul', id="pagination").find_all(
        'li')[-2].text)

    total_jobs = 0
    # scrape pages
    for pageNumber in range(1, last_page+1):
        r = session.get(default_page_url+str(pageNumber))
        r.html.render(sleep=2)
        jobs_added_count = scrapeJobModules(r.html.html, scraped_urls, session)
        break
        if (jobs_added_count == 0):
            break
        total_jobs += jobs_added_count

    print("New jobs added = ", total_jobs)

scrapeWebsite()