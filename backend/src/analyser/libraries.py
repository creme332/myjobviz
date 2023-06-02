from utils.dictionary import (boolean_to_int, merge_dicts)
from utils.constants import LIBRARIES


def lib_count(job_details_list: list[str]) -> dict[str, int]:
    count = {LIBRARIES[i]: 0 for i in range(0, len(LIBRARIES))}

    for job_detail in job_details_list:
        res = boolean_to_int(libraries_check(job_detail))
        count = merge_dicts(count, res)
    return count


def libraries_check(job_details):
    """Returns a list of libraries present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of libraries.
    """

    job_details = job_details.lower()

    is_present = {LIBRARIES[i]: False for i in range(0, len(LIBRARIES))}

    for key in is_present:
        lang = key.lower()
        if (lang in job_details):
            is_present[key] = True

    return is_present
