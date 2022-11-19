#!venv/bin/python3
import unittest
import re
import pandas as pd


def web_framework_check(job_details):
    """Returns a list of web frameworks present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of web frameworks.
    """

    # ! LIMITATION : Cannot distinguish between the verb react
    # ! and the framework react.

    job_details = job_details.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_details)
    is_present = {"Svelte": False,
                  "ASP.NET": False,
                  "FastAPI": False,
                  "React": False,
                  "Vue.js": False,  # or Vue if  english job description
                  "Express": False,
                  "Spring": False,
                  "Ruby on Rails": False,
                  "Django": False,
                  "Laravel": False,
                  "Flask": False,
                  "Gatsby": False,
                  "Symfony": False,
                  "jQuery": False,
                  "Drupal": False,
                  "Angular.js": False,
                  "Angular": False
                  }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in words and lang in job_details):
            is_present[key] = True

    # corner case for angular
    foundAngular = False
    for i in range(0, len(words)):
        current_word = words[i]
        next_word = words[min(i+1, len(words)-1)]
        if (current_word == "angular" and next_word != 'js'):
            foundAngular = True
            break
    is_present['Angular'] = foundAngular

    # alternate spellings
    if ('angular.js' in job_details or 'angularjs' in job_details):
        is_present['Angular.js'] = True

    if ('asp.net' in job_details):
        is_present['ASP.NET'] = True

    if ('ruby on rails' in job_details):
        is_present['Ruby on Rails'] = True

    if ('vue.js' in job_details or 'vuejs' in job_details):
        is_present['Vue.js'] = True

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestWebFrameworkCheck(unittest.TestCase):

    def test_uppercase(self):
        string = 'i love SVELTE'
        self.assertEqual(web_framework_check(string), ['Svelte'])

    @unittest.skip('Not sure how to distinguish between'
                   ' the verb and the framework')
    def test_react(self):
        string = 'The first word of -- react to danger -- is a verb.'
        self.assertEqual(web_framework_check(string), [])

    def test_substrings(self):
        # distinguish between Angular and Angular.js
        string = 'angular.js is...'
        self.assertCountEqual(web_framework_check(string),
                              ['Angular.js'])

        string = 'angular.js is not angular'
        self.assertCountEqual(web_framework_check(string),
                              ['Angular.js', 'Angular'])

    def test_all_frameworks(self):
        string = ('Svelte,ASP.NET,FastAPI,React,'
                  'Vue.js,Express,Spring,Ruby on Rails,Django,Laravel,'
                  'Flask,Gatsby,Symfony,jQuery,Drupal,Angular.js,Angular')
        expected = ['Svelte', 'ASP.NET', 'FastAPI', 'React',
                    'Vue.js', 'Express', 'Spring', 'Ruby on Rails',
                    'Django', 'Laravel', 'Flask', 'Gatsby', 'Symfony',
                    'jQuery', 'Drupal', 'Angular.js', 'Angular']
        self.assertCountEqual(web_framework_check(string), expected)

    # @unittest.skip('Reason for skipping')
    def test_real_job_details(self):
        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)

        # # filter df
        df = df[df['job_details'].str.contains("angular")]
        string = df['job_details'].tolist()[0]
        # print(string)
        self.assertCountEqual(web_framework_check(
            string), ['Angular', 'React'])


if __name__ == '__main__':
    unittest.main()
    # web_framework_check('')
