import re
from utils.constants import TOOLS


def tools_check(job_details: str) -> dict[str, bool]:
    """
    Returns a dictionary indicating which tools
    are present/missing from `job_details`

    Args:
        job_details (str): _description_

    Returns:
        dict[str, bool]: _description_
    """
    job_details = job_details.lower()
    words = re.findall(r'\w+', job_details)

    is_present = {TOOLS[i]: False for i in range(
        0, len(TOOLS))}

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
