'''
The tape for Brainfuck contains exactly 30,000 cells with the pointer starting
from the very left; Boolfuck contains an infinitely long tape with the pointer
starting at the "middle" (since the tape can be extended indefinitely either
direction)

Reads a bit from the input stream, storing it under the pointer. The end-user
types information using characters, though. Bytes are read in little-endian
order—the first bit read from the character a, for instance, is 1, followed by
0, 0, 0, 0, 1, 1, and finally 0. If the end-of-file has been reached, outputs a
zero to the bit under the pointer.
'''

def boolfuck(code, input=""):
    bracketPos, stack = {}, []
    for i, v in enumerate(code):
        if v in '[':
            stack.append(i)
        elif v in ']':
            if len(stack) != 0:
                previous = stack.pop()
                bracketPos[previous] = i
                bracketPos[i] = previous

    input = ''.join(list(map(lambda x: ('0' * (8 - len(x[2:])) + x[2:])[::-1], map(bin, map(ord, input)))))
    ptr, mem, out = 0, [0], ''
    i = 0
    while i < len(code):
        v = code[i]
        if v in '>':
            ptr += 1
            if ptr >= len(mem):
                mem.append(0)
        elif v in '<':
            ptr -= 1
            if ptr < 0:
                mem.insert(0, 0)
        elif v in '+':
            mem[ptr] = 0 if mem[ptr] == 1 else 1
        elif v in ';':
            out += str(mem[ptr])
        elif v in ',':
            if len(input) != 0:
                mem[ptr] = int(input[0])
                input = input[1:]
            else:
                mem[ptr] = 0
        elif v in '[':
            i = bracketPos[i] if mem[ptr] == 0 else i
        elif v in ']':
            i = bracketPos[i] if mem[ptr] == 1 else i
        i += 1

    res = list(map(''.join, zip(*[iter(out)] * 8)))
    left = len(out) % 8
    if left != 0:
        res.append(out[-left:] + '0' * (8 - len(out[-left:])))
    return ''.join(map(lambda x: chr(int(x[::-1], 2)), res))
