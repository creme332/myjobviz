import re
from utils.dictionary import (boolean_to_int, merge_dicts)
from utils.constants import TOOLS


def tools_count(job_details_list):
    count = {TOOLS[i]: 0 for i in range(0, len(TOOLS))}
    for job_detail in job_details_list:
        res = boolean_to_int(tools_check(job_detail))
        count = merge_dicts(count, res)
    return count


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

    return is_present
