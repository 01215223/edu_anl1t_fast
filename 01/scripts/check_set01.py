"""Numeric check of problem set 01, exercises 2-6.

Every check evaluates the ORIGINAL expression (with its domain restrictions: an undefined
value counts as "not a solution / not in the domain") and compares it with the claimed answer,
which is the answer given in 01/problem-set-01-solution.md. Requires mpmath.
Exits with status 1 if a check fails.
"""
import random
import sys

import mpmath as mp

mp.mp.dps = 50
random.seed(7)
results = []


def R(p, q=1):
    return mp.mpf(p) / mp.mpf(q)


def logb(b, x):
    return mp.log(x) / mp.log(b)


def check(name, ok, detail=""):
    results.append(ok)
    print(f"[{'OK' if ok else 'FAIL'}] {name} {detail}")


def grid(lo, hi, n=1500):
    return [lo + (hi - lo) * R(k, n) for k in range(n + 1)]


SPECIAL = [R(-7), R(-3), R(-2), R(-1), R(-1, 3), R(-1, 2), R(-1, 4), R(0), R(1, 9), R(1, 2),
           R(1), R(2), R(3), R(8, 9), R(8), R(10), R(12), R(15), R(26), R(-4), R(5), R(9, 4),
           R(170, 81), R(6), R(23, 4), R(1, 10), R(1, 4)]

# ---------------------------------------------------------------- Exercise 2.1
def f21(x):
    if x == 2 or x == -2:
        return None
    return (x**2 - 3*x + 2) / (4 - x**2)


pts = grid(R(-12), R(12)) + SPECIAL
ok = True
for x in pts:
    v = f21(x)
    if v is None:
        continue
    if abs(v - (-1 + 3/(x + 2))) > mp.mpf(10)**-35:
        ok = False
check("2.1 simplification f = -1 + 3/(x+2) on D_f", ok)

ok = True
for lo, hi in [(R(-12), R(-2)), (R(-2), R(2)), (R(2), R(12))]:
    xs = sorted(random.uniform(float(lo), float(hi)) for _ in range(400))
    xs = [mp.mpf(t) for t in xs]
    for a, b in zip(xs, xs[1:]):
        if not (f21(b) < f21(a)):
            ok = False
check("2.1 strictly decreasing on (-inf,-2), (-2,2), (2,inf)", ok)

# range: y is attained iff the unique candidate x = 3/(y+1) - 2 lies in D_f
ok = True
for y in grid(R(-10), R(10), 800) + [R(-1), R(-1, 4)]:
    if y == -1:
        attained = False
    else:
        x = 3/(y + 1) - 2
        v = f21(x) if (x != 2 and x != -2) else None
        attained = v is not None and abs(v - y) < mp.mpf(10)**-35
    claimed = not (y == -1 or y == R(-1, 4))
    if attained != claimed:
        ok = False
check("2.1 R_f = R \\ {-1, -1/4}", ok)
check("2.1 values f(0)=1/2, f(1)=0", f21(R(0)) == R(1, 2) and f21(R(1)) == 0)
check("2.1 limit at hole x->2 equals -1/4", abs(f21(R(2) + R(1, 10**20)) - R(-1, 4)) < R(1, 10**15))

# ---------------------------------------------------------------- Exercise 2.2
SQRT2_LOG_HALF = mp.log(R(1, 2)) / mp.log(mp.sqrt(2))  # log_{sqrt2}(1/2)


def f22_orig(x):
    if x <= 0:
        return None
    den = logb(3, 9*x)
    if den == 0:
        return None
    return (SQRT2_LOG_HALF - logb(3, x)) / den * (x**2 - x - 2)


def g22(x):
    return -x**2 + x + 2


check("2.2 log_{sqrt2}(1/2) = -2", abs(SQRT2_LOG_HALF + 2) < mp.mpf(10)**-40)

ok = True
for x in grid(R(0), R(12), 1500) + SPECIAL:
    v = f22_orig(x)
    inDf = x > 0 and x != R(1, 9)
    if inDf != (v is not None):
        ok = False
    if v is not None and abs(v - g22(x)) > mp.mpf(10)**-35:
        ok = False
check("2.2 original = -x^2+x+2 exactly on D_f=(0,1/9)U(1/9,inf); undefined elsewhere", ok)

