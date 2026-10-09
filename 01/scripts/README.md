# Checks for problem set 01

Scripts that check the answers in `../problem-set-01-solution.md`. They are checks, not part of the solution.

## Setup

Python packages (tested with Python 3.11):

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

Node.js packages (only for `render_check.js`):

    npm ci

## Scripts

| Script | Checks | Needs |
|---|---|---|
| `check_zad1.py` | Exercise 1: literal substitutions vs. closed forms, and domains (numeric, 50 digits) | mpmath |
| `check_set01.py` | Exercises 2–6: claimed answers vs. the original expressions (numeric) | mpmath |
| `sympy_check_set01.py` | Exercises 2–6: symbolic cross-check | sympy |
| `check_md_tables.py` | Tables in the solution file: shape and every cell | standard library |
| `render_check.js` | Every `$…$` and `$$…$$` span renders with KaTeX (strict mode) | katex (npm) |
| `plot_set01.py` | Plots the sketches of 2.1, 2.2, 5.1, 5.2 for a visual check | numpy, matplotlib |

Run them from this folder, for example:

    python check_zad1.py
    python check_set01.py
    python sympy_check_set01.py
    python check_md_tables.py
    npm run check
    python plot_set01.py      # writes plots_set01.png next to the script (git-ignored)

The check scripts exit with status 1 when a check fails.
