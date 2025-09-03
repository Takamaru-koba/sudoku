def print_board(board):
    
    if len(board) != 9:
        raise ValueError
    
    for row in board:
        if len(row) != 9:
            raise ValueError

    for i in range(9):
        k = 0
        print()
        if i % 3 == 0 and i != 0:
            for j in range(2):
                print("-"*6 + "+", end=" ")
            print("-"*6)
        for l in range(9):
            print(board[i][l], end=" ")
            if l == 2 or l == 5:
                print("|", end=" ")
    print()


def row_ok(board, r):
    seen = set()
    row = board[r]

    for val in row:
        if val == 0:
            continue
        if val in seen:
            raise ValueError(
                f"In Row {r}, the Digit {val} seen twice"
            )
        seen.add(val)
    return True


def column_ok(board, c):
    seen = set()
    
    for row in board:
        val = row[c]
        if val == 0:
            continue
        if val in seen:
            raise ValueError(
                f"In Column {c}, The Digit {val} appear twice"
                )
        seen.add(val)
    return True

def box_ok(board, r, c):
    seen = set()
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    
    for i in range(3):
        for j in range(3):
            val = board[nr + i][nc + j]
            if val == 0:
                continue
            elif val in seen:
                raise ValueError(
                    f"In the Box contain Row {r} Column {c}, the Digit {board[nr + i][nc + j]} appears twice "
                )
            seen.add(val)
    return True

def is_valid_move(board, r, c, val):
    old = board
    board[r][c] = val
    try:
        row_ok(board, r)
        column_ok(board, c)
        box_ok(board, r, c)
    except ValueError:
        board = old
        return False
    board = old
    return True

def find_empty(board):
    for row_idx, row in enumerate(board, start=0):
        for val_idx, val in enumerate(row, start=0):
            if val == 0:
                return row_idx, val_idx
    return None

def candidates(board, r, c):
    if board[r][c] != 0:
        raise ValueError(
            "This is not empty cell"
        )
    
    seen = set()
    for i in range(1, 10):
        seen.add(i)

    start_row = (r // 3) * 3
    start_column = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            val = board[start_row + i][start_column + j]
            if val == 0:
                continue
            elif val in seen:
                seen.remove(val)
    
    row = board[r]
    for val in row:
        if val == 0:
            continue
        if val in seen:
            seen.remove(val)
  
    for row in board:
        val = row[c]
        if val == 0:
            continue
        if val in seen:
            seen.remove(val)
        
    return sorted(seen)

steps = 0
def solve(board):
    global steps
    cell = find_empty(board)
    if cell is None:
        return True
    r, c = cell
    for can in candidates(board, r, c):
        if is_valid_move(board, r, c, can):
            board[r][c] = can
            steps += 1
            if solve(board):
                return True
            board[r][c] = 0
    return False

CONTRADICTION = object()
SOLVED = object()

def find_mrv_empty(board):
    best_len = 10
    best = None
    for row_idx, row in enumerate(board):
        for val_idx, val in enumerate(row):
            if val == 0:
                 cans = len(candidates(board, row_idx, val_idx))
                 if cans == 0:
                     return CONTRADICTION
                 elif cans == 1:
                     return (row_idx, val_idx)
                 elif cans < best_len:
                     best = (row_idx, val_idx)
                     best_len = cans
    if best is None:
        return SOLVED
    else:
        return best
    
def new_solve(board):
    global steps
    pick = find_mrv_empty(board)
    if pick is SOLVED:
        return True
    elif pick is CONTRADICTION:
        return False
    
    r, c = pick
    for can in candidates(board, r, c):
        board[r][c] = can
        steps += 1
        if new_solve(board):
            return True
        board[r][c] = 0
    return False