ok = True
for lo, hi, inc in [(R(0), R(1, 9), True), (R(1, 9), R(1, 2), True), (R(1, 2), R(12), False)]:
    xs = [lo + (hi - lo) * mp.mpf(random.random()) for _ in range(300)]
    xs = sorted(x for x in xs if x > 0)
    for a, b in zip(xs, xs[1:]):
        if inc and not (f22_orig(b) > f22_orig(a)):
            ok = False
        if (not inc) and not (f22_orig(b) < f22_orig(a)):
            ok = False
check("2.2 increasing on (0,1/9) and (1/9,1/2), decreasing on (1/2,inf)", ok)

ok = True
for y in grid(R(-10), R(4), 700) + [R(9, 4), R(170, 81), R(2)]:
    disc = 9 - 4*y
    attained = False
    if disc >= 0:
        s = mp.sqrt(disc)
        for x in [(1 + s)/2, (1 - s)/2]:
            v = f22_orig(x)
            if v is not None and abs(v - y) < mp.mpf(10)**-30:
                attained = True
    claimed = y <= R(9, 4)
    if attained != claimed:
        ok = False
check("2.2 R_f = (-inf, 9/4]", ok)
check("2.2 g(8/9) = 170/81 (hole value attained at 8/9 in D_f)", abs(g22(R(8, 9)) - R(170, 81)) == 0)
check("2.2 max value 9/4 at x=1/2", g22(R(1, 2)) == R(9, 4))

# ---------------------------------------------------------------- Exercise 3.1
ok = True
claimed = lambda x: (x < -3) or (1 < x < 2) or (x > 2)  # noqa: E731
for x in grid(R(-8), R(8), 1600) + SPECIAL:
    val = (1 - x)*(2 - x)**2*(x + 3)**3
    if (val < 0) != claimed(x):
        ok = False
check("3.1 (1-x)(2-x)^2(x+3)^3 < 0  <=>  x in (-inf,-3) U (1,2) U (2,inf)", ok)

# ---------------------------------------------------------------- Exercise 3.2
ok = True
claimed = lambda x: (x <= -3) or (x > 1)  # noqa: E731
for x in grid(R(-8), R(8), 1600) + SPECIAL:
    if x == 1 or x == -1:
        in_set = False  # undefined
    else:
        den = (x**2 - 1)*(x + 1)
        if den == 0:
            in_set = False
        else:
            in_set = (x + 3)**3 / den >= 0
    if in_set != claimed(x):
        ok = False
check("3.2 (x+3)^3/((x^2-1)(x+1)) >= 0  <=>  x in (-inf,-3] U (1,inf)", ok)

# ---------------------------------------------------------------- Exercise 3.3
def F33(x):
    return 3*mp.log(x + 1) - mp.log(1 - x**2)


xs = [-1 + R(k, 3000) * 2 for k in range(1, 3000)]  # inside (-1,1)
sign_changes = []
prev = None
for x in xs:
    if abs(x) < 1e-30:
        continue
    s = mp.sign(F33(x))
    if prev is not None and s != prev[1]:
        sign_changes.append(x)
    prev = (x, s)
check("3.3 unique root of 3log(x+1)-log(1-x^2) in (-1,1) is x=0 (sign change only there)",
      len(sign_changes) == 1 and abs(sign_changes[0]) < R(1, 1000),
      f"sign changes near {[mp.nstr(s, 4) for s in sign_changes]}")
check("3.3 x=0 solves the equation", abs(F33(R(0))) < 1e-40)
check("3.3 polynomial (x+1)^3-(1-x^2) = x(x+1)(x+3)",
      all(abs(((x + 1)**3 - (1 - x**2)) - x*(x + 1)*(x + 3)) < 1e-40 for x in SPECIAL))

# ---------------------------------------------------------------- Exercise 3.4
def L34(x):
    if x <= 0 or x == 2:
        return None
    return (x**2 - x) / (logb(2, x) - 1)


ok = True
for x in grid(R(-2), R(6), 1600) + SPECIAL:
    v = L34(x)
    in_set = v is not None and v <= 0
    if in_set != (1 <= x < 2):
        ok = False
check("3.4 (x^2-x)/(log2 x - 1) <= 0  <=>  x in [1,2)", ok)

# ---------------------------------------------------------------- Exercise 3.5
ok = True
for x in grid(R(-3), R(3), 1200) + SPECIAL:
    lhs = mp.mpf(2)**(abs(x) - 1)
    rhs = (R(1, 2))**abs(x)
    if (lhs <= rhs) != (R(-1, 2) <= x <= R(1, 2)):
        ok = False
