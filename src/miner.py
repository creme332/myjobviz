#!venv/bin/python3
"""This module is responsible for scraping the latest IT jobs
from myjob.mu website.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime
from classes.job import Job


class Scraper:

    def __init__(self, scraped_urls: list) -> None:
        self.scraped_urls = scraped_urls

        # default url for IT jobs sorted by most recent
        self.default_url = ('https://www.myjob.mu/ShowResults.aspx?'
                            'Keywords=&Location='
                            '&Category=39&Recruiter=Company&'
                            'SortBy=MostRecent&Page=')

        # duration of loading page animation
        # ! DO NOT DECREASE THIS VALUE
        self.load_duration = 5

        # number of seconds to wait between requests
        self.crawl_delay = 5

        # setup selenium scraper
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

        # store new job found
        self.new_jobs = []

    def scrapeJobModules(self) -> None:
        """Extracts all job data on current page and saves this
        data to `new_jobs`.
        """

        # get all job modules on current page
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        job_modules = soup.find_all('div', class_='module job-result')

        # initialise counter for the number of new
        # jobs found on current page
        jobs_added_count = 0

        for job_module in tqdm(job_modules):
            jobObj = Job()

            # get url of current job module
            jobObj.url = "http://myjob.mu" + \
                job_module.find('a', href=True, class_='show-more')['href']

            # ignore already scraped jobs
            if jobObj.url in self.scraped_urls:
                continue

            # else new job found
            jobs_added_count += 1
            self.scraped_urls.append(jobObj.url)

            jobObj.job_title = job_module.find(
                'h2', itemprop='title').text.lower()

            # extract company name
            if (job_module.find('a', itemprop='hiringOrganization')
                    is not None):
                jobObj.company = job_module.find(
                    'a', itemprop='hiringOrganization').text

            # extract date posted and closing date
            jobObj.date_posted = job_module.find(
                'li', itemprop='datePosted').text.replace('Added ', '')
            jobObj.closing_date = job_module.find(
                'li', class_='closed-time').text.replace('Closing ', '')

            # convert string dates to correct datetime data type
            jobObj.date_posted = datetime.strptime(
                jobObj.date_posted, '%d/%m/%Y')
            jobObj.closing_date = datetime.strptime(
                jobObj.closing_date, '%d/%m/%Y')

            # extract job location
            jobObj.location = job_module.find(
                'li', itemprop='jobLocation').text

            # extract salary
            jobObj.salary = job_module.find('li', itemprop='baseSalary').text

            # Extract job description from Show More option
            self.driver.get(jobObj.url)
            show_more = BeautifulSoup(self.driver.page_source, 'lxml')
            jobObj.job_details = show_more.find(
                'div', class_='job-details').text

            # extract employment type
            if (show_more.find('li', class_='employment-type') is not None):
                jobObj.employment_type = show_more.find(
                    'li', class_='employment-type').text

            # save job in database
            self.new_jobs.append(jobObj.__dict__)
            time.sleep(self.crawl_delay)

        return jobs_added_count

    def get_new_jobs(self) -> list:
        """Returns a list of dictionaries representing the new jobs
        found.
        """
        # start a session
        self.driver.get(self.default_url+'1')
        time.sleep(self.load_duration)  # wait for loading page to be over

        # get total number of pages present
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        last_page = int(soup.find('ul', id="pagination").find_all(
            'li')[-2].text)

        # scrape pages
        for pageNumber in tqdm(range(1, last_page+1)):
            self.driver.get(self.default_url+str(pageNumber))
            jobs_added_count = self.scrapeJobModules()

            # since jobs are sorted by recent, as soon as
            # we encounter a page which has already been visited we can stop
            # scraping. (all pages after current page are also already visited)
            if (jobs_added_count == 0):
                break

        self.driver.quit()
        return self.new_jobs


if __name__ == "__main__":
    x = Scraper([])
    jobs = x.get_new_jobs()
    print(len(jobs))
    print(jobs[0])
