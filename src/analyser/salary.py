#!venv/bin/python3
import unittest


def salary_count(salary_list):
    count = {'10,000 - 20,000': 0, '21,000 - 30,000': 0,
             '31,000 - 40,000': 0, '41,000 - 50,000': 0,
             '51,000 - 75,000': 0, '76,000 - 100,000': 0}
    invalid_salaries = ['Not disclosed', 'Negotiable', 'See description']

    for salary in salary_list:
        if (salary not in invalid_salaries):
            if (salary not in count.keys()):
                raise Exception('Unknown salary range', salary)
            count[salary] += 1
    return count


class Test(unittest.TestCase):

    def test_valid_salaries(self):
        list = ['10,000 - 20,000', '51,000 - 75,000', '76,000 - 100,000']
        self.assertEqual(salary_count(list), {'10,000 - 20,000': 1,
                                              '21,000 - 30,000': 0,
                                              '31,000 - 40,000': 0,
                                              '41,000 - 50,000': 0,
                                              '51,000 - 75,000': 1,
                                              '76,000 - 100,000': 1})

    def test_invalid_salaries(self):
        list = ['10,000 - 20,000', 'Not disclosed',
                'Negotiable', 'See description']
        self.assertEqual(salary_count(list), {'10,000 - 20,000': 1,
                                              '21,000 - 30,000': 0,
                                              '31,000 - 40,000': 0,
                                              '41,000 - 50,000': 0,
                                              '51,000 - 75,000': 0,
                                              '76,000 - 100,000': 0})
        return

    def test_unknown_ranges(self):
        list = ['10,000 - 20,000', '50,000 - 75,000', '76,000 - 100,000']
        try:
            salary_count(list)
        except Exception:
            pass
        else:
            self.fail('unexpected exception raised')
