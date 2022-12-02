#!venv/bin/python3
from classes.database import Database
from miner import Scraper
from anal import analyseAndUpdate
from visualiser import createVisualisations


def updateJobBadge(new_job_count):
    """Updates the job badge found in the README.

    Args:
        new_job_count (int): new job count
    """
    file_path = "README.md"
    new_badge = ('![Badge storing the total number of jobs'
                 ' scraped](https://img.shields.io'
                 '/badge/Total%20jobs%20scraped'
                 f'-{new_job_count}-brightgreen)\n')
    new_file_content = ''
    print(f'new job count = {new_job_count}')
    with open(file_path, 'r', encoding='utf-8') as f:

        # get all lines in readme
        lines = [line for line in f]

        # replace old badge with new badge
        lines[2] = new_badge

        # concatenate lines
        new_file_content = ''.join(lines)

    # update file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_file_content)


def debug():
    """Loads sample statistics to firestore for debugging.
    """

    # initialise database and scraper.
    my_database = Database()

    # reset statistics
    my_database.initialise_stats_collection()

    # fetch new jobs from website
    new_jobs = my_database.get_sample_dataframe().to_dict('records')

    if (len(new_jobs) == 0):
        return

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    analyseAndUpdate(my_database, job_details_list, location_list, salary_list)


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
    my_scraper = Scraper(my_database.get_recent_urls())

    # fetch new jobs from website
    new_jobs = my_scraper.get_new_jobs()

    # if no new jobs found return
    if (len(new_jobs) == 0):
        return

    # print some info about new jobs found
    job_title_list = [job['job_title'] for job in new_jobs]
    print(len(new_jobs), ' new jobs found!')
    print(job_title_list)

    # save new jobs to database
    for job in new_jobs:
        my_database.add_job(job)
        my_database.increment_size_counter()

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    # extract statistics from newly scraped data and update
    # statistics collection
    analyseAndUpdate(my_database, job_details_list, location_list, salary_list)

    # update data visualisations
    createVisualisations(my_database)

    # update job count in readme
    updateJobBadge(my_database.get_size())


if __name__ == "__main__":
    main()
