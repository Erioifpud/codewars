import math
def whoIsNext(names, r):
    # your code
    l = len(names)
    while r >= l:
        r, l = r - l, l * 2
    return names[math.ceil(r * len(names) / l) - 1]
