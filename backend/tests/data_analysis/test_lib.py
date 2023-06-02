import unittest
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.libraries import libraries_check, lib_count
import pandas as pd


class TestLibraries(unittest.TestCase):

    def test_long_names(self):
        string = 'Apache Spark'
        self.assertEqual(get_true_keys(libraries_check(string)),
                         ['Apache Spark'])

    def test_all(self):
        string = ('.NET Framework,NumPy,.NET Core,Pandas,'
                  'TensorFlow,React Native,Flutter,Keras,PyTorch,'
                  'Cordova,Apache Spark,Hadoop,Tableau,Power BI,'
                  'Power Query')
        expected = ['.NET Framework', 'NumPy', '.NET Core',
                    'Pandas', 'TensorFlow', 'React Native',
                    'Flutter', 'Keras', 'PyTorch', 'Cordova',
                    'Apache Spark', 'Hadoop', 'Tableau',
                    'Power BI', 'Power Query']
        self.assertCountEqual(get_true_keys(libraries_check(string)), expected)

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains(".NET Core")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(get_true_keys(libraries_check(
            string)), ['.NET Core'])

    def test_count(self):
        test_list = ['pandas', 'java c#', 'pandas']
        x = lib_count(test_list)
        # print(filter_dict(x))
        self.assertEqual(filter_dict(x), {'Pandas': 2})
