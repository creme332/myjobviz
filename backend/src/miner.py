from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
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

        self.scraped_urls: list[str] = scraped_urls

        self.limit: int = limit

        # default url for IT jobs sorted by most recent
        self.default_url: str = ('https://www.myjob.mu/ShowResults.aspx?'
                                 'Keywords=&Location='
                                 '&Category=39&Recruiter=Company&'
                                 'SortBy=MostRecent&Page=')

        # duration of loading page animation
        self.load_duration: int = 5  # ! Avoid decreasing this value

        # setup scraper
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver: webdriver.Chrome = webdriver.Chrome(
            options=chrome_options)

        # store new jobs found
        self.new_jobs: list[Job] = []

    def get_jobs_on_page(self, pageNumber: int) -> int:
        """
        Extracts all job data on a page and saves this
        data to `new_jobs`.

        Args:
            pageNumber(int): Page number

        Returns:
            int: number of new jobs scraped on current page
        """

        # go to page
        self.driver.get(self.default_url+str(pageNumber))
        self.wait()

        # get all job modules on current page
        job_modules = self.driver.find_elements(
            By.CSS_SELECTOR, ("div.module.job-result"))

        # initialise counter for the number of new
        # jobs found on current page
        jobs_added_count = 0

        for job_module in tqdm(job_modules):
            jobObj = Job()

            # get url of current job module
            jobObj.url = job_module.find_element(
                By.CSS_SELECTOR, 'a.show-more').get_attribute('href')

            # ignore already scraped jobs
            if jobObj.url in self.scraped_urls:
                continue

            # else new job found
            jobs_added_count += 1
            self.scraped_urls.append(jobObj.url)

            # extract job title
            jobObj.job_title = job_module.find_element(
                By.CSS_SELECTOR,
                'div.job-result-title h2').text.strip()

            # extract company name
            # * Some job posts have `Hidden Company` as their company name
            # * and in this case, the required element is missing.
            try:
                element = job_module.find_element(
                    By.CSS_SELECTOR,
                    'a[itemprop="hiringOrganization"]')
            except NoSuchElementException:
                print(f'\nCould not find hiring organization '
                      f'for {jobObj.url} on page {pageNumber}')
                jobObj.company = "Unknown"
            else:
                jobObj.company = element.text.strip()

            # extract date posted and closing date
            date_posted = job_module.find_element(
                By.CSS_SELECTOR,
                'li.updated-time').text.replace('Added ', '')

            closing_date = job_module.find_element(
                By.CSS_SELECTOR,
                'li.closed-time').text.replace('Closing ', '')

            # convert string dates to correct datetime data type
            jobObj.date_posted = datetime.strptime(
                date_posted, '%d/%m/%Y')
            jobObj.closing_date = datetime.strptime(
                closing_date, '%d/%m/%Y')

            # extract job location
            element = job_module.find_element(
                By.CSS_SELECTOR,
                'li[itemprop=\'jobLocation\']')
            jobObj.location = element.text.strip()

            # extract salary
            element = job_module.find_element(
                By.CSS_SELECTOR, 'li[itemprop=\'baseSalary\']')
            jobObj.salary = element.text.strip()

            # save job to list of scraped jobs
            self.new_jobs.append(jobObj)

            if (len(self.new_jobs) == self.limit):
                return jobs_added_count

        return jobs_added_count

    def wait(self) -> None:
        """
        Wait for page to stop loading.
        """
        time.sleep(self.load_duration)

    def get_page_count(self) -> int:
        """
        Returns the number of pages containing IT jobs.

        Each page contains around 40 jobs.

        Returns:
            int: number of pages containing IT jobs
        """
        self.driver.get(self.default_url+'1')  # go to first page of results
        self.wait()

        # get page buttons found at bottom of page
        pageButtons = self.driver.find_elements(
            By.CSS_SELECTOR, '#pagination li')
        # the last page button is the navigation button.
        # the before-last page button contains the number of pages
        last_page = int(pageButtons[-2].text)
        return last_page

    def scrape(self) -> list[dict]:
        """
        Start scraping from first page.


        Raises:
            Exception: Unable to find number of pages

        Returns:
            list[dict]: New jobs found.
        """
        last_page = self.get_page_count()
        if (last_page is None):
            raise Exception("Unable to obtain number of pages")

        # scrape each page
        for pageNumber in tqdm(range(1, last_page+1)):
            # extract job data
            jobs_added_count = self.get_jobs_on_page(pageNumber)

            # since jobs are sorted by recent, as soon as
            # we encounter a page which has already been visited we can stop
            # scraping. (all pages after current page are also already visited)
            if (jobs_added_count == 0 or jobs_added_count == self.limit):
                break

        # fetch extra information about each job
        # TODO: Fetch this information asynchronously
        # ! This information cannot be fetched directly inside the loop from
        # ! get_jobs_on_page function. Navigating between pages causes stale
        # ! element reference.
        # ! https://stackoverflow.com/q/45002008/17627866
        for jobObj in tqdm(self.new_jobs):
            # go to specific job module page
            self.driver.get(jobObj.url)
            self.wait()  # wait for page to load

            # Extract job description from Show More option
            element = self.driver.find_element(By.CSS_SELECTOR,
                                               'div.job-details')
            jobObj.job_details = element.text.strip()

            # extract employment type
            element = self.driver.find_element(
                By.CSS_SELECTOR, 'li.employment-type')
            jobObj.employment_type = element.text.strip()

        self.driver.quit()

        return [x.__dict__ for x in self.new_jobs]


if __name__ == "__main__":
    x = JobScraper([], 1)
    jobs = x.scrape()
    print(len(jobs))
    print(jobs[0])
