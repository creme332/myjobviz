#!venv/bin/python3
import unittest
import re
# import pandas as pd


def database_check(job_details):
    """Returns a list of databases present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of databases.
    """
    job_details = job_details.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_details)

    is_present = {
        "MySQL": False, "PostgreSQL": False, "SQLite": False, "MongoDB": False,
        "Microsoft SQL Server": False, "Redis": False, "MariaDB": False,
        "Firebase": False, "Elasticsearch": False, "Oracle": False,
        "DynamoDB": False, "Cassandra": False, "IBM DB2": False,
        "Couchbase": False, "NoSQL": False
    }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in words and lang in job_details):
            is_present[key] = True

    # corner cases for database names with more than 1 word
    if ("microsoft sql server" in job_details):
        is_present["Microsoft SQL Server"] = True
    if ("ibm db2" in job_details):
        is_present["IBM DB2"] = True

    # corner case for oracle database
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

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestDatabaseCheck(unittest.TestCase):

    def test_uppercase(self):
        string = 'IBM DB2'
        self.assertEqual(database_check(string), ['IBM DB2'])

    def test_substrings(self):
        string = 'sql'
        self.assertCountEqual(database_check(string),
                              [])

    def test_all_databases(self):
        string = ('MySQL,PostgreSQL,SQLite,MongoDB,Microsoft SQL Server,'
                  'Redis,MariaDB,Firebase,Elasticsearch,Oracle,'
                  'DynamoDB,Cassandra,IBM DB2,Couchbase,NoSQL')
        expected = ['MySQL', 'PostgreSQL', 'SQLite', 'MongoDB',
                    'Microsoft SQL Server', 'Redis', 'MariaDB',
                    'Firebase', 'Elasticsearch', 'Oracle',
                    'DynamoDB', 'Cassandra', 'IBM DB2',
                    'Couchbase', 'NoSQL']
        self.assertCountEqual(database_check(string), expected)

    def test_oracle_corner_case(self):
        string = ('oracle cloud is good')
        expected = []
        self.assertCountEqual(database_check(string), expected)

        string = ('oracle cloud')
        expected = []
        self.assertCountEqual(database_check(string), expected)

        string = ('oracle')
        expected = []
        self.assertCountEqual(database_check(string), ['Oracle'])

    def test_real_job_details(self):
        # data_source_filename = 'data/RawScrapedData.csv'
        # df = pd.read_csv(data_source_filename, header=0)

        # # filter df to include only rows mentioning sql
        # df = df[df['job_details'].str.contains("sql")]
        # string = df['job_details'].tolist()[0]

        string = 'expertise mysql/mariadb (database tuning, sql optimisation)'
        self.assertCountEqual(database_check(string), ['MySQL', 'MariaDB'])


if __name__ == '__main__':
    unittest.main()
