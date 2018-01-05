def boolfuck(code, input=""):
    li = list(map(int, ''.join([bin(ord(i))[2:].rjust(8, '0')[::-1] for i in input])))
    var = {'mem': [0], 'ptr': 0, 'i': li, 'iptr': 0, 'out': ''}
    new_code, indent = [], 0
    for c in code:
        cur_indent = indent
        if c == '>': line = 'ptr += 1; ptr < len(mem) or mem.append(0)'
        elif c == '<': line = 'ptr -= 1; ptr >= 0 or mem.insert(0, 0)'
        elif c == '+': line = 'mem[ptr] = (mem[ptr] + 1) % 2'
        elif c == ';': line = 'out += str(mem[ptr])'
        elif c == ',': line = 'mem[ptr] = 0 if len(i) == 0 else i.pop(0)'
        elif c == '[': line = 'while mem[ptr]:'; indent += 1
        elif c == ']': line = ''; indent -= 1
        else: line = ''
        new_code.append('\t' * cur_indent + line)
    exec('\n'.join(new_code), var)
    out, res = var['out'], ''
    while out:
        res += chr(int(out[:8].ljust(8, '0')[::-1], 2))
        out = out[8:]
    return res
