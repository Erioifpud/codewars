'''
左减时不可跨越一个位值。比如，99不可以用IC（ {\displaystyle 100-1} 100-1）表示，而是用XCIX（ {\displaystyle [100-10]+[10-1]} [100-10]+[10-1]）表示。（等同于阿拉伯数字每位数字分别表示。）
I - 1
V - 5
X - 10
L - 50
C - 100
D - 500
M - 1000

IV - 4
IX - 9
XL - 40
XC - 90
CD - 400
CM - 900
'''

def solution(n):
    # convert int to roman string
    t = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
         ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))
    r = []
    while n:
        for i in t:
            if n >= i[1]:
                n -= i[1]
                r.append(i[0])
                break
    return ''.join(r)
