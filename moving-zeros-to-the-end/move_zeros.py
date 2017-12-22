def move_zeros(array):
    #your code here
    nz = list(filter(lambda x: not ((type(x) is int or type(x) is float) and x == 0), array))
    nz += [0 for i in range(len(array) - len(nz))]
    return nz
