import unittest
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.webframework import web_framework_check, web_count
import pandas as pd


class TestWebFramework(unittest.TestCase):

    def test_uppercase(self):
        string = 'i love SVELTE'
        self.assertEqual(get_true_keys(
            web_framework_check(string)), ['Svelte'])

    @unittest.skip('Not sure how to distinguish between'
                   ' the verb and the framework')
    def test_react(self):
        string = 'The first word of -- react to danger -- is a verb.'
        self.assertEqual(get_true_keys(web_framework_check(string)), [])

    def test_substrings(self):
        # distinguish between Angular and Angular.js
        string = 'angular.js is...'
        self.assertCountEqual(get_true_keys(web_framework_check(string)),
                              ['Angular.js'])

        string = 'angular.js is not angular'
        self.assertCountEqual(get_true_keys(web_framework_check(string)),
                              ['Angular.js', 'Angular'])

    def test_all_frameworks(self):
        string = ('Svelte,ASP.NET,FastAPI,React,'
                  'Vue.js,Express,Spring,Ruby on Rails,Django,Laravel,'
                  'Flask,Gatsby,Symfony,jQuery,Drupal,Angular.js,Angular')
        expected = ['Svelte', 'ASP.NET', 'FastAPI', 'React',
                    'Vue.js', 'Express', 'Spring', 'Ruby on Rails',
                    'Django', 'Laravel', 'Flask', 'Gatsby', 'Symfony',
                    'jQuery', 'Drupal', 'Angular.js', 'Angular']
        self.assertCountEqual(get_true_keys(
            web_framework_check(string)), expected)

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df
        df = df[df['job_details'].str.contains("angular")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(get_true_keys(web_framework_check(
            string)), ['Angular', 'React'])

    def test_getCount(self):
        test_list = ['unbuntu', 'azue azure', 'watson']
        x = web_count(test_list)
        # print(filter_dict(x))
        self.assertEqual(filter_dict(x), {})
