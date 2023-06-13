from typing import Callable
from analyser.cloudplatforms import cp_check
from analyser.database import db_check
from analyser.language import language_check
from analyser.libraries import libraries_check
from analyser.location import location_count
from analyser.os import os_check
from analyser.tools import tools_check
from analyser.salary import salary_count
from analyser.word_frequency import job_title_words
from analyser.webframework import web_framework_check
from utils.dictionary import merge_dicts, boolean_to_int
from utils.constants import (CLOUD_PLATFORMS, DATABASES, LIBRARIES,
                             WEB_FRAMEWORKS, TOOLS, OPERATING_SYSTEMS,
                             LANGUAGES)
from classes.database import Database


def count_occurences(
        job_desc_list: list[str],
        attribute_list: list[str],
        attribute_checker: Callable[[str], dict[str, bool]]) -> dict[str, int]:
    """
    For each attribute in `attribute_list`, count the number of job
    descriptions in `job_desc_list` which mentions that attribute.
    `attribute_checker` is used to check which attributes are present
    in a particular job description.

    Args:
        job_desc_list (list[str]): A list of job descriptions
        attribute_list (list[str]): A list of attributes to be searched.
        An example is a list of web frameworks.
        attribute_checker (Callable): A function which performs a presence
        check for each attribute in `attribute_list` for a job description.

    Returns:
        dict[str, int]: _description_
    """
    # create a dictionary from list
    count = {attribute_list[i]: 0 for i in range(0, len(attribute_list))}

    for job_detail in job_desc_list:
        res = boolean_to_int(attribute_checker(job_detail))
        count = merge_dicts(count, res)
    return count


def update_analytics(main_db: Database,
                     job_title_list: list[str],
                     job_desc_list: list[str],
                     location_list: list[str],
                     salary_list: list[str]) -> None:

    # analyse job_title_list
    increment = job_title_words(job_title_list)
    main_db.update_stats(
        increment, main_db.job_title_data_ref)

    # analyse cp
    increment = count_occurences(job_desc_list, CLOUD_PLATFORMS, cp_check)
    main_db.update_stats(
        increment, main_db.cloud_data_ref)

    # analyse database
    increment = count_occurences(job_desc_list, DATABASES, db_check)
    main_db.update_stats(increment, main_db.db_data_ref)

    # analyse language
    increment = count_occurences(job_desc_list, LANGUAGES, language_check)
    main_db.update_stats(increment,
                         main_db.lang_data_ref)

    # analyse libraries
    increment = count_occurences(job_desc_list, LIBRARIES, libraries_check)
    main_db.update_stats(increment, main_db.lib_data_ref)

    # analyse location
    increment = location_count(location_list)
    main_db.update_stats(increment, main_db.loc_data_ref)

    # analyse os
    increment = count_occurences(job_desc_list, OPERATING_SYSTEMS, os_check)
    main_db.update_stats(increment, main_db.os_data_ref)

    # analyse salary
    increment = salary_count(salary_list)
    main_db.update_stats(
        increment, main_db.salary_data_ref)

    # analyse tools
    increment = count_occurences(job_desc_list, TOOLS, tools_check)
    main_db.update_stats(
        increment, main_db.tools_data_ref)

    # analyse web frameworks
    increment = count_occurences(
        job_desc_list, WEB_FRAMEWORKS, web_framework_check)
    main_db.update_stats(increment, main_db.web_data_ref)
