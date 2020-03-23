

def maze(board, c_r, c_c, t_r, t_c, rows, cols, path=""):

    if (c_r == t_r) and (c_c == t_c):
        print(path)
        return

    if (c_r not in range(0, rows)) or (c_c not in range(0, cols)):
        return

    if board[c_r][c_c]:
        return
    board[c_r][c_c] = True
    maze(board, c_r - 1, c_c, t_r, t_c, rows, cols, path+"U")
    maze(board, c_r + 1, c_c, t_r, t_c, rows, cols, path+"D")
    maze(board, c_r, c_c - 1, t_r, t_c, rows, cols, path+"L")
    maze(board, c_r, c_c + 1, t_r, t_c, rows, cols, path+"R")
    board[c_r][c_c] = False

board = [[False] * 5 for i in range(3)]

maze(board, 0, 0, 2, 2, 3, 5)

def maze_li(board, c_r, c_c, t_r, t_c, rows, cols, path=""):

    if (c_r == t_r) and (c_c == t_c):
        return [path]

    if (c_r not in range(0, rows)) or (c_c not in range(0, cols)):
        return []

    if board[c_r][c_c]:
        return []

    acc = []
    board[c_r][c_c] = True
    acc.extend(maze_li(board, c_r - 1, c_c, t_r, t_c, rows, cols, path+"U"))
    acc.extend(maze_li(board, c_r + 1, c_c, t_r, t_c, rows, cols, path+"D"))
    acc.extend(maze_li(board, c_r, c_c - 1, t_r, t_c, rows, cols, path+"L"))
    acc.extend(maze_li(board, c_r, c_c + 1, t_r, t_c, rows, cols, path+"R"))
    board[c_r][c_c] = False

    return acc

li = maze_li(board, 1, 3, 2, 2, 3, 5)

sorted_li = sorted(li, key=lambda item: len(item))

print(sorted_li)