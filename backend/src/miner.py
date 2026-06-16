from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from tqdm import tqdm
from datetime import datetime
from classes.job import Job


_DATE_FORMATS = ['%d/%m/%Y', '%Y-%m-%d', '%d %b %Y', '%b %d, %Y', '%B %d, %Y']
_DATE_PREFIXES = ('Posted ', 'Closing ', 'Added ', 'Closes ')


def _parse_date(text: str) -> datetime | None:
    text = text.strip()
    for prefix in _DATE_PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            continue
    return None


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
        self.default_url: str = 'https://www.myjob.mu/jobs/information-technology'

        # max seconds to wait for an element or new content to appear
        self.load_duration: int = 15  # ! Avoid decreasing this value

        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')

        self.driver: webdriver.Chrome = webdriver.Chrome(options=chrome_options)

        self.new_jobs: list[Job] = []

    def _wait_for(self, css_selector: str) -> None:
        """Block until an element matching css_selector is present in the DOM."""
        WebDriverWait(self.driver, self.load_duration).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )

    def _wait_for_more_elements(self, css_selector: str, current_count: int) -> None:
        """Block until the number of elements matching css_selector exceeds current_count, or timeout."""
        try:
            WebDriverWait(self.driver, self.load_duration).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, css_selector)) > current_count
            )
        except TimeoutException:
            pass  # no new content appeared — scroll loop will detect the stall

    def _scroll_to_bottom(self) -> None:
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def collect_job_urls(self) -> list[str]:
        """
        Loads the IT jobs listing page and scrolls until no new jobs appear.

        Returns:
            list[str]: Job URLs not already in scraped_urls.
        """
        self.driver.get(self.default_url)
        self._wait_for('a[href*="/job/"]')

        job_pattern = re.compile(r'/job/\d+')
        seen: set[str] = set()

        while True:
            prev_count = len(seen)
            element_count = len(self.driver.find_elements(By.CSS_SELECTOR, 'a[href*="/job/"]'))

            for a in self.driver.find_elements(By.CSS_SELECTOR, 'a[href*="/job/"]'):
                href = a.get_attribute('href') or ''
                if job_pattern.search(href):
                    seen.add(href)

            # no new jobs loaded since last scroll — we've reached the end
            if len(seen) == prev_count:
                break

            new_urls = [u for u in seen if u not in self.scraped_urls]
            if self.limit != -1 and len(new_urls) >= self.limit:
                break

            self._scroll_to_bottom()
            self._wait_for_more_elements('a[href*="/job/"]', element_count)

        return [u for u in seen if u not in self.scraped_urls]

    def scrape_job_page(self, url: str) -> Job:
        """
        Navigate to a job detail page and extract all fields.

        Args:
            url (str): Full URL of the job posting.

        Returns:
            Job: Populated Job object.
        """
        jobObj = Job()
        jobObj.url = url

        self.driver.get(url)
        self._wait_for('h3')

        # job title
        try:
            jobObj.job_title = self.driver.find_element(
                By.CSS_SELECTOR, 'h3').text.strip()
        except NoSuchElementException:
            pass

        # company name (.text returns empty for off-screen elements in headless)
        try:
            el = self.driver.find_element(
                By.CSS_SELECTOR, 'a[href*="/companies/"] span')
            jobObj.company = self.driver.execute_script(
                'return arguments[0].textContent', el).strip()
        except NoSuchElementException:
            jobObj.company = 'Unknown'

        # employment type badge
        try:
            jobObj.employment_type = self.driver.find_element(
                By.CSS_SELECTOR, 'span.rounded-lg').text.strip()
        except NoSuchElementException:
            pass

        # metadata grid: location, salary, date posted, closing date (in order)
        meta_items = self.driver.find_elements(
            By.CSS_SELECTOR, 'ul.grid.grid-cols-2 > li')
        if len(meta_items) >= 1:
            jobObj.location = meta_items[0].text.strip()
        if len(meta_items) >= 2:
            jobObj.salary = meta_items[1].text.strip()
        if len(meta_items) >= 3:
            jobObj.date_posted = _parse_date(meta_items[2].text)
        if len(meta_items) >= 4:
            jobObj.closing_date = _parse_date(meta_items[3].text)

        # job description — container starts with a "Job Description" heading
        try:
            desc_container = self.driver.find_element(
                By.XPATH, '//h4[contains(., "Job Description")]/..')
            jobObj.job_details = desc_container.text.strip()
        except NoSuchElementException:
            try:
                jobObj.job_details = self.driver.find_element(
                    By.CSS_SELECTOR, 'div.py-5').text.strip()
            except NoSuchElementException:
                pass

        return jobObj

    def scrape(self) -> list[dict]:
        """
        Scroll the listing page to collect all job URLs, then visit each one
        to extract full details.

        Returns:
            list[dict]: New jobs found.
        """
        job_urls = self.collect_job_urls()

        if self.limit != -1:
            job_urls = job_urls[:self.limit]

        try:
            for url in tqdm(job_urls):
                jobObj = self.scrape_job_page(url)
                self.new_jobs.append(jobObj)
                self.scraped_urls.append(url)
        finally:
            self.driver.quit()

        return [x.__dict__ for x in self.new_jobs]


if __name__ == '__main__':
    import json
    job_scraper = JobScraper([], 1)
    out = job_scraper.scrape_job_page("https://www.myjob.mu/job/99534/systems-and-network-engineer")
    print(json.dumps(out.__dict__, indent=2, default=str))
