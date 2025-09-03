from sudoku.board import is_valid_move, find_empty

def do_move(board, r, c, v, history):
    old = board[r][c]
    if v != 0 and not is_valid_move(board, r, c, v):
        raise ValueError("Invalid move")
    history.append((r, c, old))
    board[r][c] = v
    print("ok")
    return board

def undo(board, history):
    if not history:
        raise ValueError("No moves to undo")
    r, c, old = history.pop()
    board[r][c] = old
    print("undone")
    return board
