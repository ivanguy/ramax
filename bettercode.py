# -*- coding: utf-8 -*-

def isIncDecSame(data):
    if data is None:
        raise ValueError("data is None")

    # values are same
    first = data[0]
    for item in data[1:]:
        if item != first:
            break
    else:
        return True

    # values increase
    val = int(data[0])
    for item in data[1:]:
        if int(item) == val + 1:
            val += 1
        else:
            break
    else:
        return True

    # values decrease
    val = int(data[0])
    for item in data[1:]:
        if int(item) == val - 1:
            val -= 1
        else:
            break
    else:
        return True

    return False

