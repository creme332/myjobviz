#!venv/bin/python3
import unittest
import pandas as pd
import re


def cloud_platforms_check(job_details):
    """Returns a list of cloud platforms present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of cloud platforms.
    """

    job_details = job_details.lower()
    words = re.findall(r'\w+', job_details)

    # list of words but without special characters

    is_present = {"AWS": False,
                  "Google Cloud": False,
                  "Azure": False,
                  "Heroku": False,
                  "DigitalOcean": False,
                  "Watson": False,
                  "Oracle Cloud Infrastructure": False
                  }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in job_details):
            is_present[key] = True

    # corner case for AWS
    is_present['AWS'] = 'aws' in words

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestCloudPlatormsCheck(unittest.TestCase):

    def test_uppercase(self):
        string = 'i love WATSON'
        self.assertEqual(cloud_platforms_check(string), ['Watson'])

    def test_long_names(self):
        string = 'Google Cloud; Oracle Cloud Infrastructure'
        self.assertEqual(cloud_platforms_check(string),
                         ['Google Cloud',
                          'Oracle Cloud Infrastructure'])

    def test_substring(self):
        # AWS must not be matched here
        string = ('laws are good')
        expected = []
        self.assertCountEqual(cloud_platforms_check(string), expected)

    def test_all(self):
        string = ('AWS,Google Cloud,Azure,Heroku,'
                  'DigitalOcean,Watson,Oracle'
                  ' Cloud Infrastructure')
        expected = ['AWS', 'Google Cloud', 'Azure', 'Heroku',
                    'DigitalOcean', 'Watson', 'Oracle Cloud Infrastructure']
        self.assertCountEqual(cloud_platforms_check(string), expected)

    # @unittest.skip('Reason for skipping')
    def test_real_job_details(self):
        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(cloud_platforms_check(
            string), [])


if __name__ == '__main__':
    unittest.main()
    # web_framework_check('')
