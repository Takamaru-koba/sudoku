from typing import List
import csv

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

def load_flat81(path: str) -> List[List[int]]:
    board: List[List[int]] = []
    with open(path) as file:
        line = file.read().strip()
        line = "".join(line.split())

        if len(line) != 81:
            raise ValueError(
                "Not 81 values"
            )

        cells: List[int] = []
        for char in line:
            if char in "0.":
                cells.append(0)
            elif char.isdigit():
                cells.append(int(char))
            else:
                raise ValueError(
                    f"invalid value {char}"
                )
    board = [cells[i:i+9] for i in range(0, 81, 9)]
    return board

def load_csv(path: str) -> List[List[int]]:
    with open(path, "r", encoding="utf-8") as file:
        board: List[List[int]] = []
        text = csv.reader(file)
        for row in text:
            cells: List[int] = []
            for val in row:
                if val in "0.":
                    cells.append(0)
                elif val.isdigit() and 1 <= int(val) <= 9:
                    cells.append(int(val))
                else:
                    raise ValueError(
                        f"Not accepted board value, {val}"
                    )
            board.append(cells)
            if len(cells) != 9:
                raise ValueError(
                    f"Expected 9 value, got {len(cells)} values in Row {row}"
                )
        if len(board) != 9:
            raise ValueError(
                f"Expected 9 rows, got {len(row)}"
            )
    return board

def detect_format(text: str) -> str:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if any("," in line for line in lines):
        return "csv"
    elif len(lines) >= 9 and all("," not in line and 7 <= len(line) <= 11 for line in lines[:9]):
        return "board"
    compact = "".join(text.split())
    if len(compact) == 81 and all(ch.isdigit() or ch == "." for ch in compact):
        return "flat81"
    raise ValueError("Unknown puzzle format (cannot auto-detect)")

def load_any(path: str, fmt: str="auto"):
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()
    format = detect_format(text) if fmt == "auto" else fmt
    if format == "csv":
        return load_csv(path)
    elif format == "board":
        return load_board(path)
    elif format == "flat81":
        return load_flat81(path)
    raise ValueError(f"Unknown format: {format}")