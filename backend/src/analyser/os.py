import re
from utils.dictionary import (boolean_to_int, merge_dicts)
from utils.constants import OPERATING_SYSTEMS


def os_count(job_details_list):
    count = {OPERATING_SYSTEMS[i]: 0 for i in range(0, len(OPERATING_SYSTEMS))}

    for job_detail in job_details_list:
        res = boolean_to_int(os_check(job_detail))
        count = merge_dicts(count, res)
    return count


def os_check(job_details):
    """Returns a list of os present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of os.
    """

    job_details = job_details.lower()
    words = re.findall(r'\w+', job_details)

    is_present = {OPERATING_SYSTEMS[i]: False for i in range(
        0, len(OPERATING_SYSTEMS))}

    for key in is_present:
        lang = key.lower()
        if (lang in words):
            is_present[key] = True

    return is_present
