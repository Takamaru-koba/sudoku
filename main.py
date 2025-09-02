import sys
import argparse
import sudoku.board as sb
from sudoku.board import print_board, find_empty, candidates, new_solve
from sudoku.load_board import load_board, load_any

def parser_args():
    parser = argparse.ArgumentParser(description="CLI for loading file")
    parser.add_argument("--load", required=True, help="Path to puzzle file")
    parser.add_argument("--show", action="store_true", help="print loaded file")
    parser.add_argument("--hint", action="store_true", help="printing hints")
    parser.add_argument("--solve", action="store_true", help="This solves the board")
    return parser.parse_args()

def main():
    args = parser_args()
    try:
        board = load_any(args.load)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    if args.hint:
        cell = find_empty(board)
        if cell is None:
            print("No empty. Completed?")
        else:
            r, c = cell
            can = candidates(board, r, c)
            if not can:
                print(f"Dead end at Row {r}, Column {c}")
            else:
                print(f"You can fill {can} in an empty cell at Row {r} Column {c}")

    if args.solve:
        sb.steps = 0
        answer = new_solve(board)
        print(f"solved? {answer} steps:{sb.steps}")
        print_board(board)
    elif args.show:
        print_board(board)

if __name__ ==  "__main__":
    main()