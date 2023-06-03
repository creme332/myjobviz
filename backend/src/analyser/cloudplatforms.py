import re
from utils.constants import CLOUD_PLATFORMS


def cp_check(job_desc: str) -> dict[str, bool]:
    """
    Returns a dictionary indicating which cloud platform is present/absent in
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
