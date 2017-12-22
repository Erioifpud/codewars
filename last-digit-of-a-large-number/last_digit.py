def last_digit(n1, n2):
    if n2 == 0:
        return 1
    return [(n1 % 10) ** i % 10 for i in range(1, 5)][n2 % 4 - 1]
