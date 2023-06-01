from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime
from classes.job import Job


class JobScraper:
    """
    Scrapes IT jobs from myjob.mu website
    """

    def __init__(self, scraped_urls: list[str], limit: int = -1) -> None:
        """
        Creates an instance of a scraper.

        Args:
            scraped_urls (list): A list of job URLs previously scraped. These
            jobs will be skipped. If an empty list is passed, all jobs found
            will be processed.

            limit (int): Maximum number of jobs that must be scraped. Default
            value of -1 means there's no limit.
        """

        self.scraped_urls = scraped_urls

        self.limit = limit

        # default url for IT jobs sorted by most recent
        self.default_url = ('https://www.myjob.mu/ShowResults.aspx?'
                            'Keywords=&Location='
                            '&Category=39&Recruiter=Company&'
                            'SortBy=MostRecent&Page=')

        # duration of loading page animation
        self.load_duration = 5  # ! Avoid decreasing this value

        # number of seconds to wait between requests
        self.crawl_delay = 5

        # setup selenium scraper
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=chrome_options)

        # store new jobs found
        self.new_jobs = []

    def get_jobs(self) -> int:
        """
        Extracts all job data on current page and saves this
        data to `new_jobs`.

        Returns:
            int: number of new jobs scraped on current page
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

            # extract job title
            jobObj.job_title = job_module.find(
                'h2', itemprop='title'). text.lower()

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
                'li', itemprop='jobLocation').text if job_module.find(
                'li', itemprop='jobLocation') else 'Unknown'

            # extract salary
            jobObj.salary = (job_module.find('li', itemprop='baseSalary').text
                             if job_module.find(
                'li', itemprop='baseSalary') else 'Unknown')

            # Extract job description from Show More option
            self.driver.get(jobObj.url)
            show_more = BeautifulSoup(self.driver.page_source, 'lxml')
            x = show_more.find(
                'div', class_='job-details')
            jobObj.job_details = x.text if x else 'Unknown'

            # extract employment type
            x = show_more.find('li', class_='employment-type')
            jobObj.employment_type = x.text if x else 'Unknown'

            # save job to list of scraped jobs
            self.new_jobs.append(jobObj.__dict__)

            if (len(self.new_jobs) == self.limit):
                return jobs_added_count

            # sleep
            time.sleep(self.crawl_delay)

        return jobs_added_count

    def scrape(self) -> list[dict]:
        """
        Start scraping


        Raises:
            Exception: Unable to find number of pages

        Returns:
            list[dict]: New jobs found.
        """

        # start a session
        self.driver.get(self.default_url+'1')
        time.sleep(self.load_duration)  # wait for loading page to be over

        # get total number of pages present
        soup = BeautifulSoup(self.driver.page_source, 'lxml')

        paginationContainer = soup.find('ul', id="pagination")
        pageButtons = paginationContainer.find_all('li')  # pyright: ignore
        # last element is the navigation button so use before last element
        last_page = int(pageButtons[-2].text)

        if (last_page is None):
            raise Exception("Unable to obtain number of pages")

        # scrape each page
        for pageNumber in tqdm(range(1, last_page+1)):
            # go to page
            self.driver.get(self.default_url+str(pageNumber))

            # extract job data
            jobs_added_count = self.get_jobs()

            # since jobs are sorted by recent, as soon as
            # we encounter a page which has already been visited we can stop
            # scraping. (all pages after current page are also already visited)
            if (jobs_added_count == 0 or jobs_added_count == self.limit):
                break

        self.driver.quit()
        return self.new_jobs


if __name__ == "__main__":
    x = JobScraper([], 1)  # scrape only 1 job
    jobs = x.scrape()
    print(len(jobs))
    print(jobs[0])
