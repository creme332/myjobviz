import re
from utils.dictionary import (boolean_to_int, merge_dicts)


def lang_count(job_details_list) -> dict:
    count = {
        "C++": False, "Java": False, "Python": False,
        "Javascript": False, "PHP": False,
        "HTML": False, "CSS": False, "Clojure": False,
        "C#": False, "Bash": False, "Shell": False,
        "PowerShell": False, "Kotlin": False,
        "Rust": False, "Typescript": False, "SQL": False,
        "Ruby": False, "Dart": False
    }
    count = boolean_to_int(count)
    for job_detail in job_details_list:
        res = boolean_to_int(language_check(job_detail))
        count = merge_dicts(count, res)
    return count


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

    return is_present
