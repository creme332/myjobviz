#!venv/bin/python3
import unittest
import re
import pandas as pd


def language_check(job_details):
    """Returns a list of programming languages present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of programming languages.
    """
    job_details = job_details.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_details)

    is_present = {
        "C++": False, "Java": False, "Python": False,
        "Javascript": False, "PHP": False,
        "HTML": False, "CSS": False, "Clojure": False,
        "C#": False, "Bash": False, "Shell": False,
        "PowerShell": False, "Kotlin": False,
        "Rust": False, "Typescript": False, "SQL": False,
        "Ruby": False, "Dart": False
    }

    # corner cases for languages containing special characters
    if ('c++' in job_details):
        is_present['C++'] = True

    if ('c#' in job_details):
        is_present['C#'] = True

    if ('html5' in job_details):
        is_present['HTML'] = True

    if ('css3' in job_details):
        is_present['CSS'] = True

    for key in is_present:
        lang = key.lower()
        if (lang in words and lang in job_details):
            is_present[key] = True

    # corner case for ruby vs ruby on rails
    foundRuby = False
    for i in range(0, len(words)):
        current_word = words[i]
        next_word = words[min(i+1, len(words)-1)]
        next_next_word = words[min(i+2, len(words)-1)]
        if (current_word == "ruby" and next_word != 'on'
            and (next_next_word != 'rails'
                 or next_next_word != 'rail')):
            foundRuby = True
            break
    is_present['Ruby'] = foundRuby

    # return matches only
    return [key for key in is_present if is_present[key]]


class TestLanguageCheck(unittest.TestCase):

    def test_uppercase(self):
        string = 'JAVA is cool... HTML5'
        self.assertEqual(language_check(string), ['Java', 'HTML'])

    def test_substrings(self):
        string = 'Javascript is cool but not powershell'
        # notice there's no 'Java' and 'Shell' in expected answer
        self.assertCountEqual(language_check(string),
                              ['Javascript', 'PowerShell'])

        string = 'learn SCSS'  # CSS not present here
        self.assertCountEqual(language_check(string),
                              [])

    def test_special_characters(self):
        string = '[c++, c#]'
        self.assertCountEqual(language_check(string), ['C#', 'C++'])

        string = 'html/scss'
        self.assertCountEqual(language_check(string), ['HTML'])

        string = 'bash/php/python'
        self.assertCountEqual(language_check(string),
                              ['Bash', 'PHP', 'Python'])

    def test_all_languages(self):
        string = ('C++, Java, Python, Javascript,'
                  'PHP, HTML, CSS, Clojure, C#, Bash,'
                  'Shell, PowerShell, Kotlin, Rust,'
                  'Typescript, SQL, Ruby, Dart')
        expected = ['C++', 'Java', 'Python',
                    'Javascript', 'PHP', 'HTML',
                    'CSS', 'Clojure', 'C#', 'Bash',
                    'Shell', 'PowerShell', 'Kotlin',
                    'Rust', 'Typescript', 'SQL',
                    'Ruby', 'Dart']
        self.assertCountEqual(language_check(string), expected)

    def test_ruby_corner_case(self):
        string = ('ruby on rail is a framework')
        expected = []
        # here even though ruby is present in string, it is not
        # related to the Ruby programming language
        self.assertCountEqual(language_check(string), expected)

        string = ('oh my ruby')
        expected = ['Ruby']
        self.assertCountEqual(language_check(string), expected)

        string = ('oh my ruby on fleek')
        expected = []
        self.assertCountEqual(language_check(string), expected)

        string = ('oh my ruby on rail')
        expected = []
        self.assertCountEqual(language_check(string), expected)

        string = ('oh my ruby on rails')
        expected = []
        self.assertCountEqual(language_check(string), expected)

    def test_real_job_details(self):
        data_source_filename = 'data/RawScrapedData.csv'
        df = pd.read_csv(data_source_filename, header=0)
        string = df.head()['job_details'].values[0]
        self.assertCountEqual(language_check(string), ['Javascript', 'HTML'])


if __name__ == '__main__':
    unittest.main()