check("3.5 2^{|x|-1} <= (1/2)^{|x|}  <=>  x in [-1/2,1/2]", ok)

# ---------------------------------------------------------------- Exercise 4
def f4(t):  # original function, defined for t in D_f = (0,1)U(1,inf)
    if not (t > 0 and t != 1):
        raise ValueError("outside D_f")
    return (1 + 2*t)/(t - t**2) + mp.sin(1/t + mp.sqrt(t))


def in_Df(t):
    return t > 0 and t != 1


# literal substitution vs. closed forms, random points in claimed domains
def rnd(a, b):
    return mp.mpf(random.uniform(float(a), float(b)))


cases4 = {
    "f(-x)": (lambda x: f4(-x),
              lambda x: (2*x - 1)/(x**2 + x) + mp.sin(-1/x + mp.sqrt(-x)),
              [(R(-30), R(-1) - R(1, 10**4)), (R(-1) + R(1, 10**4), R(-10, 10**4))]),
    "f(1/x)": (lambda x: f4(1/x),
               lambda x: x*(x + 2)/(x - 1) + mp.sin(x + 1/mp.sqrt(x)),
               [(R(1, 10**4), R(1) - R(1, 10**4)), (R(1) + R(1, 10**4), R(30))]),
    "f(sqrt x)": (lambda x: f4(mp.sqrt(x)),
                  lambda x: (1 + 2*mp.sqrt(x))/(mp.sqrt(x) - x) + mp.sin(x**(-R(1, 2)) + x**R(1, 4)),
                  [(R(1, 10**4), R(1) - R(1, 10**4)), (R(1) + R(1, 10**4), R(30))]),
    "f(x^2)": (lambda x: f4(x**2),
               lambda x: (1 + 2*x**2)/(x**2 - x**4) + mp.sin(1/x**2 + abs(x)),
               [(R(-30), R(-1) - R(1, 10**4)), (R(-1) + R(1, 10**4), R(-1, 10**4)),
                (R(1, 10**4), R(1) - R(1, 10**4)), (R(1) + R(1, 10**4), R(30))]),
}
for name, (literal, closed, ivs) in cases4.items():
    worst = mp.mpf(0)
    for _ in range(1500):
        lo, hi = random.choice(ivs)
        x = rnd(lo, hi)
        worst = max(worst, abs(literal(x) - closed(x)) / max(1, abs(literal(x))))
    check(f"4 {name} closed form equals literal substitution", worst < mp.mpf(10)**-35,
          f"(max rel diff {mp.nstr(worst, 3)})")

# domains: f(t(x)) defined iff t(x) in D_f
dom4 = {
    "f(-x)": (lambda x: -x, lambda x: (x < -1) or (-1 < x < 0)),
    "f(1/x)": (lambda x: (1/x) if x != 0 else None, lambda x: (0 < x < 1) or (x > 1)),
    "f(sqrt x)": (lambda x: mp.sqrt(x) if x >= 0 else None, lambda x: (0 < x < 1) or (x > 1)),
    "f(x^2)": (lambda x: x**2, lambda x: x not in (-1, 0, 1)),
}
for name, (inner, claim) in dom4.items():
    ok = True
    for x in grid(R(-4), R(4), 1200) + SPECIAL:
        t = inner(x)
        defined = t is not None and in_Df(t)
        if defined != claim(x):
            ok = False
    check(f"4 domain {name}", ok)

# simplified rational parts
check("4 simplification (2x-1)/(x^2+x) equals (1-2x)/(-x-x^2)",
      all(abs((2*x - 1)/(x**2 + x) - (1 - 2*x)/(-x - x**2)) < 1e-40 for x in SPECIAL if x not in (0, -1)))
check("4 simplification x(x+2)/(x-1) equals (1+2/x)/(1/x-1/x^2)",
      all(abs(x*(x + 2)/(x - 1) - (1 + 2/x)/(1/x - 1/x**2)) < 1e-40 for x in SPECIAL if x not in (0, 1)))
check("4 simplification (1+2s)/(s-s^2) with s=sqrt x equals (1+2sqrt x)/(sqrt x - x)",
      all(abs((1 + 2*mp.sqrt(x))/(mp.sqrt(x) - x) - (1 + 2*mp.sqrt(x))/(mp.sqrt(x)*(1 - mp.sqrt(x)))) < 1e-40
          for x in SPECIAL if x > 0 and x != 1))

