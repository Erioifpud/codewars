def calc(expr):
    # TODO: Your awesome code here
    s = []
    for c in expr.split():
        s.append(c)
        if c in ['+', '-', '*', '/']:
            si, b, a = s.pop(), s.pop(), s.pop()
            s.append(str(eval(''.join((a, si, b)))))
    return eval(s.pop()) if s else 0
