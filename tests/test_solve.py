import sudoku.board as B
from sudoku.load_board import load_any

def test_solve_valid():
    board = load_any("data/flat81.txt")
    B.steps = 0
    ok = B.solve(board)
    assert ok == True