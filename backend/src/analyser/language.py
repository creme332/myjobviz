import re
from utils.constants import LANGUAGES


def language_check(job_details: str) -> dict[str, bool]:
    """
    Returns a dictionary indicating which languages
    are present/missing from `job_details`

    Args:
        job_details (str): _description_

    Returns:
        dict[str, bool]: _description_
    """
    job_details = job_details.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_details)

    is_present = {LANGUAGES[i]: False for i in range(0, len(LANGUAGES))}

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
