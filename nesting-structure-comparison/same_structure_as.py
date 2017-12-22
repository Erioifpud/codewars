def translate(li, result):
    if type(li) is list:
        result += '1'
        for l in li:
            if type(l) is not list:
                result += '2'
            else:
                result += translate(l, result)
    return result

def same_structure_as(original,other):
    return translate(original, "") == translate(other, "")
