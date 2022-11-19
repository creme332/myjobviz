#!venv/bin/python3
import unittest
import pandas as pd


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

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestLibrariesCheck(unittest.TestCase):

    def test_long_names(self):
        string = 'Apache Spark'
        self.assertEqual(libraries_check(string),
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
        self.assertCountEqual(libraries_check(string), expected)

    # @unittest.skip('Reason for skipping')
    def test_real_job_details(self):
        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains(".NET Core")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(libraries_check(
            string), ['.NET Core'])


if __name__ == '__main__':
    unittest.main()
    # web_framework_check('')
