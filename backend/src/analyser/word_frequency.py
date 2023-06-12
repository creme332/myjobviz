import re
from utils.dictionary import merge_dicts


def job_title_words(job_title_list: list[str]) -> dict:
    count = {}
    for title in job_title_list:
        # remove trailing/leading spaces and convert to lowercase
        new_title = title.strip().lower()

        # remove all numbers and special characters.
        # keep only alphabets and spaces in between
        # ? https://stackoverflow.com/a/5843547/17627866
        new_title = re.sub('[^A-Za-z ]+', '', new_title)

        # count frequency of words with length > 2
        words = new_title.split()
        words = [w for w in words if (len(w) > 2)]
        wfreq = [words.count(w) for w in words]
        count = merge_dicts(count, dict(zip(words, wfreq)))
    return count
