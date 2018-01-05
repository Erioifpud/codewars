def my_first_interpreter(code):
    # Make your esolang interpreter here
    i, o = 0, ''
    for v in code:
        if v in '+': i = (i + 1) % 256
        elif v in '.': o += chr(i)
    return o
