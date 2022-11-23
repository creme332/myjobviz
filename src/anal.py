#!venv/bin/python3
from analyser.cloudplatforms import cp_count
from analyser.database import db_count
from analyser.language import lang_count
from analyser.libraries import lib_count
from analyser.location import location_count
from analyser.os import os_count
from analyser.tools import tools_count
from analyser.salary import salary_count
from analyser.webframework import web_count


def analyseAndUpdate(my_database, job_details_list,
                     location_list, salary_list):
    # analyse cp
    increment = cp_count(job_details_list)
    # print(increment)
    my_database.update_filtered_statistics(
        increment, my_database.cloud_data_ref)

    # analyse database
    increment = db_count(job_details_list)
    my_database.update_filtered_statistics(increment, my_database.db_data_ref)

    # analyse language
    increment = lang_count(job_details_list)
    my_database.update_filtered_statistics(increment,
                                           my_database.lang_data_ref)

    # analyse libraries
    increment = lib_count(job_details_list)
    my_database.update_filtered_statistics(increment, my_database.lib_data_ref)

    # analyse location
    increment = location_count(location_list)
    my_database.update_filtered_statistics(increment, my_database.loc_data_ref)

    # analyse os
    increment = os_count(job_details_list)
    my_database.update_filtered_statistics(increment, my_database.os_data_ref)

    # analyse salary
    increment = salary_count(salary_list)
    my_database.update_filtered_statistics(
        increment, my_database.salary_data_ref)

    # analyse tools
    increment = tools_count(job_details_list)
    my_database.update_filtered_statistics(
        increment, my_database.tools_data_ref)

    # analyse web frameworks
    increment = web_count(job_details_list)
    my_database.update_filtered_statistics(increment, my_database.web_data_ref)
