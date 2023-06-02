import re
from utils.dictionary import (boolean_to_int, merge_dicts)


def cp_count(job_details_list: list[str]) -> dict[str, int]:
    count = {"AWS": 0,
             "Google Cloud": 0,
             "Azure": 0,
             "Heroku": 0,
             "DigitalOcean": 0,
             "Watson": 0,
             "Oracle Cloud Infrastructure": 0
             }
    for job_detail in job_details_list:
        res = boolean_to_int(cloud_platforms_check(job_detail))
        count = merge_dicts(count, res)
    return count


def cloud_platforms_check(job_details):
    """Returns a list of cloud platforms present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of cloud platforms.
    """

    job_details = job_details.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_details)

    is_present = {"AWS": False,
                  "Google Cloud": False,
                  "Azure": False,
                  "Heroku": False,
                  "DigitalOcean": False,
                  "Watson": False,
                  "Oracle Cloud Infrastructure": False
                  }

    for key in is_present:
        lang = key.lower()
        if (lang in job_details):
            is_present[key] = True

    # corner case for AWS
    is_present['AWS'] = 'aws' in words

    return is_present
