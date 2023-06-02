import re
from utils.dictionary import (boolean_to_int, merge_dicts)


def os_count(job_details_list):
    count = {
        "Windows": False,
        "Mac": False,
        "Linux": False,
    }
    count = boolean_to_int(count)
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

    is_present = {
        "Windows": False,
        "Mac": False,
        "Linux": False,
    }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in words):
            is_present[key] = True

    return is_present