# ---------------------------------------------------------------- Exercise 5.1
def f51(x):
    d = x**2 - 2*x + 1
    if d <= 0:
        return None
    return 1/mp.sqrt(d)


ok = True
for x in grid(R(-10), R(10), 1500) + SPECIAL:
    v = f51(x)
    if x == 1:
        if v is not None:
            ok = False
    elif v is None or abs(v - 1/abs(x - 1)) > mp.mpf(10)**-35:
        ok = False
check("5.1 f(x) = 1/|x-1| on D_f = R \\ {1}", ok)

ok = True
for lo, hi, inc in [(R(-10), R(1), True), (R(1), R(10), False)]:
    xs = sorted(rnd(lo, hi - R(1, 10**6)) for _ in range(400))
    for a, b in zip(xs, xs[1:]):
        if inc and not (f51(b) > f51(a)):
            ok = False
        if (not inc) and not (f51(b) < f51(a)):
            ok = False
check("5.1 increasing on (-inf,1), decreasing on (1,inf)", ok)
check("5.1 f(0)=1 < f(1/2)=2 (so NOT decreasing on (-inf,1))", f51(R(0)) == 1 and f51(R(1, 2)) == 2)

ok = True
for y in grid(R(-3), R(10), 600):
    attained = y > 0 and any(
        (x != 1 and f51(x) is not None and abs(f51(x) - y) < mp.mpf(10)**-30)
        for x in [1 + 1/y, 1 - 1/y])
    if attained != (y > 0):
        ok = False
check("5.1 R_f = (0,inf)", ok)

# ---------------------------------------------------------------- Exercise 5.2
def f52(x):
    if x <= -1 or x == 0:
        return None
    den = 2*logb(5, x + 1)
    if den == 0:
        return None
    return (x**2 + x + 6)/den * logb(5, x**2 + 2*x + 1)


ok = True
for x in grid(R(-3), R(12), 1500) + SPECIAL:
    v = f52(x)
    inDf = (x > -1) and (x != 0)
    if inDf != (v is not None):
        ok = False
    if v is not None and abs(v - (x**2 + x + 6)) > mp.mpf(10)**-30:
        ok = False
check("5.2 D_f = (-1,0)U(0,inf) and f(x) = x^2+x+6 there", ok)

ok = True
for lo, hi, inc in [(R(-1), R(-1, 2), False), (R(-1, 2), R(0), True), (R(0), R(10), True)]:
    xs = sorted(rnd(lo + R(1, 10**6), hi - R(1, 10**6)) for _ in range(300))
    for a, b in zip(xs, xs[1:]):
        if inc and not (f52(b) > f52(a)):
            ok = False
        if (not inc) and not (f52(b) < f52(a)):
            ok = False
check("5.2 decreasing on (-1,-1/2), increasing on (-1/2,0) and on (0,inf)", ok)

ok = True
for y in grid(R(5), R(12), 700) + [R(23, 4), R(6)]:
    disc = 4*y - 23
    attained = False
    if disc >= 0:
        s = mp.sqrt(disc)
        for x in [(-1 + s)/2, (-1 - s)/2]:
            v = f52(x)
            if v is not None and abs(v - y) < mp.mpf(10)**-30:
                attained = True
    claimed = (R(23, 4) <= y < 6) or (y > 6)
    if attained != claimed:
        ok = False
check("5.2 R_f = [23/4,6) U (6,inf)", ok)

# ---------------------------------------------------------------- Exercise 6.1
def ineq61(x):
    if x < -4:
        return None
    return mp.sqrt(x + 4) > x - 8


ok = True
for x in grid(R(-10), R(20), 1500) + SPECIAL:
    v = ineq61(x)
    if v is None:
        if x >= -4:
            ok = False
        continue
    if v != (-4 <= x < 12):
        ok = False
check("6.1 sqrt(x+4) > x-8  <=>  x in [-4,12)", ok)

# ---------------------------------------------------------------- Exercise 6.2
def h62(x):
    return mp.sqrt(x + 5) - (5 - mp.sqrt(x + 10))


