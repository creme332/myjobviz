import unittest
from utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.os import os_check, os_count
import pandas as pd


class TestOSCheck(unittest.TestCase):

    def test_all(self):
        string = ('Windows,Mac,Linux')
        expected = ['Windows', 'Mac', 'Linux']
        self.assertCountEqual(get_true_keys(os_check(string)), expected)

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains("Machine")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(get_true_keys(os_check(
            string)), [])

    def test_count(self):
        test_list = ['pandas', 'java  c#', 'pandas']
        x = os_count(test_list)
        # print(filter_dict(x))
        self.assertEqual(filter_dict(x), {})
