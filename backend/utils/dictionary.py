def merge_dicts(a: dict, b: dict) -> dict:
    """
    Merges two dictionaries by adding the values of their
    common keys and by preserving uncommon keys.

    https://stackoverflow.com/a/39189980/17627866

    Args:
        a (dict): first dictionary
        b (dict): second dictionary

    Returns:
        dict: merged dictionary
    """
    for k in b:
        if k in a:
            b[k] = b[k] + a[k]
    c = {**a, **b}
    return c


def filter_dict(dict: dict[str, int]) -> dict[str, int]:
    """
    Given a dictionary, remove all key-values pair where
    where value=0

    Args:
        dict (dict): Initial dictionary

    Returns:
        dict: Final dictionary
    """
    return {x: y for x, y in dict.items() if y != 0}


def get_true_keys(booleanDict: dict[str, bool]) -> list[str]:
    """
    Given a dictionary with boolean values, return
    a list of keys whose values are True

    Args:
        booleanDict (dict): A dictionary with boolean values

    Returns:
        list: A list of keys whose values are True
    """
    # returns a list of keys which value True
    return [key for key in booleanDict if booleanDict[key]]


def boolean_to_int(dict: dict[str, bool]) -> dict[str, int]:
    """
    Given a dictionary with boolean values,
    return a dictionary where true is 1 and false is 0.

    Args:
        dict (dict): Dictionary with boolean values

    Returns:
        dict: Final dictionary where boolean values are integers
    """
    new_dict = {}
    for key, val in dict.items():
        new_dict[key] = 1 if val else 0
    return new_dict
