import pytest
from sudoku.load_board import load_board

def test_good_file():
    board = load_board("data/good_file.txt")
    assert len(board) == 9
    assert all(len(row) == 9 for row in board)
    assert all(isinstance(x, int) for row in board for x in row)
    assert any(0 in row for row in board)

def test_bad_char():
    with pytest.raises(ValueError) as e:
        load_board("data/bad_char_file.txt")
    msg = str(e.value)
    
    assert "Row 4" in msg
    assert "col 7" in msg

def test_short_row():
    with pytest.raises(ValueError) as e:
        load_board("data/short_row_file.txt")
    msg = str(e.value)

    assert "Row 3" in msg
    assert "9" in msg

def test_too_many_row():
    with pytest.raises(ValueError) as e:
        load_board("data/too_many_rows_file.txt")
    msg = str(e.value)

    assert "9" in msg