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
