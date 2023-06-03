
import unittest
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.tools import tools_check, tools_count
from src.utils.constants import TOOLS
import pandas as pd


class TestTools(unittest.TestCase):

    def test_long_names(self):
        string = 'Unreal Engine'
        self.assertEqual(get_true_keys(tools_check(string)),
                         ['Unreal Engine'])

    def test_nodejs(self):
        string = 'node.js'
        self.assertEqual(get_true_keys(tools_check(string)),
                         ['Node.js'])

        string = 'node js'
        self.assertEqual(get_true_keys(tools_check(string)),
                         ['Node.js'])

        string = 'nodejs'
        self.assertEqual(get_true_keys(tools_check(string)),
                         ['Node.js'])

    def test_all(self):
        string = ','.join(TOOLS)
        result = get_true_keys(tools_check(string))
        self.assertCountEqual(set(result), set(TOOLS))

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains("github")]
        string = df['job_details'].tolist()[0]
        self.assertCountEqual(get_true_keys(tools_check(
            string)), ['Github', 'Gitlab', 'Docker', 'Terraform', 'Ansible'])

    def test_count(self):
        test_list = ['pandas', 'java  c#', 'pandas']
        x = tools_count(test_list)
        self.assertEqual(filter_dict(x), {})
