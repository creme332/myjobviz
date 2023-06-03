import re
from utils.dictionary import (boolean_to_int, merge_dicts)
from utils.constants import CLOUD_PLATFORMS


def cp_count(job_desc_list: list[str]) -> dict[str, int]:
    """
    Counts the number of job descriptions mentioning cloud platforms.

    Args:
        job_desc_list (list[str]): A list of job descriptions

    Returns:
        dict[str, int]: A dictionary where the key is a database name
        and the value is the number of job descriptions mentioning
        that database.
    """

    # create a dictionary from list
    count = {CLOUD_PLATFORMS[i]: 0 for i in range(0, len(CLOUD_PLATFORMS))}

    for job_detail in job_desc_list:
        res = boolean_to_int(cp_check(job_detail))
        count = merge_dicts(count, res)
    return count


def cp_check(job_desc: str) -> dict[str, bool]:
    """
    Returns a dictionary indicating which cloud platform is present in
    given job description.

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        dict[str, bool]: Final dictionary
    """

    job_desc = job_desc.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_desc)

    # create a dictionary which stores which cloud platforms
    # are present
    is_present = {CLOUD_PLATFORMS[i]: False for i in range(
        0, len(CLOUD_PLATFORMS))}

    for key in is_present:
        lower_case_key = key.lower()
        if (lower_case_key in job_desc):
            is_present[key] = True

    # corner case for AWS
    is_present['AWS'] = 'aws' in words

    return is_present
