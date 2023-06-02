import unittest
from src.analyser.salary import salary_count


class TestSalary(unittest.TestCase):

    def test_valid_salaries(self):
        list = ['10,000 - 20,000', '51,000 - 75,000', '76,000 - 100,000']
        self.assertEqual(salary_count(list), {'10,000 - 20,000': 1,
                                              '21,000 - 30,000': 0,
                                              '31,000 - 40,000': 0,
                                              '41,000 - 50,000': 0,
                                              '51,000 - 75,000': 1,
                                              '76,000 - 100,000': 1,
                                              'More Than 100,000': 0})

    def test_invalid_salaries(self):
        list = ['10,000 - 20,000', 'Not disclosed',
                'Negotiable', 'See description']
        self.assertEqual(salary_count(list), {'10,000 - 20,000': 1,
                                              '21,000 - 30,000': 0,
                                              '31,000 - 40,000': 0,
                                              '41,000 - 50,000': 0,
                                              '51,000 - 75,000': 0,
                                              '76,000 - 100,000': 0,
                                              'More Than 100,000': 0})
        return

    def test_unknown_ranges(self):
        list = ['10,000 - 20,000', '50,000 - 75,000', '76,000 - 100,000']
        x = salary_count(list)
        self.assertEqual(x, {'10,000 - 20,000': 1,
                             '21,000 - 30,000': 0,
                             '31,000 - 40,000': 0,
                             '41,000 - 50,000': 0,
                             '51,000 - 75,000': 0,
                             '76,000 - 100,000': 1,
                             'More Than 100,000': 0})
