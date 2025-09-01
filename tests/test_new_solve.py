import sudoku.board as B
from sudoku.load_board import load_board
import pytest

def test_solved_board():
    board = load_board("data/solved_board.txt")
    assert B.find_mrv_empty(board) is B.SOLVED
    assert B.new_solve(board) is True

def test_zero_candidates():
    board = load_board("data/zero_candidates.txt")
    assert B.find_mrv_empty(board) is B.CONTRADICTION
    
def test_one_candidates():
    board = load_board("data/one_candidates.txt")
    assert B.find_mrv_empty(board) == (0, 8)

def test_steps():
    b1 = load_board("data/good_file.txt")
    b2 = [row[:] for row in b1]
    B.steps = 0
    assert B.new_solve(b1) is True
    fewer_steps = B.steps
    B.steps = 0
    assert B.solve(b2) is True
    more_steps = B.steps
    assert fewer_steps < more_steps
    