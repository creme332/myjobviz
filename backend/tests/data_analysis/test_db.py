import unittest
from src.analyser.database import db_check
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.utils.constants import DATABASES
from src.analyser.runner import count_occurences


class TestDatabase(unittest.TestCase):

    def test_uppercase(self):
        string = 'IBM DB2'
        self.assertEqual(get_true_keys(db_check(string)), ['IBM DB2'])

    def test_substrings(self):
        string = 'sql'
        self.assertCountEqual(get_true_keys(db_check(string)),
                              [])

    def test_postgres(self):
        string = 'postGReSQL'
        self.assertCountEqual(get_true_keys(db_check(string)),
                              ['PostgreSQL'])
        string = ('Sait utiliser les principales bases de'
                  ' données relationnelles (MySQL, Postgres)')
        result = get_true_keys(db_check(string))
        self.assertCountEqual(set(result),
                              {'PostgreSQL', 'MySQL'})

    def test_all_databases(self):
        string = ','.join(DATABASES)
        result = get_true_keys(db_check(string))
        self.assertCountEqual(set(result), set(DATABASES))

    def test_oracle_corner_case(self):
        string = ('oracle cloud is good')
        expected = []
        print(get_true_keys(db_check(string)))
        self.assertCountEqual(get_true_keys(db_check(string)), expected)

        string = ('oracle cloud')
        expected = []
        self.assertCountEqual(get_true_keys(db_check(string)), expected)

        string = ('oracle')
        expected = []
        self.assertCountEqual(get_true_keys(db_check(string)), ['Oracle'])

    def test_real_job_details(self):
        string = 'expertise mysql/mariadb (database tuning, sql optimisation)'
        result = get_true_keys(db_check(string))

        self.assertCountEqual(result, {'MySQL', 'MariaDB'})

    def test_db_count(self):
        List = ['mariadb', 'helpe das sql Mariadb', 'mysql']
        x = filter_dict(count_occurences(List, DATABASES, db_check))
        self.assertCountEqual(x, {'MySQL': 1, 'MariaDB': 2})
