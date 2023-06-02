import unittest
import pandas as pd
from utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.cloudplatforms import cloud_platforms_check, cp_count


class TestCloudPlatformsCheck(unittest.TestCase):
    def test_uppercase(self):
        string = 'i love WATSON'
        x = cloud_platforms_check(string)
        self.assertEqual(
            get_true_keys(x),
            ['Watson'])

    def test_long_names(self):
        string = 'Google Cloud; Oracle Cloud Infrastructure'
        self.assertEqual(get_true_keys(cloud_platforms_check(string)),
                         ['Google Cloud',
                          'Oracle Cloud Infrastructure'])

    def test_substring(self):
        # AWS must not be matched here
        string = ('laws are good')
        expected = []
        self.assertCountEqual(get_true_keys(
            cloud_platforms_check(string)), expected)

    def test_all(self):
        string = ('AWS,Google Cloud,Azure,Heroku,'
                  'DigitalOcean,Watson,Oracle'
                  ' Cloud Infrastructure')
        expected = ['AWS', 'Google Cloud', 'Azure', 'Heroku',
                    'DigitalOcean', 'Watson', 'Oracle Cloud Infrastructure']
        self.assertCountEqual(cloud_platforms_check(string), expected)

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)
        string = df['job_details'].tolist()[0]
        self.assertCountEqual(get_true_keys(cloud_platforms_check(string)), [])

    def test_getCount(self):
        test_list = ['unbuntu', 'azue azure', 'watson']
        x = cp_count(test_list)
        self.assertEqual(filter_dict(x), {'Azure': 1,
                                          'Watson': 1})
