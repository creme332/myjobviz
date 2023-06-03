def salary_count(salary_list: list[str]) -> dict[str, int]:
    """
    Count the number of times each salary occur in list

    NOTE: Not all jobs give salary ranges. Some "invalid" ranges
    such as `See description` and `Negotiable` will be present.

    Args:
        salary_list (list[str]): A list of salaries

    Returns:
        dict[str, int]: Count of each salary
    """
    # ? myjob.mu website has a consistent spelling of salaries so
    # ? there are no corner cases
    salary_count = dict()
    for location in salary_list:
        # remove special characters
        sanitized_location = location.replace('\r\n', '',).strip()
        # update count
        salary_count[sanitized_location] = salary_count.get(
            sanitized_location, 0) + 1
    return salary_count
