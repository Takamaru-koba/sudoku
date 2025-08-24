import pytest
from sudoku.board import print_board

def test_grid_is_valid(capsys):
    board = [[0]*9 for _ in range(9)]
    print_board(board)
    out, err = capsys.readouterr()
    assert("0") in out

def test_grid_is_not_valid(capsys):
    board = [[0]*8 for _ in range(9)]
    with pytest.raises(ValueError):
        print_board(board)
