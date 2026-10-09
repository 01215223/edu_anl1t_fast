"""Checks the tables of the problem set 01 solution file against exact values.

Checks that every table has a consistent shape, that the four value tables (2.1, 2.2, 5.1, 5.2) and
the five sign tables (3.1, 3.2, 3.4, 6.3, 6.6) match exact math. Usage: python check_md_tables.py [FILE]
(FILE defaults to ../problem-set-01-solution.md). Uses only the standard library. Exits with status 1
on failure.
"""
import os
import re
import sys
from fractions import Fraction as F

DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "problem-set-01-solution.md")
path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PATH
lines = open(path, encoding="utf-8").read().split("\n")

# ---- collect tables: maximal runs of lines starting with '|'
tables, cur = [], []
for ln in lines:
    if ln.startswith("|"):
        cur.append(ln)
    else:
        if cur:
            tables.append(cur)
            cur = []
if cur:
    tables.append(cur)


def cells(row):
    parts = row.strip().strip("|").split("|")
    return [p.strip() for p in parts]


# ---- 1. shape: every row has the same number of cells as its header
shape_ok = True
for t in tables:
    n = len(cells(t[0]))
    for r in t[2:]:
        if len(cells(r)) != n:
            shape_ok = False
            print("SHAPE MISMATCH:", r[:80])
print(f"[{'OK' if shape_ok else 'FAIL'}] table shapes consistent ({len(tables)} tables)")

FRAC = re.compile(r"^\\frac(?:\{(\d+)\}|(\d))(?:\{(\d+)\}|(\d))$")


def num(s):
    s = s.strip().strip("$").strip()
    neg = s.startswith("-")
    if neg:
        s = s[1:]
    m = FRAC.match(s)
    if m:
        v = F(int(m.group(1) or m.group(2)), int(m.group(3) or m.group(4)))
    elif s.isdigit():
        v = F(int(s))
    else:
        raise ValueError(f"cannot parse number: {s!r}")
    return -v if neg else v


def txt(s):
    return s.strip().strip("$").strip()


def sgn(v):
    return "+" if v > 0 else ("-" if v < 0 else "0")


failures = 0


def report(ok, label):
    global failures
    if not ok:
        failures += 1
    print(f"[{'OK' if ok else 'FAIL'}] {label}")


# ---- 2. value tables (first cell '$x$' and second row '$f(x)$'), in file order: 2.1, 2.2, 5.1, 5.2
value_funcs = [
    ("2.1 f=(x^2-3x+2)/(4-x^2)", lambda x: None if x in (2, -2) else (x*x - 3*x + 2)/(4 - x*x)),
    ("2.2 f=-x^2+x+2 on D_f", lambda x: None if (x <= 0 or x == F(1, 9)) else -x*x + x + 2),
    ("5.1 f=1/|x-1|", lambda x: None if x == 1 else 1/abs(x - 1)),
    ("5.2 f=x^2+x+6 on D_f", lambda x: None if (x <= -1 or x == 0) else x*x + x + 6),
]
value_tables = [t for t in tables if txt(cells(t[0])[0]) == "$x$" or cells(t[0])[0] == "$x$"]
value_tables = [t for t in tables if cells(t[0])[0] == "$x$"]
print(f"found {len(value_tables)} value tables (expected 4)")
for (name, fn), t in zip(value_funcs, value_tables):
    xs = [num(c) for c in cells(t[0])[1:]]
    ys = [num(c) for c in cells(t[2])[1:]]
    ok = len(xs) == len(ys) and all(fn(x) == y for x, y in zip(xs, ys))
    report(ok, f"value table {name}: x={[str(x) for x in xs]} f={[str(y) for y in ys]}")

# ---- 3. sign tables (first header cell 'przedział'), in file order: 3.1, 3.2, 3.4, 6.3, 6.6
sign_tables = [t for t in tables if cells(t[0])[0] == "przedział"]
print(f"found {len(sign_tables)} sign tables (expected 5)")


def expect_rows(name, cols, rows):
    """cols: list of representative x; rows: list of functions col->string."""
    return [[rf(x) for x in cols] for rf in rows]


def sgn_or_na(num_v, den_v):
    if den_v == 0:
        return "nie istnieje"
    return sgn(num_v/den_v)


# 3.1 : (1-x)(2-x)^2(x+3)^3 < 0 ; columns (-inf,-3),(-3,1),(1,2),(2,inf)
cols31 = [F(-4), F(0), F(3, 2), F(3)]
exp31 = [
    [sgn(1 - x) for x in cols31],
    [sgn((2 - x)**2) for x in cols31],
    [sgn((x + 3)**3) for x in cols31],
    [sgn((1 - x)*(2 - x)**2*(x + 3)**3) for x in cols31],
]
# 3.2 : (x+3)^3/((x^2-1)(x+1)) >= 0 ; columns (-inf,-3),-3,(-3,-1),-1,(-1,1),1,(1,inf)
cols32 = [F(-4), F(-3), F(-2), F(-1), F(0), F(1), F(2)]
den32 = lambda x: (x*x - 1)*(x + 1)  # noqa: E731
exp32 = [
    [sgn((x + 3)**3) for x in cols32],
    [sgn(den32(x)) for x in cols32],
    [sgn_or_na((x + 3)**3, den32(x)) for x in cols32],
]
# 3.4 : (x^2-x)/(log2 x - 1) <= 0 ; columns (0,1),1,(1,2),2,(2,inf)
cols34 = [F(1, 2), F(1), F(3, 2), F(2), F(3)]
exp34 = [
    [sgn(x*x - x) for x in cols34],
    [sgn(x - 2) for x in cols34],  # sign of log2 x - 1 equals sign of x - 2 for x>0
    [sgn_or_na(x*x - x, x - 2) for x in cols34],
]
# 6.3 : (x-3)/((1-x)(2-x)^2) >= 0 ; columns (-inf,1),1,(1,2),2,(2,3),3,(3,inf)
cols63 = [F(0), F(1), F(3, 2), F(2), F(5, 2), F(3), F(4)]


def q63(x):
    return None if x in (1, 2) else (x - 3)/((1 - x)*(2 - x)**2)


exp63 = [
    [sgn(x - 3) for x in cols63],
    [sgn(1 - x) for x in cols63],
    [("nie istnieje" if q63(x) is None else sgn(q63(x))) for x in cols63],
]
# 6.6 : (log2 x - 1)/(x^2-x) <= 0 ; columns (0,1),(1,2),2,(2,inf)
cols66 = [F(1, 2), F(3, 2), F(2), F(3)]
exp66 = [
    [sgn(x - 2) for x in cols66],
    [sgn(x*x - x) for x in cols66],
    [("0" if (x - 2) == 0 else sgn_or_na(x - 2, x*x - x)) for x in cols66],
]

expected_sign_tables = [("3.1", exp31), ("3.2", exp32), ("3.4", exp34), ("6.3", exp63), ("6.6", exp66)]
for (name, exp), t in zip(expected_sign_tables, sign_tables):
    body = t[2:]
    got = [[txt(c) for c in cells(r)[1:]] for r in body]
    ok = len(got) == len(exp) and all(g == e for g, e in zip(got, exp))
    report(ok, f"sign table {name}")
    if not ok:
        print("   got:     ", got)
        print("   expected:", exp)

print()
print("ALL TABLE CHECKS PASSED" if failures == 0 else f"TABLE FAILURES: {failures}")
sys.exit(1 if failures else 0)
