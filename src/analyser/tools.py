#!venv/bin/python3
import unittest
import pandas as pd
import re


def tools_check(job_details):
    """Returns a list of tools present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of tools.
    """

    job_details = job_details.lower()
    words = re.findall(r'\w+', job_details)

    is_present = {
        "Git": False,
        "Terraform": False,
        "Kubernetes": False,
        "Node.js": False,
        "Docker": False,
        "Ansible": False,
        "Yarn": False,
        "Unreal Engine": False,
        "Unity 3D": False,
        "Github": False,
        "Gitlab": False,
    }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in words and lang in job_details):
            is_present[key] = True

    if ('unreal engine' in job_details):
        is_present['Unreal Engine'] = True

    if ('unity 3d' in job_details):
        is_present['Unity 3D'] = True

    # corner case for nodejs
    # !check for  format : NODE JS
    for i in range(0, len(words)):
        current_word = words[i]
        next_word = words[min(i+1, len(words)-1)]

        if (current_word == "node" and next_word == 'js'):
            is_present['Node.js'] = True
            break

    if ('nodejs' in job_details or 'node.js' in job_details):
        is_present['Node.js'] = True

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestToolsCheck(unittest.TestCase):

    def test_long_names(self):
        string = 'Unreal Engine'
        self.assertEqual(tools_check(string),
                         ['Unreal Engine'])

    def test_nodejs(self):
        string = 'node.js'
        self.assertEqual(tools_check(string),
                         ['Node.js'])

        string = 'node js'
        self.assertEqual(tools_check(string),
                         ['Node.js'])

        string = 'nodejs'
        self.assertEqual(tools_check(string),
                         ['Node.js'])

    def test_all(self):
        string = ('Git,Terraform,Kubernetes,Node.js,Docker,Ansible,'
                  'Yarn,Unreal Engine,Unity 3D,Github')
        expected = ['Git', 'Terraform', 'Kubernetes', 'Node.js',
                    'Docker', 'Ansible', 'Yarn', 'Unreal Engine',
                    'Unity 3D', 'Github']
        self.assertCountEqual(tools_check(string), expected)

    # @unittest.skip('Reason for skipping')
    def test_real_job_details(self):
        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # filter df to include only rows mentioning sql
        df = df[df['job_details'].str.contains("github")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(tools_check(
            string), ['Github', 'Gitlab', 'Docker', 'Terraform', 'Ansible'])


if __name__ == '__main__':
    unittest.main()
