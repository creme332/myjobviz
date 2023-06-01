from __future__ import annotations
import unittest
import re
from analyser.dictionaryUtils import (toIntegerValues, merge_dicts,
                                      to_true_list, filter_dict)


def db_count(job_details_list):
    # create a dictionary of databases to be analysed
    count = {
        "MySQL": 0, "PostgreSQL": 0, "SQLite": 0, "MongoDB": 0,
        "Microsoft SQL Server": 0, "Redis": 0, "MariaDB": 0,
        "Firebase": 0, "Elasticsearch": 0, "Oracle": 0,
        "DynamoDB": 0, "Cassandra": 0, "IBM DB2": 0,
        "Couchbase": 0, "NoSQL": 0
    }
    for job_detail in job_details_list:
        res = toIntegerValues(database_check(job_detail))
        count = merge_dicts(count, res)
    return count


def database_check(job_details: str) -> list[str]:
    """Returns a list of databases present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of databases.
    """
    job_details = job_details.lower()

    # list of words but without special characters such as ,.;:
    words = re.findall(r'\w+', job_details)

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
        if (lang in words and lang in job_details):
            is_present[key] = True

    # add alternative spelling for postgreSQL
    if ('postgres' in words):
        is_present['PostgreSQL'] = True

    # corner cases for database names with more than 1 word
    if ("microsoft sql server" in job_details):
        is_present["Microsoft SQL Server"] = True
    if ("ibm db2" in job_details):
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
    if ("oracle database" in job_details):
        is_present["Oracle"] = True

    return is_present


class TestDatabaseCheck(unittest.TestCase):

    def test_uppercase(self):
        string = 'IBM DB2'
        self.assertEqual(to_true_list(database_check(string)), ['IBM DB2'])

    def test_substrings(self):
        string = 'sql'
        self.assertCountEqual(to_true_list(database_check(string)),
                              [])

    def test_postgres(self):
        string = 'postGReSQL'
        self.assertCountEqual(to_true_list(database_check(string)),
                              ['PostgreSQL'])
        string = ('Sait utiliser les principales bases de'
                  ' données relationnelles (MySQL, Postgres)')
        self.assertCountEqual(to_true_list(database_check(string)),
                              ['PostgreSQL', 'MySQL'])

    def test_all_databases(self):
        string = ('MySQL,PostgreSQL,SQLite,MongoDB,Microsoft SQL Server,'
                  'Redis,MariaDB,Firebase,Elasticsearch,Oracle,'
                  'DynamoDB,Cassandra,IBM DB2,Couchbase,NoSQL')
        expected = ['MySQL', 'PostgreSQL', 'SQLite', 'MongoDB',
                    'Microsoft SQL Server', 'Redis', 'MariaDB',
                    'Firebase', 'Elasticsearch', 'Oracle',
                    'DynamoDB', 'Cassandra', 'IBM DB2',
                    'Couchbase', 'NoSQL']
        self.assertCountEqual(to_true_list(database_check(string)), expected)

    def test_oracle_corner_case(self):
        string = ('oracle cloud is good')
        expected = []
        self.assertCountEqual(to_true_list(database_check(string)), expected)

        string = ('oracle cloud')
        expected = []
        self.assertCountEqual(to_true_list(database_check(string)), expected)

        string = ('oracle')
        expected = []
        self.assertCountEqual(to_true_list(database_check(string)), ['Oracle'])

    def test_real_job_details(self):
        string = 'expertise mysql/mariadb (database tuning, sql optimisation)'
        self.assertCountEqual(to_true_list(
            database_check(string)), ['MySQL', 'MariaDB'])

    def test_db_count(self):
        List = ['mariadb', 'helpe das sql Mariadb', 'mysql']
        x = filter_dict(db_count(List))
        # print(x)
        self.assertCountEqual(x, {'MySQL': 1, 'MariaDB': 2})
