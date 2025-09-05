import sys
import argparse
import sudoku.board as sb
from sudoku.board import print_board, find_empty, candidates, new_solve
from sudoku.load_board import load_any
from sudoku.move import do_move, undo

def parser_args():
    parser = argparse.ArgumentParser(description="CLI for loading file")
    parser.add_argument("--load", required=True, help="Path to puzzle file")
    parser.add_argument("--show", action="store_true", help="print loaded file")
    parser.add_argument("--hint", action="store_true", help="printing hints")
    parser.add_argument("--solve", action="store_true", help="This solves the board")
    parser.add_argument("--move", nargs=3, type=int, metavar=("R", "C", "V") ,help="move the cell")
    parser.add_argument("--undo", action="store_true", help="UNDO last move")
    parser.add_argument("--play", action="store_true", help="Let's play it!!")
    return parser.parse_args()

def main():
    digit = None
    args = parser_args()
    if not (args.play or args.solve or args.show or args.hint or args.move or args.undo):
        print("Sudoku CLI")
        print("="*11)
        print("[1] Play")
        print("[2] Auto-solve")
        print("[3] Show board")
        print("[4] Quit")
        
        digit = input("Choice: ").strip()

    try:
        board = load_any(args.load)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    state = [row[:] for row in board]
    history = []

    if args.play or digit == "1":
        print("command: move r, c, v | undo | hint | show | quit | (0 indexed)")
        while True:
            try:
                part = input("> ").split()
            except(EOFError, KeyboardInterrupt):
                break
            if not part:
                print("Invalid command")
                continue

            cmd = part[0]
            rest = part[1:]

            if cmd == "quit":
                break
            elif cmd == "move":
                try: (r, c, v) = map(int, rest)
                except ValueError:
                    print("r, c, v is not integer")
                    continue
                if len(rest) != 3:
                    print("not 3 inputs")
                    continue

                try:
                    r, c, v = map(int, rest)
                except ValueError:
                    print("r,c,v must be integers"); continue
                if not (0 <= r < 9 and 0 <= c < 9):
                    print("r,c must be in 0..8"); continue
                if not (0 <= v <= 9):
                    print("v must be 0..9 (0 erases)"); continue

                if board[r][c] != 0:
                    print ("That cell is clue")
                    continue
                if not (0 <= r < 9 and 0 <= c < 9):
                    print("r,c must be in 0..8"); continue
                if not (0 <= v <= 9):
                    print("v must be 0..9 (0 erases)"); continue
                
                try: 
                    do_move(state, r, c, v, history)
                    print_board(state)
                except ValueError as e:
                    print(e)
                    continue

            elif cmd == "undo":
                try:
                    undo(state, history)
                    print_board(state)
                except ValueError as e:
                    print(e)

            elif cmd == "hint":
                cell = find_empty(state)
                if cell is None:
                    print("No empty. Completed?")
                else:
                    r, c = cell
                    can = candidates(state, r, c)
                    if not can:
                        print(f"Dead end at Row {r}, Column {c}")
                    else:
                        print(f"You can fill {can} in an empty cell at Row {r} Column {c}")
            elif cmd == "show":
                print_board(state)
            else:
                print("unknown command")
        return 
    else:
        if args.move:
            r, c, v = args.move
            if not (0 <= r < 9 and 0 <= c < 9):
                raise ValueError("r, c must be in 0..8")
            if not (0 <= v <= 9):
                raise ValueError("v must be 0..9 (0 erases)")
            if board[r][c] != 0:
                raise ValueError("That cell is a clue")
            do_move(state, r, c, v, history)  
              
        if args.undo:
            if not history:
                raise ValueError("You can't undo yet as there is no history")
            undo(state, history)

        if args.hint:
            cell = find_empty(state)
            if cell is None:
                print("No empty. Completed?")
            else:
                r, c = cell
                can = candidates(state, r, c)
                if not can:
                    print(f"Dead end at Row {r}, Column {c}")
                else:
                    print(f"You can fill {can} in an empty cell at Row {r} Column {c}")

        if args.solve or digit == "2":
            work = [row[:] for row in state]
            sb.steps = 0
            answer = new_solve(work)
            print(f"solved? {answer} steps:{sb.steps}")
            if answer == False:
                print_board(state)
            else:
                print_board(work)
        elif args.show or digit == "3":
            print_board(state)


if __name__ ==  "__main__":
    main()