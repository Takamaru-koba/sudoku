from typing import List

def load_board(path: str) -> List[List[int]]:
    """Load a Sudoku board from file and return a fresh 9×9 int matrix."""
    board: List[List[int]] = []

    # encoding belongs here, not in enumerate(...)
    with open(path, "r", encoding="utf-8") as file:
        for line_num, raw in enumerate(file, start=1):
            row = raw.strip()

            # Ignore blank lines, but still enforce exactly 9 data rows overall
            if row == "":
                continue

            # Length check → message must include "Row N" and "expected 9"
            if len(row) != 9:
                raise ValueError(
                    f"Row {line_num}: expected 9 characters, got {len(row)}"
                )

            cells: List[int] = []
            for col_num, ch in enumerate(row, start=1):
                if ch in ("0", "."):
                    cells.append(0)
                elif "1" <= ch <= "9":
                    cells.append(int(ch))
                else:
                    # Must include "Row N" and "col M"
                    raise ValueError(
                        f"Row {line_num}, col {col_num}: illegal character '{ch}'. "
                        "Allowed: digits 0–9 or '.'"
                    )

            board.append(cells)

            # Too many rows → include "more than 9" (tests can assert substring "9")
            if len(board) > 9:
                raise ValueError(
                    f"Too many rows: found more than 9 by line {line_num}"
                )

    # Too few rows → include the actual count (tests can assert it mentions 9)
    if len(board) != 9:
        raise ValueError(f"Expected 9 rows, found {len(board)}")

    return board