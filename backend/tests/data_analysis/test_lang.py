import unittest
import pandas as pd
from src.analyser.language import lang_count, language_check
from utils.dictionary import (get_true_keys, filter_dict)


class TestLanguageCheck(unittest.TestCase):

    def test_uppercase(self):
        string = 'JAVA is cool... HTML5'
        self.assertEqual(get_true_keys(
            language_check(string)), ['Java', 'HTML'])

    def test_substrings(self):
        string = 'Javascript is cool but not powershell'
        # notice there's no 'Java' and 'Shell' in expected answer
        self.assertCountEqual(get_true_keys(language_check(string)),
                              ['Javascript', 'PowerShell'])

        string = 'learn SCSS'  # CSS not present here
        self.assertCountEqual(get_true_keys(language_check(string)),
                              [])

    def test_special_characters(self):
        string = '[c++, c#]'
        self.assertCountEqual(get_true_keys(
            language_check(string)), ['C#', 'C++'])

        string = 'html/scss'
        self.assertCountEqual(get_true_keys(language_check(string)), ['HTML'])

        string = 'bash/php/python'
        self.assertCountEqual(get_true_keys(language_check(string)),
                              ['Bash', 'PHP', 'Python'])

    def test_all_languages(self):
        string = ('C++, Java, Python, Javascript,'
                  'PHP, HTML, CSS, Clojure, C#, Bash,'
                  'Shell, PowerShell, Kotlin, Rust,'
                  'Typescript, SQL, Ruby, Dart')
        expected = ['C++', 'Java', 'Python',
                    'Javascript', 'PHP', 'HTML',
                    'CSS', 'Clojure', 'C#', 'Bash',
                    'Shell', 'PowerShell', 'Kotlin',
                    'Rust', 'Typescript', 'SQL',
                    'Ruby', 'Dart']
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

    def test_ruby_corner_case(self):
        string = ('ruby on rail is a framework')
        expected = []
        # here even though ruby is present in string, it is not
        # related to the Ruby programming language
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

        string = ('oh my ruby')
        expected = ['Ruby']
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

        string = ('oh my ruby on fleek')
        expected = []
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

        string = ('oh my ruby on rail')
        expected = []
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

        string = ('oh my ruby on rails')
        expected = []
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)
        string = df.head()['job_details'].values[0]
        self.assertCountEqual(get_true_keys(language_check(string)), [
                              'Javascript', 'HTML'])

    def test_lang_count(self):
        test_list = ['c# java', 'java c#', 'watson']
        x = lang_count(test_list)
        # print(filter_dict(x))
        self.assertEqual(filter_dict(x), {'Java': 2, 'C#': 2})
