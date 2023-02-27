# Valid Sudoku Leetcode 36
def valid_sudoku(board):
    def is_invalid(li):
        return len(a := [i for i in li if i != '.']) != len(set(a))

    # checking rows and columns
    n = 9
    if any(is_invalid([board[r][c] for c in range(n)]) or is_invalid([board[c][r] for c in range(n)]) for r in
           range(n)):
        return False

    for i in range(3):
        for j in range(3):
            region = []
            for ix in range(i * 3, (i + 1) * 3):
                for jx in range(j * 3, (j + 1) * 3):
                    if board[ix][jx] != '.':
                        region.append((board[ix][jx]))
            if is_invalid(region):
                return False
    return True
