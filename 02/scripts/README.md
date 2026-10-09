# Checks for problem set 02

Scripts that check the answers in `../problem-set-02-solution.md`. They are checks, not part of the solution.

## Setup

Python packages (tested with Python 3.11):

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

## Scripts

| Script | Checks | Needs |
|---|---|---|
| `check_set02.py` | Exercises 1–8: claimed answers vs. the original expressions (numeric, 50 digits) and periodicity / parity / monotonicity on sample grids | mpmath |
| `check_md_github.py` | Solution file: macros outside a conservative allow-list, raw `<`/`>` in math, `|` in table math, `$$` block layout, `_`/`*` in text | standard library |
| `plot_set02.py` | Plots the sketches of exercises 1, 3, 7.3 for a visual check | numpy, matplotlib |

Run them from this folder:

    python check_set02.py
    python check_md_github.py ../problem-set-02-solution.md
    python plot_set02.py      # writes plots_set02.png next to the script (tracked; it is embedded in the solution)

`check_set02.py` exits with status 1 when a check fails. Numeric checks on grids support the
answers but do not replace the proofs written in the solution.
