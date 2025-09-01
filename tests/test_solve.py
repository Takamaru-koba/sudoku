import sudoku.board as B
from sudoku.load_board import load_board

board = load_board("data/good_file.txt")
B.steps = 0
ok = B.solve(board)
print("Solved?", ok, "Steps:", B.steps)
