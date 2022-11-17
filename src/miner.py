#!venv/bin/python3
"""This module is responsible for scraping the latest IT jobs
from myjob.mu website.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import library
from jobClass import Job
from tqdm import tqdm

# setup scraper
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)


def scrapeJobModules(html_text, scraped_urls):
    """Extracts all job data on a page and save this data to library.

    Args:
        html_text (html): html of page
        scraped_urls (array): list of urls already scraped

    Returns:
        jobs_added_count: number of new jobs found on webpage
    """

    # get all job modules on current page
    soup = BeautifulSoup(html_text, 'lxml')
    job_modules = soup.find_all('div', class_='module job-result')
    # print(len(job_modules))
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
        if (job_module.find('a', itemprop='hiringOrganization')
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
        driver.get(jobObj.url)
        # time.sleep(1)
        show_more = BeautifulSoup(driver.page_source, 'lxml')
        jobObj.job_details = show_more.find(
            'div', class_='job-details').text

        # extract employment type
        if (show_more.find('li', class_='employment-type') is not None):
            jobObj.employment_type = show_more.find(
                'li', class_='employment-type').text

        # save job in database
        # print(jobObj.job_title)
        library.uploadJob(jobObj.__dict__)
        # return

    return jobs_added_count


def scrapeWebsite():
    """Sets up Selenium scraper and scrapes all pages containing IT jobs on website by 
    calling `scrapeJobModules()`. 
    """
    # get already scraped urls from library
    scraped_urls = library.getAsDataframe()['url'].values

    # default url for IT jobs sorted by most recent
    default_page_url = ('https://www.myjob.mu/ShowResults.aspx?'
                        'Keywords=&Location=&Category=39&Recruiter=Company&'
                        'SortBy=MostRecent&Page=')
    # start a session
    driver.get(default_page_url+'1')
    time.sleep(5)  # any number > 3 should work fine

    # get number of pages that must be scraped
    soup = BeautifulSoup(driver.page_source, 'lxml')
    last_page = int(soup.find('ul', id="pagination").find_all(
        'li')[-2].text)

    total_jobs = 0
    # scrape pages
    for pageNumber in tqdm(range(1, last_page+1)):
        driver.get(default_page_url+str(pageNumber))
        jobs_added_count = scrapeJobModules(driver.page_source, scraped_urls)
        total_jobs += jobs_added_count

        # since jobs are sorted by date on website, as soon as
        # we encounter a page which we have already visited we can stop
        # scraping. (all pages after current page are also already visited)
        if (jobs_added_count == 0):
            break

    print("New jobs added = ", total_jobs)
    driver.quit()


if __name__ == "__main__":
    scrapeWebsite()
