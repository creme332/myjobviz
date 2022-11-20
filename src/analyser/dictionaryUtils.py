def merge_dicts(a, b):
    """Merges two dictionaries by adding the values of their
    common keys and by preserving uncommon keys.

    https://stackoverflow.com/a/39189980/17627866

    Args:
        a (dict): dictionary
        b (dict): dictionary

    Returns:
        dict: merged dictionary
    """
    for k in b:
        if k in a:
            b[k] = b[k] + a[k]
    c = {**a, **b}
    return c


def filter_dict(dict):
    """Removes key-values where value=0 in dictionary

    Args:
        dict (_type_): _description_

    Returns:
        _type_: _description_
    """
    return {x: y for x, y in dict.items() if y != 0}


def to_true_list(booleanDict):
    """Returns a list of keys whose values in dictionary are True

    Args:
        booleanDict (_type_): A dictionary with boolean values

    Returns:
        _type_: _description_
    """
    # returns a list of keys which value True
    return [key for key in booleanDict if booleanDict[key]]


def toIntegerValues(dict):
    """Returns a dictionary where Boolean values are integers.

    Args:
        dict (_type_): _description_

    Returns:
        _type_: _description_
    """
    for key, val in dict.items():
        dict[key] = 1 if val else 0
    return dict
