import unittest
from src.utils.dictionary import (get_true_keys, filter_dict)
from src.analyser.webframework import web_framework_check
from src.utils.constants import WEB_FRAMEWORKS
from src.analyser.runner import count_occurences


class TestWebFramework(unittest.TestCase):

    def test_uppercase(self):
        string = 'i love SVELTE'
        result = get_true_keys(
            web_framework_check(string))
        self.assertEqual(set(result), {'Svelte'})

    def test_react(self):
        string = ' i am reactive to danger . '
        result = get_true_keys(web_framework_check(string))
        self.assertEqual(len(result), 0)

        # ! False positive. Not sure how to distinguish
        # ! between framework and verb
        string = ' you  should react fast '
        result = get_true_keys(web_framework_check(string))
        self.assertEqual(result, ['React'])

    def test_substrings(self):
        # distinguish between Angular and Angular.js
        string = 'angular.js is...'
        result = get_true_keys(web_framework_check(string))
        self.assertCountEqual(set(result),
                              {'Angular.js'})

        string = 'angular.js is not angular'
        result = get_true_keys(web_framework_check(string))
        self.assertCountEqual(set(result),
                              {'Angular.js', 'Angular'})

    def test_all_frameworks(self):
        string = ','.join(WEB_FRAMEWORKS)
        result = get_true_keys(
            web_framework_check(string))
        self.assertCountEqual(set(result), set(WEB_FRAMEWORKS))

    def test_count_occurences(self):
        test_list = ['unbuntu', 'azue azure', 'watson']
        x = count_occurences(test_list, WEB_FRAMEWORKS, web_framework_check)
        self.assertEqual(filter_dict(x), {})
