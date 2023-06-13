import unittest
import pandas as pd
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.cloudplatforms import cp_check
from src.analyser.runner import count_occurences
from src.utils.constants import CLOUD_PLATFORMS


class TestCloudPlatforms(unittest.TestCase):
    def test_uppercase(self):
        string = 'i love WATSON'
        result = get_true_keys(cp_check(string))
        self.assertEqual(
            set(result),
            {'Watson'})

    def test_long_names(self):
        string = 'Google Cloud; Oracle Cloud Infrastructure'
        result = get_true_keys(cp_check(string))
        self.assertEqual(set(result),
                         {'Google Cloud',
                          'Oracle Cloud Infrastructure'})

    def test_substring(self):
        # AWS must not be matched here
        string = ('laws are good')
        result = get_true_keys(
            cp_check(string))
        self.assertCountEqual(result, [])

    def test_all(self):
        string = ','.join(CLOUD_PLATFORMS)
        result = get_true_keys(cp_check(string))
        self.assertCountEqual(set(result), set(CLOUD_PLATFORMS))

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)
        string = df['job_details'].tolist()[0]
        result = get_true_keys(cp_check(string))

        self.assertCountEqual(result, [])

    def test_getCount(self):
        test_list = ['unbuntu', 'azue azure', 'watson']
        x = count_occurences(test_list, CLOUD_PLATFORMS, cp_check)
        self.assertEqual(filter_dict(x), {'Azure': 1,
                                          'Watson': 1})
