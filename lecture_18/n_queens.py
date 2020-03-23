def queens(board, row, n):

    if row == n:
        print("solution mil gaya")
        return

    for col in range(0, n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            queens(board,row + 1, n)
            board[row][col] = False

def is_safe(board, row, col, n):

    # checking above
    for i in range(0, row):
        if board[i][col]:
            return False

    # checking left
    steps = min(row, col)
    for i in range(1, steps + 1):
        if board[row-i][col-i]:
            return False

    # checking right
    steps = min(row, n - 1 - col)
    for i in range(1, steps + 1):
        if board[row - i][col + i]:
            return False

    return True

n = 4

board = [[False] * n for i in range(n)]

queens(board, 0, n)

def is_safe(board, row, col, n):

    for