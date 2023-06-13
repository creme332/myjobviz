import unittest
import pandas as pd
from src.analyser.language import language_check
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.utils.constants import LANGUAGES
from src.analyser.runner import count_occurences


class TestLanguage(unittest.TestCase):

    def test_uppercase(self):
        string = 'JAVA is cool... HTML5'
        result = set(get_true_keys(
            language_check(string)))
        self.assertEqual(result, {'Java', 'HTML'})

    def test_css(self):
        string = 'learn SCSS'  # CSS not present here
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result,
                              {})
        # ! False positive: tailwind css \= css
        string = 'i love Tailwind CSS'
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result,
                              {'CSS'})

    def test_substrings(self):
        string = 'Javascript is cool but not powershell'
        result = set(get_true_keys(
            language_check(string)))
        # notice there's no 'Java' and 'Shell' in expected answer
        self.assertCountEqual(result,
                              {'Javascript', 'PowerShell'})

    def test_special_characters(self):
        string = '[c++, c#]'
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result, {'C#', 'C++'})

        string = 'html/scss'
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result, {'HTML'})

        string = 'bash/php/python'
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result,
                              {'Bash', 'PHP', 'Python'})

    def test_all_languages(self):
        string = ','.join(LANGUAGES)
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result, set(LANGUAGES))

    def test_ruby_corner_case(self):
        string = ('ruby on rail is a framework')
        result = set(get_true_keys(
            language_check(string)))
        # here even though ruby is present in string, it is not
        # related to the Ruby programming language
        self.assertCountEqual(result, {})

        string = ('oh my ruby')
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result, {'Ruby'})

        string = ('oh my ruby on fleek')
        result = set(get_true_keys(
            language_check(string)))
        expected = []
        self.assertCountEqual(get_true_keys(language_check(string)), expected)

        string = ('oh my ruby on rail')
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result, {})

        string = ('oh my ruby on rails')
        result = set(get_true_keys(
            language_check(string)))
        self.assertCountEqual(result, {})

    @unittest.skip('Missing sample data')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)
        string = df.head()['job_details'].values[0]
        self.assertCountEqual(get_true_keys(language_check(string)), [
                              'Javascript', 'HTML'])

    def test_lang_count(self):
        test_list = ['c# java', 'java c#', 'watson']
        x = count_occurences(test_list, LANGUAGES, language_check)
        self.assertEqual(filter_dict(x), {'Java': 2, 'C#': 2})
