import re
from utils.constants import OPERATING_SYSTEMS


def os_check(job_details: str) -> dict[str, bool]:
    """
    Returns a dictionary indicating which OS
    are present/missing from `job_details`

    Args:
        job_details (str): _description_

    Returns:
        dict[str, bool]: _description_
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
