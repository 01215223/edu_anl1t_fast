"""Symbolic cross-check of problem set 01, exercises 2-6, with SymPy.

Results marked [OK] or [DIFF] are compared with the answers in 01/problem-set-01-solution.md;
[INFO] lines are printed for review. Requires sympy. Exits with status 1 if a comparison differs.
"""
import sys

from sympy import symbols, Rational, Interval, Union, oo, S, diff, solveset, sqrt, simplify, log
from sympy.calculus.util import function_range
from sympy.solvers.inequalities import solve_univariate_inequality

x = symbols('x', real=True)


results = []


def show(label, value, expected):
    ok = (value == expected)
    results.append(ok)
    print(f"[{'OK' if ok else 'DIFF'}] {label}: sympy -> {value}" + ("" if ok else f"   (expected {expected})"))


# 3.1 polynomial inequality
s31 = solve_univariate_inequality((1 - x)*(2 - x)**2*(x + 3)**3 < 0, x, relational=False)
show("3.1", s31, Union(Interval.open(-oo, -3), Interval.open(1, 2), Interval.open(2, oo)))

# 3.2 rational inequality (x=+-1 excluded since denominator vanishes)
s32 = solve_univariate_inequality((x + 3)**3/((x**2 - 1)*(x + 1)) >= 0, x, relational=False)
show("3.2", s32, Union(Interval(-oo, -3), Interval.open(1, oo)))

# 6.3 rational inequality (x=1 and x=2 excluded)
s63 = solve_univariate_inequality((x - 3)/((1 - x)*(2 - x)**2) >= 0, x, relational=False)
print("[INFO] 6.3 sympy ->", s63, "  (expected (1,2) U (2,3]; note 2 must be excluded)")
show("6.3", s63, Union(Interval.open(1, 2), Interval.Lopen(2, 3)))

# 2.1 range and monotonicity (original rational function, natural domain)
f21 = (x**2 - 3*x + 2)/(4 - x**2)
r21 = function_range(f21, x, S.Reals)
print("[INFO] 2.1 range (sympy) ->", r21)
print("[INFO] 2.1 f' =", simplify(diff(f21, x)), "; f'<0 on:", solveset(diff(f21, x) < 0, x, S.Reals))

# 2.2 simplified form on its domain
g22 = -x**2 + x + 2
dom22 = Union(Interval.open(0, Rational(1, 9)), Interval.open(Rational(1, 9), oo))
r22 = function_range(g22, x, dom22)
show("2.2 range", r22, Interval(-oo, Rational(9, 4)))
print("[INFO] 2.2 increasing where g'>0:", solveset(diff(g22, x) > 0, x, S.Reals), "(intersect with domain)")

# 5.2 simplified polynomial on its domain
f52 = x**2 + x + 6
dom52 = Union(Interval.open(-1, 0), Interval.open(0, oo))
r52 = function_range(f52, x, dom52)
show("5.2 range", r52, Union(Interval.Ropen(Rational(23, 4), 6), Interval.open(6, oo)))

# 5.1 monotonicity of 1/|x-1| on each side (derivative of 1/(1-x) for x<1 and 1/(x-1) for x>1)
print("[INFO] 5.1 d/dx 1/(1-x) on x<1 =", simplify(diff(1/(1 - x), x)), "> 0 => increasing on (-inf,1)")
print("[INFO] 5.1 d/dx 1/(x-1) on x>1 =", simplify(diff(1/(x - 1), x)), "< 0 => decreasing on (1,inf)")

# 6.4 : log_3 + log_sqrt3 + log_{1/3} = 2 log_3
t = symbols('t', positive=True)
lhs = log(t, 3) + log(t, sqrt(3)) + log(t, Rational(1, 3))
print("[INFO] 6.4 simplified LHS:", simplify(lhs.rewrite(log)), " (expect 2*log(t)/log(3))")
print("[INFO] 6.4 solve 2*log_3(x+1)=6 ->", solveset(2*log(x + 1, 3) - 6, x, S.Reals))

# 6.2 real solutions
print("[INFO] 6.2 solveset ->", solveset(sqrt(x + 5) - (5 - sqrt(x + 10)), x, S.Reals))

print("ALL CHECKS PASSED" if all(results) else f"{results.count(False)} CHECK(S) DIFFER")
sys.exit(0 if all(results) else 1)
