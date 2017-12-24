def dbl_linear(n):
	# your code
    r, i, j =[1], 0, 0
    while len(r) < n + 1:
        y, z = 2 * r[i] + 1, 3 * r[j] + 1
        if z < y:
            if r[-1] != z:
                r.append(z)
            j += 1
        else:
            if r[-1] != y:
                r.append(y)
            i += 1
    return r.pop()
