import sys
import argparse
from sudoku.board import print_board
from sudoku.load_board import load_board

def parser_args():
    parser = argparse.ArgumentParser(description="CLI for loading file")
    parser.add_argument("--load", required="True", help="Path to puzzle file")
    parser.add_argument("--show", action="store_true", help="print loaded file")
    return parser.parse_args()

def main():
    args = parser_args()
    try:
        board = load_board(args.load)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    if args.show:
        print_board(board)

if __name__ ==  "__main__":
    main()