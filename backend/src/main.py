from classes.database import Database
from miner import JobScraper
from analysis import analyseAndUpdate
from utils.service_key import get_service_account_key


def update_readme_job_badge(new_job_count):
    """Updates the job badge found in the README.

    Args:
        new_job_count (int): new job count
    """
    badge_color = 'orange'
    file_path = "README.md"
    new_badge = ('![Badge storing the total number of jobs'
                 ' scraped](https://img.shields.io'
                 '/badge/Total%20jobs%20scraped'
                 f'-{new_job_count}-{badge_color})\n')
    new_file_content = ''
    with open(file_path, 'r', encoding='utf-8') as f:

        # get all lines in readme
        lines = [line for line in f]

        # place new badge on third line
        lines[2] = new_badge

        # concatenate lines
        new_file_content = ''.join(lines)

    # update file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_file_content)


def rebase_statistics():
    """
    Recalculates and updates all statistics. frontend-db is also updated.

    This function ensures data integrity but heavily impacts read and
    write quotas.
    """
    # load main database.
    my_database = Database(get_service_account_key(True))

    # get all jobs stored in database
    new_jobs = my_database.get_dataframe().to_dict('records')

    # update size of database
    my_database.update_size_counter(len(new_jobs))

    if (len(new_jobs) == 0):
        return

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    print("Unique salaries", set(salary_list))

    print("Unique locations", set(location_list))

    # process data and updates statistics
    analyseAndUpdate(my_database, job_details_list, location_list, salary_list)


def transfer_statistics(main_db: Database):
    """
    Clones statistics found in main_db to frontend_db

    Args:
        main_db (Database): database containing scraped data
    """
    frontend_db = Database(get_service_account_key(), "frontend_db")
    x = main_db.export_collection(main_db.stats_collection_ref)
    frontend_db.import_collection(frontend_db.stats_collection_ref, x)


def backup_to_drive():
    """
    Saves all jobs in main database to google drive in json format.
    """
    main_db = Database(get_service_account_key(True))
    df = main_db.get_dataframe()
    df.to_json('sample_jobs.json', orient='records')

def main():

    # setup database and scraper.
    main_db = Database(get_service_account_key(True))
    my_scraper = JobScraper(main_db.get_recent_urls())

    # fetch new jobs from website
    new_jobs = my_scraper.scrape()

    # if no new jobs found return
    if (len(new_jobs) == 0):
        return

    # print some info about new jobs found
    job_title_list = [job['job_title'] for job in new_jobs]
    print(len(new_jobs), ' new jobs found!')
    print(job_title_list[:5])

    # update database size
    current_db_size = main_db.get_size()
    current_db_size += len(new_jobs)
    main_db.update_size_counter(current_db_size)

    # save new jobs to database
    for job in new_jobs:
        main_db.add_job(job)

    # get data to be analysed in a list
    job_details_list = [job['job_details'] for job in new_jobs]
    salary_list = [job['salary'] for job in new_jobs]
    location_list = [job['location'] for job in new_jobs]

    # extract statistics from newly scraped data and update
    # statistics collection
    analyseAndUpdate(main_db, job_details_list, location_list, salary_list)

    # send statistics to frontend db
    transfer_statistics(main_db)

    # update job count in readme
    update_readme_job_badge(current_db_size)


if __name__ == "__main__":


    # main()
    # print(JobScraper([], 1).scrape())
