# StudySmart User Instructions

This guide explains how to install, run, and use the current command-line version of StudySmart.

## 1. Install and start

Open a terminal in the `StudySmart` folder, then run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

Windows PowerShell users should replace the activation command with:

```powershell
.venv\Scripts\Activate.ps1
```

StudySmart recalculates saved priority scores once when the program starts and then displays the main menu.

## 2. Use the main menu

Enter the number beside the action you want and press Enter.

| Choice | Action |
|---:|---|
| `1` | View assignments |
| `2` | Add an assignment |
| `3` | Delete an assignment |
| `4` | Mark an assignment as done |
| `5` | Undo “mark as done” |
| `6` | Show the study summary |
| `7` | Clear the terminal |
| `0` | Exit StudySmart |

If the menu input is not a number, or the number is not a listed option, StudySmart prints an error and shows the menu again.

## 3. Add an assignment

Choose `2`, then enter:

1. Assignment name — it cannot be empty.
2. Module — it cannot be empty.
3. Deadline — use exactly `YYYY-MM-DD`, for example `2026-09-18`.
4. Difficulty — enter an integer from `1` to `5`.

The application then:

1. Assigns a unique ID.
2. Sets `completed` to `false`.
3. Calculates the priority score and level.
4. Saves the assignment in `src/data/assignments.json`.

An invalid date format or a non-integer difficulty cancels the current add operation and returns to the main menu. An out-of-range integer difficulty is requested again until it is between 1 and 5.

## 4. View assignments

Choose `1`, then select one of these filters:

| Choice | Result |
|---:|---|
| `1` | Only unfinished assignments |
| `2` | Only completed assignments |
| `3` | All assignments |

The table shows the assignment ID, name, module, deadline, difficulty, priority score, and completion status. Results are ordered from the highest score to the lowest. If the selected list is empty, StudySmart prints `No assignments found`.

## 5. Delete an assignment

1. Choose `3`.
2. Read the assignment table.
3. Enter the value in the `ID` column for the assignment to remove.

Use the actual assignment ID, not its row position. The record is permanently removed from `src/data/assignments.json` when the ID is valid. A missing or invalid ID leaves the data unchanged.

## 6. Mark an assignment as done

1. Choose `4`.
2. StudySmart displays unfinished assignments only.
3. Enter the assignment’s `ID`.

The selected record changes from `completed: false` to `completed: true`. If there are no unfinished assignments, the application reports that there is nothing to update.

## 7. Undo “mark as done”

1. Choose `5`.
2. StudySmart displays completed assignments only.
3. Enter the assignment’s `ID`.

The selected record changes from `completed: true` to `completed: false`.

## 8. View the study summary

Choose `6` to display:

- Total assignments
- Completed assignments
- Incomplete assignments
- Completion rate as a percentage

When there are no assignments, the completion rate is `0%`.

## 9. Understand priority

For an assignment with a future deadline:

```text
priority score = difficulty / (days remaining + 1)
```

StudySmart uses the following levels internally:

- `LOW`: score below 1
- `MEDIUM`: score from 1 up to, but not including, 2
- `HIGH`: score of 2 or more
- `OVERDUE`: deadline is today or earlier; the current code assigns score `99999`

Because lists are sorted in descending order, assignments due today or earlier appear first, followed by the highest future-deadline scores.

## 10. Data and testing

Normal usage changes `src/data/assignments.json`. Do not manually edit that file while StudySmart is running.

Run the complete test suite from the project root:

```bash
python3 -m pytest
```

The tests use files inside `src/data/test/` rather than the normal assignments file.

## Troubleshooting

### `python3: command not found`

Install Python 3.9 or newer, reopen the terminal, and try again.

### `No module named pytest`

Activate the virtual environment and reinstall the requirements:

```bash
python3 -m pip install -r requirements.txt
```

### The program rejects a deadline

Use four digits for the year, two for the month, and two for the day: `YYYY-MM-DD`.

### An assignment ID is rejected

Open the relevant list again and enter the exact value shown in its `ID` column. IDs may contain gaps after assignments are deleted.

## Program flowchart

The complete control flow is shown in [docs/studysmart-flowchart.svg](docs/studysmart-flowchart.svg).
