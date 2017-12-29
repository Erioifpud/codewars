'''
def p(n1, n2):
    if n1 < 0:
        return 0
    elif n1 == 0:
        return 1
    elif n1 == 1 or n2 == 1:
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
'''

import time
def p(n1, n2, buf):
    if buf.get(str(n1) + '|' + str(n2)):
        return buf.get(str(n1) + '|' + str(n2))
    else:
        if n1 < 0:
            return 0
        elif n1 == 0:
            return 1
        elif n1 == 1 or n2 == 1:
            return 1
        elif n1 < n2:
            a = p(n1, n1, buf)
            buf[str(n1) + '|' + str(n1)] = a
            return a
        elif n1 == n2:
            a = p(n1, n1 - 1, buf)
            buf[str(n1) + '|' + str(n1 - 1)] = a
            return 1 + a
        else:
            a, b = p(n1 - n2, n2, buf), p(n1, n2 - 1, buf)
            buf[str(n1 - n2) + '|' + str(n2)] = a
            buf[str(n1) + '|' + str(n2 - 1)] = b
            return a + b

def exp_sum(n):
    #your code here
    return p(n, n, {})

print(time.time() * 1000)
exp_sum(100)
print()
print(time.time() * 1000)
