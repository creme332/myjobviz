import re
from utils.constants import WEB_FRAMEWORKS


def web_framework_check(job_details: str) -> dict[str, bool]:
    """
    Returns a dictionary indicating which web frameworks
    are present/missing from `job_details`

    Args:
        job_details (str): _description_

    Returns:
        dict[str, bool]: _description_
    """

    # ! LIMITATION : Cannot distinguish between the verb react
    # ! and the framework react.

    job_details = job_details.lower()

    # list of words but without special characters
    words = re.findall(r'\w+', job_details)
    is_present = {WEB_FRAMEWORKS[i]: False for i in range(0,
                                                          len(WEB_FRAMEWORKS))}

    for key in is_present:
        lang = key.lower()
        if (lang in words):
            is_present[key] = True

    # corner case for angular /= angularjs
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

    if ('next.js' in job_details or 'nextjs' in job_details):
        is_present['Next.js'] = True

    if ('asp.net' in job_details):
        is_present['ASP.NET'] = True

    if ('ruby on rails' in job_details):
        is_present['Ruby on Rails'] = True

    if ('vue.js' in job_details or 'vuejs' in job_details):
        is_present['Vue.js'] = True

    return is_present
