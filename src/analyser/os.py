#!venv/bin/python3
import unittest
import pandas as pd
import re


def os_check(job_details):
    """Returns a list of os present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of os.
    """

    job_details = job_details.lower()
    words = re.findall(r'\w+', job_details)

    is_present = {
        "Windows": False,
        "Mac": False,
        "Linux": False,
    }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in words):
            is_present[key] = True

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestOSCheck(unittest.TestCase):

    def test_all(self):
        string = ('Windows,Mac,Linux')
        expected = ['Windows', 'Mac', 'Linux']
        self.assertCountEqual(os_check(string), expected)

    # @unittest.skip('Reason for skipping')
    def test_real_job_details(self):
        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains("Machine")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(os_check(
            string), [])


if __name__ == '__main__':
    unittest.main()
