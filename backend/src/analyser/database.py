from __future__ import annotations
import re
from utils.dictionary import (boolean_to_int, merge_dicts,)


def db_count(job_details_list: list[str]) -> dict[str, int]:
    """
    Counts the number of job descriptions mentioning databases.

    Args:
        job_details_list (list[str]): A list of job descriptions

    Returns:
        dict: A dictionary where the key is a database name
        and the value is the number of job descriptions mentioning
        that database.
    """
    count = {
        "MySQL": 0, "PostgreSQL": 0, "SQLite": 0, "MongoDB": 0,
        "Microsoft SQL Server": 0, "Redis": 0, "MariaDB": 0,
        "Firebase": 0, "Elasticsearch": 0, "Oracle": 0,
        "DynamoDB": 0, "Cassandra": 0, "IBM DB2": 0,
        "Couchbase": 0, "NoSQL": 0
    }
    for job_detail in job_details_list:
        res = boolean_to_int(db_check(job_detail))
        count = merge_dicts(count, res)
    return count


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

    is_present = {
        "MySQL": False, "PostgreSQL": False, "SQLite": False, "MongoDB": False,
        "Microsoft SQL Server": False, "Redis": False, "MariaDB": False,
        "Firebase": False, "Elasticsearch": False, "Oracle": False,
        "DynamoDB": False, "Cassandra": False, "IBM DB2": False,
        "Couchbase": False, "NoSQL": False
    }  # ! TAKE AS PARAMETER
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

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
