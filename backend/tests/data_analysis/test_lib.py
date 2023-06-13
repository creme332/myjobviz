import unittest
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.libraries import libraries_check
from src.utils.constants import LIBRARIES
import pandas as pd
from src.analyser.runner import count_occurences


class TestLibraries(unittest.TestCase):

    def test_long_names(self):
        string = 'Apache Spark'
        self.assertEqual(get_true_keys(libraries_check(string)),
                         ['Apache Spark'])

    def test_all(self):
        string = ','.join(LIBRARIES)
        result = get_true_keys(libraries_check(string))
        self.assertCountEqual(set(result), set(LIBRARIES))

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains(".NET Core")]
        string = df['job_details'].tolist()[0]
        self.assertCountEqual(get_true_keys(libraries_check(
            string)), ['.NET Core'])

    def test_count(self):
        test_list = ['pandas', 'java c#', 'pandas']
        x = count_occurences(test_list, LIBRARIES, libraries_check)
        self.assertEqual(filter_dict(x), {'Pandas': 2})
