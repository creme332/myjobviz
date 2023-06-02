from utils.dictionary import (boolean_to_int, merge_dicts)


def lib_count(job_details_list) -> dict:
    count = {".NET Framework": False,
             "NumPy": False,
             ".NET Core": False,
             "Pandas": False,
             "TensorFlow": False,
             "React Native": False,
             "Flutter": False,
             "Keras": False,
             "PyTorch": False,
             "Cordova": False,
             "Apache Spark": False,
             "Hadoop": False,
             "Tableau": False,
             "Power BI": False,
             "Power Query": False,
             }
    count = boolean_to_int(count)
    for job_detail in job_details_list:
        res = boolean_to_int(libraries_check(job_detail))
        count = merge_dicts(count, res)
    return count


def libraries_check(job_details):
    """Returns a list of libraries present in `job_details`

    Args:
        job_details (str): Job details scraped from website.

    Returns:
        List[str]: A list of libraries.
    """

    job_details = job_details.lower()

    is_present = {".NET Framework": False,
                  "NumPy": False,
                  ".NET Core": False,
                  "Pandas": False,
                  "TensorFlow": False,
                  "React Native": False,
                  "Flutter": False,
                  "Keras": False,
                  "PyTorch": False,
                  "Cordova": False,
                  "Apache Spark": False,
                  "Hadoop": False,
                  "Tableau": False,
                  "Power BI": False,
                  "Power Query": False,
                  }
    # print(is_present.keys())
    # print(','.join(is_present.keys()))

    for key in is_present:
        lang = key.lower()
        if (lang in job_details):
            is_present[key] = True

    return is_present
