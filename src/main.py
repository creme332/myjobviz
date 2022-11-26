#!venv/bin/python3
from classes.database import Database
from miner import Scraper
from anal import analyseAndUpdate
from visualiser import createVisualisations
import pandas as pd


def debug():

    # initialise database and scraper.
    my_database = Database()
    # return

    # fetch new jobs from website
    # new_jobs = my_scraper.get_new_jobs()
    new_jobs = pd.read_csv('data/RawScrapedData.csv').to_dict('records')

    if (len(new_jobs) == 0):
        return

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    analyseAndUpdate(my_database, job_details_list, location_list, salary_list)
    return

    createVisualisations(my_database)

    # save all new jobs to database
    for job in new_jobs:
        my_database.add_job(job)


def rebaseStatsCollection():
    """Call this function when an error occurred the last time `main()` was
    called. This function will ensure that all stored statistics are valid.
    """
    # initialise database.
    my_database = Database()
    my_database.initialise_stats_collection()

    my_database.recalculate_size_counter()

    # fetch all jobs from website
    new_jobs = my_database.get_dataframe().to_dict('records')

    if (len(new_jobs) == 0):
        return

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    # extract statistics from newly scraped data and update
    # statistics collection
    analyseAndUpdate(my_database, job_details_list, location_list, salary_list)


def main():

    # initialise database and scraper.
    my_database = Database()
    recent_urls = my_database.get_recent_urls()
    # print(recent_urls)
    my_scraper = Scraper(recent_urls)

    # fetch new jobs from website
    new_jobs = my_scraper.get_new_jobs()

    if (len(new_jobs) == 0):
        return
    print(len(new_jobs), ' new jobs found!')

    # save new jobs to database
    for job in new_jobs:
        my_database.add_job(job)

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    # extract statistics from newly scraped data and update
    # statistics collection
    analyseAndUpdate(my_database, job_details_list, location_list, salary_list)

    # update data visualisations
    createVisualisations(my_database)


if __name__ == "__main__":
    my_database = Database()
    # my_database.check_duplicates()
    # my_database.initialise_stats_collection()
    # main()
    # rebaseStatsCollection()
    createVisualisations(my_database)
    # debug()
