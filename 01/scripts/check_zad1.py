"""Numeric check of exercise 1 of problem set 01 (Zadanie 1).

The literal substitutions f(-x), f(1/x), f(sqrt x) and f(x^2) are compared with the closed forms
in 01/problem-set-01-solution.md at random points, and the domains are checked on a grid.
Requires mpmath. Exits with status 1 if a check fails.
"""
import random
import sys

import mpmath as mp

mp.mp.dps = 50


# Definition of f, valid only for t in D_f = (0,1) U (1,inf) (x^x and log_x need x>0, x != 1).
def f(t):
    if not (t > 0 and t != 1):
        raise ValueError("t outside D_f")
    return t**t + mp.log(1 + 2*mp.sqrt(t) + 3*t**2) / mp.log(t)


def in_Df(t):
    return t > 0 and t != 1


# ---- 1. Literal substitution vs. simplified closed forms (random points in claimed domains) ----
random.seed(1)


def rand_in(intervals):
    lo, hi = random.choice(intervals)
    return mp.mpf(random.uniform(lo, hi))


checks = {
    # name: (sample intervals, literal composite, simplified closed form)
    "f(-x)": (
        [(-50, -1.0001), (-0.9999, -0.0001)],
        lambda x: f(-x),
        lambda x: (-x)**(-x) + mp.log(1 + 2*mp.sqrt(-x) + 3*x**2) / mp.log(-x),
    ),
    "f(1/x)": (
        [(0.0001, 0.9999), (1.0001, 50)],
        lambda x: f(1/x),
        # log_{1/x} b = -log_x b, and (1/x)^(1/x) = x^(-1/x)
        lambda x: x**(-1/x) - mp.log(1 + 2/mp.sqrt(x) + 3/x**2) / mp.log(x),
    ),
    "f(sqrt x)": (
        [(0.0001, 0.9999), (1.0001, 50)],
        lambda x: f(mp.sqrt(x)),
        # (sqrt x)^(sqrt x) = x^(sqrt(x)/2)
        lambda x: x**(mp.sqrt(x)/2) + mp.log(1 + 2*x**mp.mpf(0.25) + 3*x) / mp.log(mp.sqrt(x)),
    ),
    "f(x^2)": (
        [(-50, -1.0001), (-0.9999, -0.0001), (0.0001, 0.9999), (1.0001, 50)],
        lambda x: f(x**2),
        # (x^2)^(x^2) = |x|^(2x^2)
        lambda x: abs(x)**(2*x**2) + mp.log(1 + 2*abs(x) + 3*x**4) / mp.log(x**2),
    ),
}

all_ok = True
for name, (ivs, literal, closed) in checks.items():
    worst = mp.mpf(0)
    for _ in range(2000):
        x = rand_in(ivs)
        a, b = literal(x), closed(x)
        rel = abs(a - b) / max(1, abs(a))
        worst = max(worst, rel)
    ok = worst < mp.mpf(10)**(-40)
    all_ok &= ok
    print(f"{name:10s} max rel. difference over 2000 pts = {mp.nstr(worst, 3):>10s}  -> {'OK' if ok else 'MISMATCH'}")

# ---- 2. Domain check: composite defined <=> inner map t(x) lies in D_f, on a grid incl. boundaries ----
claimed = {
    "f(-x)": (lambda x: -x, lambda x: (x < -1) or (-1 < x < 0)),
    "f(1/x)": (lambda x: (1/x) if x != 0 else None, lambda x: (0 < x < 1) or (x > 1)),
    "f(sqrt x)": (lambda x: mp.sqrt(x) if x >= 0 else None, lambda x: (0 < x < 1) or (x > 1)),
    "f(x^2)": (lambda x: x**2, lambda x: x not in (-1, 0, 1)),
}

grid = [mp.mpf(k)/1000 for k in range(-3000, 3001)] + [mp.mpf(-1), mp.mpf(0), mp.mpf(1)]
for name, (inner, claim) in claimed.items():
    mism = []
    for x in grid:
        t = inner(x)
        defined = False if t is None else in_Df(t)
        if defined != claim(x):
            mism.append(x)
    ok = not mism
    all_ok &= ok
    print(f"domain {name:10s} grid of {len(grid)} pts -> {'OK' if ok else 'MISMATCH at ' + str(mism[:5])}")

print("ALL OK" if all_ok else "SOME CHECKS FAILED")
sys.exit(0 if all_ok else 1)
