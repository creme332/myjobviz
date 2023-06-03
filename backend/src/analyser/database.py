from __future__ import annotations
import re
from utils.constants import DATABASES


def db_check(job_desc: str) -> dict[str, bool]:
    """
    Returns a dictionary of boolean values where key-value
    represent databases present in the given job description

    Args:
        job_desc (str): Job description

    Returns:
        dict: Dictionary of boolean values
    """

    # convert to lowercase
    job_desc = job_desc.lower()

    # get the list of words in job_desc but without
    # special characters such as ,.;:
    words = re.findall(r'\w+', job_desc)

    is_present = {DATABASES[i]: False for i in range(0, len(DATABASES))}

    for key in is_present:
        lang = key.lower()
        if (lang in words and lang in job_desc):
            is_present[key] = True

    # add alternative spelling for postgreSQL
    if ('postgres' in words):
        is_present['PostgreSQL'] = True

    # corner cases for database names with more than 1 word
    if ("microsoft sql server" in job_desc):
        is_present["Microsoft SQL Server"] = True
    if ("ibm db2" in job_desc):
        is_present["IBM DB2"] = True

    # corner case for oracle database
    # do not confuse with oracle cloud
    foundOracle = False
    for i in range(0, len(words)):
        current_word = words[i]
        next_word = words[min(i+1, len(words)-1)]
        if (current_word == "oracle" and next_word != 'cloud'):
            foundOracle = True
            break
    is_present['Oracle'] = foundOracle
    # alternative spelling for oracle
    if ("oracle database" in job_desc):
        is_present["Oracle"] = True

    return is_present
