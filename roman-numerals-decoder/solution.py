def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    t = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
         ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    i, res = 0, 0
    for k, v in t:
        while roman[i:i + len(k)] == k:
            res += v
            i += len(k)
    return res
