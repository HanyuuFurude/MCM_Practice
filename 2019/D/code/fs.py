def fs(val):
    if isinstance(val, str) is False:
        s = str(int(val))
    else:
        s = val
    return s
