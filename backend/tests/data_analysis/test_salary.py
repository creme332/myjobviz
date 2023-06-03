import unittest
from src.analyser.salary import salary_count
from src.utils.constants import PUBLIC_SALARY_RANGES


class TestSalary(unittest.TestCase):

    def test_valid_salaries(self):
        self.assertEqual(salary_count(PUBLIC_SALARY_RANGES),
                         {'Less Than 10,000': 1,
                          '10,000 - 20,000': 1,
                          '21,000 - 30,000': 1,
                          '31,000 - 40,000': 1,
                          '41,000 - 50,000': 1,
                          '51,000 - 75,000': 1,
                          '76,000 - 100,000': 1,
                          'More Than 100,000': 1
                          })
