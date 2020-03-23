import numpy as np

def sudoku(board, row, col):

    if row == 9:
        print(board)
        return
    if col == 9:
        sudoku(board, row + 1, 0)
        return

    if board[row, col] != 0:
        sudoku(board, row, col + 1)
    else:
        for item in range(1, 10):
            if isSafe(board, row, col, item):
                board[row, col] = item
                sudoku(board, row, col + 1)
                board[row, col] = 0
def isSafe(board, row, col, item):

    if item in board[row, :]:
        return False

    if item in board[:, col]:
        return False

    row_s = row - (row%3)
    col_s = col - (col%3)
    cut = board[row_s:row_s+3, col_s:col_s+3]

    if item in cut.flatten():
        return False

    return True

grid =                [[0, 0, 0, 0, 0, 8, 4, 0, 0],
                      [5, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 8, 7, 0, 0, 0, 0, 3, 1],
                      [0, 0, 3, 0, 1, 0, 0, 8, 0],
                      [9, 0, 0, 8, 6, 3, 0, 0, 5],
                      [0, 5, 0, 0, 9, 0, 6, 0, 0],
                      [1, 3, 0, 0, 0, 0, 2, 5, 0],
                      [0, 0, 0, 0, 0, 0, 0, 7, 4],
                      [0, 0, 5, 2, 0, 6, 3, 0, 0]]
board = np.array(grid)


sudoku(board,0,0)

def li_sudoku(board, row, col):

    if row == 9:
        return [board.copy()]
    if col == 9:
        return li_sudoku(board, row + 1, 0)


    if board[row, col] != 0:
        return li_sudoku(board, row, col + 1)
    else:
        acc = []
        for item in range(1, 10):
            if isSafe(board, row, col, item):
                board[row, col] = item
                acc.extend(li_sudoku(board, row, col + 1))
                board[row, col] = 0

        return acc

answers = li_sudoku(board, 0, 0)
print(answers)