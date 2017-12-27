'''
> ++ptr;
< --ptr;
+ ++*ptr;
- --*ptr;
. putchar(*ptr);
, *ptr =getch();
[ while (*ptr) {
] }

> 指针加一
< 指针减一
+ 指针指向的字节的值加一
- 指针指向的字节的值减一
. 输出指针指向的单元内容（ASCⅡ码）
, 输入内容到指针指向的单元（ASCⅡ码）
[ 如果指针指向的单元值为零，向后跳转到对应的]指令的次一指令处
] 如果指针指向的单元值不为零，向前跳转到对应的[指令的次一指令处


'''

def brain_luck(code, input):
    bracketPos, stack = {}, []
    for i, v in enumerate(code):
        if v in '[':
            stack.append(i)
        elif v in ']':
            if len(stack) != 0:
                previous = stack.pop()
                bracketPos[previous] = i
                bracketPos[i] = previous

    input = list(input)
    ptr, mem, out = 0, [0] * 255, ''
    i = 0
    while i < len(code):
        v = code[i]
        if v in '>':
            ptr += 1
        elif v in '<':
            ptr -= 1
        elif v in '+':
            mem[ptr] = 0 if mem[ptr] == 255 else mem[ptr] + 1
        elif v in '-':
            mem[ptr] = 255 if mem[ptr] == 0 else mem[ptr] - 1
        elif v in '.':
            out += chr(mem[ptr])
        elif v in ',':
            mem[ptr] = ord(input.pop(0))
        elif v in '[':
            i = bracketPos[i] if mem[ptr] == 0 else i
        elif v in ']':
            i = bracketPos[i] if mem[ptr] != 0 else i
        i += 1
    return out
