import unittest
import pandas as pd
from analyser.dictionaryUtils import (toIntegerValues, merge_dicts,
                                      to_true_list, filter_dict)


def lib_count(job_details_list) -> dict:
    count = {".NET Framework": False,
             "NumPy": False,
             ".NET Core": False,
             "Pandas": False,
             "TensorFlow": False,
             "React Native": False,
             "Flutter": False,
             "Keras": False,
             "PyTorch": False,
             "Cordova": False,
             "Apache Spark": False,
             "Hadoop": False,
             "Tableau": False,
             "Power BI": False,
             "Power Query": False,
             }
    count = toIntegerValues(count)
    for job_detail in job_details_list:
        res = toIntegerValues(libraries_check(job_detail))
        count = merge_dicts(count, res)
    return count


def libraries_check(job_details):
    """Returns a list of libraries present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of libraries.
    """

    job_details = job_details.lower()

    is_present = {".NET Framework": False,
                  "NumPy": False,
                  ".NET Core": False,
                  "Pandas": False,
                  "TensorFlow": False,
                  "React Native": False,
                  "Flutter": False,
                  "Keras": False,
                  "PyTorch": False,
                  "Cordova": False,
                  "Apache Spark": False,
                  "Hadoop": False,
                  "Tableau": False,
                  "Power BI": False,
                  "Power Query": False,
                  }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in job_details):
            is_present[key] = True

    return is_present


class TestLibrariesCheck(unittest.TestCase):

    def test_long_names(self):
        string = 'Apache Spark'
        self.assertEqual(to_true_list(libraries_check(string)),
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
        self.assertCountEqual(to_true_list(libraries_check(string)), expected)

    # @unittest.skip('Reason for skipping')
    def test_real_job_details(self):
        data_source_filename = 'data/sample-raw.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains(".NET Core")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(to_true_list(libraries_check(
            string)), ['.NET Core'])

    def test_count(self):
        test_list = ['pandas', 'java c#', 'pandas']
        x = lib_count(test_list)
        # print(filter_dict(x))
        self.assertEqual(filter_dict(x), {'Pandas': 2})
