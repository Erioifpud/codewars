def p(array, minRow, maxRow, minCol, maxCol, result):
    if minRow > maxRow and minCol > maxCol:
        return
    elif minRow == maxRow and minCol == maxCol:
         result.append(array[minRow][minCol])
    for i in range(minCol, maxCol + 1):
        result.append(array[minRow][i])
    result.pop()
    for i in range(minRow, maxRow + 1):
        result.append(array[i][maxCol])
    result.pop()
    for i in range(maxCol, minCol - 1, -1):
        result.append(array[maxRow][i])
    result.pop()
    for i in range(maxRow, minRow - 1, -1):
        result.append(array[i][minCol])
    result.pop()
    p(array, minRow + 1, maxRow - 1, minCol + 1, maxCol - 1, result)

def snail(array):
    n, r = len(array[0]), []
    if n == 0:
        return []
    p(array, 0, n - 1, 0, n - 1, r)
    return r
