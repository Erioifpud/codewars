def p(n1, n2):
    if n1 == 1 or n2 == 1:
        return 1
    elif n1 < n2:
        return p(n1, n1)
    elif n1 == n2:
        return 1 + p(n1, n1 - 1)
    else:
        return p(n1 - n2, n2) + p(n1, n2 - 1)

def exp_sum(n):
    #your code here
    return p(n, n)
