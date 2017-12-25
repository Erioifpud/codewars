def validSolution(board):
    # a = next(filter(lambda row: sorted(row) != [1,2,3,4,5,6,7,8,9], board), None) is None
    # b = next(filter(lambda col: sorted(col) != [1,2,3,4,5,6,7,8,9], zip(*board)), None) is None
    # or
    a = next(filter(lambda row: sum(row) != 45, board), None) is None
    b = next(filter(lambda col: sum(col) != 45, zip(*board)), None) is None
    for i in range(3):
        for j in range(3):
            line = []
            for k in board[3 * i: 3 * (i + 1)]:
                line += k[3 * j: 3 * (j + 1)]
            if sorted(line) != [1,2,3,4,5,6,7,8,9]:
                return False
    return a and b
