from functools import reduce
def to_camel_case(text):
    #your code here
    if not text:
        return ''
    return str(reduce(lambda x,y: x[:-1] + y.upper() if x[-1] == '-' or x[-1] == '_' else x+y, text))
