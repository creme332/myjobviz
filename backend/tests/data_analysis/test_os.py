import unittest
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.os import os_check
import pandas as pd
from src.utils.constants import OPERATING_SYSTEMS
from src.analyser.runner import count_occurences


class TestOS(unittest.TestCase):

    def test_all(self):
        string = ','.join(OPERATING_SYSTEMS)
        result = get_true_keys(os_check(string))
        self.assertCountEqual(set(result), set(OPERATING_SYSTEMS))

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains("Machine")]
        string = df['job_details'].tolist()[0]
        self.assertCountEqual(get_true_keys(os_check(
            string)), [])

    def test_count(self):
        test_list = ['pandas', 'java  c#', 'pandas']
        x = count_occurences(test_list, OPERATING_SYSTEMS, os_check)
        self.assertEqual(filter_dict(x), {})