root62 = mp.findroot(h62, (R(-5) + R(1, 10**6), R(15)), solver='bisect' if False else 'anderson')
check("6.2 unique root x=-1 of sqrt(x+5) = 5 - sqrt(x+10)",
      abs(h62(R(-1))) < 1e-40 and abs(root62 + 1) < mp.mpf(10)**-25,
      f"(numeric root {mp.nstr(root62, 12)})")
ok = all(h62(x) < 0 for x in grid(R(-5), R(-1), 200)[:-1]) and all(h62(x) > 0 for x in grid(R(-1) + R(1, 1000), R(15), 200))
check("6.2 h changes sign only at -1 on [-5,15] (monotone increasing)", ok)

# ---------------------------------------------------------------- Exercise 6.3
def ineq63(x):
    if x == 1 or x == 2:
        return None
    return (1 - x)**-1 * (2 - x)**-2 * (x - 3)


ok = True
for x in grid(R(-4), R(8), 1600) + SPECIAL:
    v = ineq63(x)
    in_set = v is not None and v >= 0
    if in_set != ((1 < x < 2) or (2 < x <= 3)):
        ok = False
check("6.3 (1-x)^-1 (2-x)^-2 (x-3) >= 0  <=>  x in (1,2) U (2,3]", ok,
      "(x=2 excluded: expression undefined there)")
check("6.3 value at x=2 is undefined (so 2 must NOT be in the answer)", ineq63(R(2)) is None)

# ---------------------------------------------------------------- Exercise 6.4
def F64(x):
    return logb(3, x + 1) + logb(mp.sqrt(3), x + 1) + logb(R(1, 3), x + 1) - 6


check("6.4 LHS equals 2*log_3(x+1) (identity)",
      all(abs(logb(3, x + 1) + logb(mp.sqrt(3), x + 1) + logb(R(1, 3), x + 1) - 2*logb(3, x + 1)) < 1e-40
          for x in grid(R(-1) + R(1, 1000), R(40), 200)))
check("6.4 x=26 solves the equation", abs(F64(R(26))) < 1e-40)

# ---------------------------------------------------------------- Exercise 6.5 (log = log10)
def ineq65(x):
    if x <= 0:
        return None
    return (mp.log10(x) - 1)*(mp.log10(x) - 10)*(x + 2) <= 0


ok = True
for k in range(0, 3000):
    u = R(-6) + R(18, 3000) * k  # x = 10^u
    x = mp.mpf(10)**u
    v = ineq65(x)
    if v != (1 <= u <= 10):
        ok = False
for x in [R(10), mp.mpf(10)**10, mp.mpf(10)**R(11, 2)]:
    pass
check("6.5 (log x-1)(log x-10)(x+2) <= 0  <=>  x in [10, 10^10]  (grid in log scale)", ok)
check("6.5 boundary: x=10 and x=10^10 are solutions",
      ineq65(mp.mpf(10)) is True and ineq65(mp.mpf(10)**10) is True)

# ---------------------------------------------------------------- Exercise 6.6
def ineq66(x):
    if x <= 0 or x == 1:
        return None
    return (logb(2, x) - 1)/(x**2 - x) <= 0


ok = True
for x in grid(R(0), R(6), 1600) + SPECIAL:
    v = ineq66(x)
    in_set = bool(v)
    if in_set != (1 < x <= 2):
        if not (x <= 0 or x == 1):
            ok = False
check("6.6 (log2 x - 1)/(x^2-x) <= 0  <=>  x in (1,2]", ok)

# ---------------------------------------------------------------- Exercise 6.7
def ineq67(x):
    return mp.mpf(2)**(2*abs(x + 2)) - 4*mp.mpf(2)**(1 - x) < 0


ok = True
for x in grid(R(-10), R(5), 1500) + SPECIAL:
    if ineq67(x) != (R(-7) < x < R(-1, 3)):
        ok = False
check("6.7 (2^|x+2|)^2 - 4*2^(1-x) < 0  <=>  x in (-7,-1/3)", ok)
check("6.7 boundaries -7 and -1/3 give equality", abs(mp.mpf(2)**(2*abs(R(-7) + 2)) - 4*mp.mpf(2)**(1 - R(-7))) < 1e-30
      and abs(mp.mpf(2)**(2*abs(R(-1, 3) + 2)) - 4*mp.mpf(2)**(1 - R(-1, 3))) < 1e-30)

print()
print("ALL CHECKS PASSED" if all(results) else f"FAILURES: {results.count(False)}")
sys.exit(0 if all(results) else 1)
