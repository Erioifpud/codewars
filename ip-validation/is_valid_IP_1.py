def is_valid_IP(strng):
    s = strng.split('.')
    a = [str(i) for i in range(256)]
    return False if len(s) != 4 else len(list(filter(lambda x: x not in a, s))) == 0
