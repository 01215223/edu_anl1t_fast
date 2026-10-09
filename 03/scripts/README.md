# Checks for problem set 03

Scripts that check the answers in `../../03a/problem-set-03-a-solution.md` (sequences) and
`../../03b/problem-set-03-b-solution.md` (functions). They are checks, not part of the solution.

## Setup

Python packages (tested with Python 3.11):

    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt

## Scripts

| Script | Checks | Needs |
|---|---|---|
| `check_set03.py` | All limits of 03a and 03b evaluated numerically at 80 digits (large n, or x close to the point; one-sided limits; the non-existence examples; the hyperbolic identities) | mpmath |
| `../../02/scripts/check_md_github.py` | Solution files: macros outside a conservative allow-list, raw `<`/`>` in math, `$$` layout, `|` in table math | standard library (script lives in the set 02 folder) |

Run them from this folder:

    python check_set03.py
    python ../../02/scripts/check_md_github.py ../../03a/problem-set-03-a-solution.md ../../03b/problem-set-03-b-solution.md

`check_set03.py` exits with status 1 when a check fails. Numeric checks support the claimed values
but do not replace the proofs written in the solutions. Some limits converge slowly (for example
4.3 and 1.2 of 03a/03b, error of order 1/sqrt(n) or sqrt(x)); the script uses larger n or smaller x
for them.
