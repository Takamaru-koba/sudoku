Sudoku CLI Solver

A command-line interface (CLI) Sudoku solver and player.
You can play Sudoku interactively, get hints, undo moves, or let the computer solve it using backtracking solvers. Supports multiple puzzle formats (.txt, flat81, .csv).

⸻

✨ Features
	•	Load Sudoku puzzles from:
	•	Standard .txt (9 lines, 9 digits each, with 0 or . for blanks)
	•	Flat81 single-line format (81 characters)
	•	CSV format (9×9 grid)
	•	Interactive Play Mode with:
	•	move r c v → make a move
	•	undo → undo the last move
	•	hint → show candidates for an empty cell
	•	show → display the board
	•	quit → exit play mode
	•	Auto-solver with two algorithms:
	•	Baseline → naive backtracking
	•	MRV → Minimum Remaining Values heuristic (faster)
	•	Profiling mode: measure number of steps and time to solve

⸻

🚀 Installation

Clone the repository and set up your environment:

git clone <your-repo-url>
cd sudoku_project
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt


⸻

🕹 Usage

Show Menu

python main.py --load data/good_file.txt

Play Mode

python main.py --load data/good_file.txt --play

Example commands inside play mode:

> move 0 2 4
> hint
> undo
> show
> quit

Auto-Solve

python main.py --load data/good_file.txt --solve

With Profiling

python main.py --load data/flat81.txt --solve --solver baseline --profile

Example output:

solved? True steps:510 time:3.21ms


⸻

📂 Project Structure

sudoku_project/
├── data/               # Example Sudoku boards
├── src/sudoku/         # Core modules
│   ├── board.py        # Board logic (validation, candidates, solvers)
│   ├── load_board.py   # File loaders (txt, flat81, csv)
│   ├── move.py         # Do/undo moves
├── tests/              # Pytest unit tests
├── main.py             # CLI entry point
└── README.md           # This file


⸻

🧪 Testing

Run unit tests with:

pytest


⸻

📚 Lessons Learned
	•	Implemented backtracking recursion for solving Sudoku
	•	Explored MRV heuristic to optimize search
	•	Built a CLI tool with argparse and interactive loops
	•	Learned about file parsing and handling multiple formats
	•	Practiced profiling algorithms with step counts and timing

⸻

🏁 Future Improvements
	•	Add difficulty estimation
	•	Implement more heuristics (forward-checking, constraint propagation)
	•	GUI version

⸻

⚡ Built with Python 3.13 — by Takaaki Kobayashi

⸻