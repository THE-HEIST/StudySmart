# StudySmart

A command-line assignment manager for students. Track your assignments, set deadlines, calculate priority scores, and monitor your progress — all from the terminal.

## What it does

StudySmart helps you organize your schoolwork by letting you:

- **Add assignments** with a name, module, deadline, and difficulty level (1-5)
- **View assignments** sorted by priority (most urgent first)
- **Mark assignments as done** and undo if you change your mind
- **Delete assignments** you no longer need
- **See a study summary** with your completion rate
- **Clear the terminal** when things get cluttered

The priority system automatically scores each assignment based on how hard it is and how many days are left. The closer the deadline and the harder the task, the higher it ranks.

## Quick start

```bash
# Clone the repository
git clone https://github.com/THE-HEIST/StudySmart.git
cd StudySmart

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Option 2: Jupyter Notebook File

Start StudySmart by opening the `main.ipynb` in Anaconda Navigator or other Notebook editor and run the main cell.

The application will then display the main menu and is ready to use.

> **Note:** The ZIP file contains the complete project files required to run StudySmart. The GitHub repository provides the same project with its version history and development structure. For a quick demonstration, the ZIP version can be used directly without cloning the repository.

## How it works

When you run `python main.py`, you see a welcome message and then the main menu:

```
No    Function Name
---------------------------------------------
1     View Assignments
2     Add Assignment
3     Delete Assignment
4     Mark Assignment as Done
5     Undo Mark Assignment as Done
6     Show Study Summary
7     Clear Terminal
0     Exit
```

Each time you start the program, it recalculates all priority scores based on today's date. An assignment with difficulty 5 due tomorrow gets a score of 2.5 (HIGH), while one with difficulty 1 due in 10 days gets 0.09 (LOW). Overdue assignments get a special score of 99999 and are labeled "OVERDUE".

## Project structure

```
StudySmart/
├── main.py                          # Entry point
├── src/
│   ├── LangaDB/
│   │   └── controllers.py           # Custom JSON database engine
│   ├── data_processing_module/
│   │   ├── config.py                # Database setup (users + assignments)
│   │   └── config4test.py           # Database setup for tests
│   └── core/
│       ├── authentication/          # Login/signup (not used in current version)
│       ├── common/
│       │   ├── calculate_priority.py # Priority scoring algorithm
│       │   └── product.py           # Main menu and control flow
│       ├── create/
│       │   └── assignments.py       # Add new assignments
│       ├── read/
│       │   └── assignments.py       # View and filter assignments
│       ├── update/
│       │   └── mark_as_done.py      # Mark/undo completion
│       └── delete/
│           └── assignment.py        # Delete assignments
├── tests/
│   ├── create/test_assignment.py
│   ├── read/test_assignment.py
│   ├── update/test_mark_completed.py
│   ├── delete/test_delete.py
│   └── common/priority_calculate/
│       ├── test_calculate.py
│       └── test_leveling.py
├── requirements.txt
└── pyproject.toml
```

## Data storage

StudySmart uses a custom lightweight database called **LangaDB** — a Python class that stores data as JSON files on disk. No external database server is needed. The data files live in `src/data/`:

- `assignments.json` — your assignments
- `users.json` — user accounts (currently not used)

## Running tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/create/test_assignment.py -v

# Run with coverage report
pytest --cov=src
```

Tests use a separate database in `src/data/test/` so they never touch your real data.

## Documentation

**[StudySmart Documentation →](https://the-heist.github.io/THE-HEIST/)**

The documentation website covers every file in the project with line-by-line explanations, designed for people who are new to programming.

## Tech stack

- **Python 3.9+**
- **LangaDB** — custom JSON file-based database (built into the project)
- **pytest** — testing framework
- **GitHub Actions** — continuous integration (tests on Python 3.9–3.13)

## Team

THE HEIST — Hùng Anh, Quốc Bảo, Trang Anh, Bayane

## License

MIT License. See [LICENSE](LICENSE) for details.
