def location_count(location_list: list[str]) -> dict[str, int]:
    """
    Returns a dictionary where keys are locations and values are
    frequency.

    NOTE: Not all locations are district names. Some other possible values
    of locations are: `Mauritius`, `Rodrigues`, `Overseas`.

    Args:
        location_list (list[str]): List of job locations

    Returns:
        dict[str, int]: Dictionary
    """
    # ? myjob.mu website has a consistent spelling of job locations so
    # ? there is no need to check cases
    location_count = dict()
    for location in location_list:
        # remove special characters from location
        sanitized_location = location.replace('\r\n', '',).strip()
        # update count
        location_count[sanitized_location] = location_count.get(
            sanitized_location, 0) + 1

    # ? myjob.mu website incorrectly writes "Plaine Wilhems"
    if "Plaine Wilhems" in location_count:
        # Rename Plaine Wilhems to Plaines Wilhems
        location_count['Plaines Wilhems'] = location_count.pop(
            'Plaine Wilhems')
    return location_count
