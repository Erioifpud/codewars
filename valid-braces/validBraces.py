import re
def validBraces(string):
    ex = re.compile(r'\(\)|\[\]|{}')
    while ex.search(string):
        string = ex.sub('', string)
    return not bool(string)
