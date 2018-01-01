def interpreter(code, tape):
    bracketPos, stack = {}, []
    for i, v in enumerate(code):
        if v in '[':
            stack.append(i)
        elif v in ']':
            if len(stack) != 0:
                previous = stack.pop()
                bracketPos[previous] = i
                bracketPos[i] = previous

    ptr, mem = 0, list(map(int, tape))
    i = 0
    while 0 <= i < len(code):
        if ptr >= len(mem) or ptr < 0:
            break
        v = code[i]
        if v in '>':
            ptr += 1
        elif v in '<':
            ptr -= 1
        elif v in '*':
            mem[ptr] = 0 if mem[ptr] == 1 else 1
        elif v in '[':
            i = bracketPos[i] if mem[ptr] == 0 else i
        elif v in ']':
            i = bracketPos[i] if mem[ptr] != 0 else i
        i += 1
    return ''.join(map(str, mem))
