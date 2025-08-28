import pytest
from sudoku.board import row_ok, column_ok, box_ok, is_valid_move

def test_row_ok_valid():
    board = [[0, 1, 2, 3, 4, 5, 6, 7, 8]]
    assert row_ok(board, 0) is True

def test_row_ok_invalid():
    board = [[0, 0, 0, 0, 0, 0, 0, 1, 1]]
    with pytest.raises(ValueError) as e:
        row_ok(board, 0)
    msg = str(e.value)

    assert "Row 0" in msg
    assert "Digit 1" in msg

def test_column_ok_valid():
    board = [
        [5,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [3,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [7,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [9,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
    ]
    assert column_ok(board, 0) is True

def test_column_ok_invalid():
    board = [
        [5,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [3,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [7,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [9,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [5,0,0,0,0,0,0,0,0],
    ]
    with pytest.raises(ValueError) as e:
        column_ok(board, 0)
    
    msg = str(e.value)

    assert "Column 0" in msg
    assert "Digit 5" in msg


def test_board_ok_valid():
    board = [
    [5, 3, 0, 0, 0, 0, 0, 0, 0],  # 5,3 in box
    [6, 0, 0, 0, 0, 0, 0, 0, 0],  # 6 in box
    [0, 9, 8, 0, 0, 0, 0, 0, 0],  # 9,8 in box
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    
    assert box_ok(board, 0, 0) is True

def test_box_ok_invalid():
    board = [
    [5, 3, 0, 0, 0, 0, 0, 0, 0],  # first 5
    [6, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 9, 8, 0, 0, 0, 0, 0, 0],  # second 5 → duplicate
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    with pytest.raises(ValueError) as e:
        box_ok(board, 0, 0)
    
    msg = str(e.value)

    assert "Row 0" in msg
    assert "Column 0" in msg
    assert "Digit 5" in msg

def test_is_valid_move_valid():
    # A standard starter board (zeros are empty)
    board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    assert is_valid_move(board, 4, 5, 7) is True
    
