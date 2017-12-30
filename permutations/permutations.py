import itertools

def permutations(string):
    #your code here
    return [''.join(i) for i in set(itertools.permutations(list(string)))]
