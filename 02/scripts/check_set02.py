"""Numeric checks of problem set 02 (exercises 2-8).

Every check compares the claimed answer from 02/problem-set-02-solution.md with the
ORIGINAL expression evaluated at high precision (mpmath), or tests a property
(periodicity, parity, monotonicity) on a sample grid. Checks are numeric, not proofs.
Requires mpmath. Exits with status 1 if a check fails.
"""
import sys

import mpmath as mp

mp.mp.dps = 50
results = []


def check(name, ok, detail=""):
    results.append(bool(ok))
    print(f"[{'OK' if ok else 'FAIL'}] {name} {detail}")


def close(a, b, eps=mp.mpf("1e-30")):
    return abs(a - b) < eps


def pi():
    return mp.pi


def floor_(x):
    return mp.floor(x)


def is_period(f, T, xs):
    """True if f(x+T) == f(x) for all sample points x (where both are defined)."""
    for x in xs:
        try:
            a, b = f(x + T), f(x)
        except (ValueError, ZeroDivisionError):
            continue
        if not close(a, b, mp.mpf("1e-25")):
            return False
    return True


GRID = [mp.mpf(k) / 37 + mp.mpf("0.0123") for k in range(-400, 401)]

# ---------------- Exercise 1: floor and fractional part ----------------
f1 = floor_
g1 = lambda x: x - floor_(x)
pts = [mp.mpf(k) / 13 for k in range(-130, 131)]
check("ex1 floor: [x] <= x < [x]+1",
      all(floor_(x) <= x < floor_(x) + 1 for x in pts))
check("ex1 g(x)=x-[x] takes values in [0,1)",
      all(0 <= g1(x) < 1 for x in pts))
check("ex1 g is 1-periodic", is_period(g1, 1, pts))
check("ex1 [x+1] = [x]+1 (f is not periodic, it grows by 1)",
      all(close(f1(x + 1), f1(x) + 1) for x in pts))

# ---------------- Exercise 2: inverse trig of trig values ----------------
v21 = mp.acos(mp.sin(mp.mpf(32) / 5 * pi()))
check("ex2.1 arccos(sin(32pi/5)) = pi/10", close(v21, pi() / 10), f"value={v21}")
v22 = mp.asin(mp.cos(-mp.mpf(7) / 11 * pi()))
check("ex2.2 arcsin(cos(-7pi/11)) = -3pi/22", close(v22, -3 * pi() / 22), f"value={v22}")

# ---------------- Exercise 3: periodicity ----------------
xs = [mp.mpf(k) / 17 + mp.mpf("0.031") for k in range(-300, 301)]
f31 = lambda x: mp.sin(mp.asin(x)) if -1 <= x <= 1 else None
check("ex3.1 sin(arcsin x) = x on [-1,1] (bounded domain, so not periodic)",
      all(close(mp.sin(mp.asin(mp.mpf(k) / 50)), mp.mpf(k) / 50) for k in range(-50, 51)))
f32 = lambda x: mp.asin(mp.sin(x))
check("ex3.1 arcsin(sin x) has period 2pi",
      is_period(f32, 2 * pi(), xs))
check("ex3.1 arcsin(sin x) does not have period pi",
      not is_period(f32, pi(), xs))
check("ex3.1 arcsin(sin x) does not have period pi/2",
      not is_period(f32, pi() / 2, xs))
f33 = lambda x: mp.sin(pi() * x)
check("ex3.2 sin(pi x) has period 2", is_period(f33, 2, xs))
check("ex3.2 sin(pi x) does not have period 1", not is_period(f33, 1, xs))
f34 = lambda x: mp.cot(x) * abs(mp.sin(x)) if mp.sin(x) != 0 else None
check("ex3.2 cot(x)|sin x| has period pi", is_period(f34, pi(), xs))
check("ex3.2 cot(x)|sin x| does not have period pi/2", not is_period(f34, pi() / 2, xs))
# Closed form on (0,pi): cot x * sin x = cos x ; on (pi,2pi): -cos x
check("ex3.2 cot(x)|sin x| = cos x on (0,pi) and -cos x on (pi,2pi)",
      all(close(f34(x), mp.cos(x)) for x in xs if 0 < x < pi())
      and all(close(f34(x), -mp.cos(x)) for x in xs if pi() < x < 2 * pi()))

# ---------------- Exercise 4: parity ----------------
f41 = lambda x: x * (mp.power(2, x) - mp.power(2, -x))
check("ex4.1 f(-x)=f(x) (even)", all(close(f41(-x), f41(x)) for x in GRID))
f42 = lambda x: mp.log(x + mp.sqrt(x * x + 1), 2)
check("ex4.2 f(-x)=-f(x) (odd)", all(close(f42(-x), -f42(x)) for x in GRID))

# ---------------- Exercise 5 and 8: monotonicity of sequences ----------------
a51 = lambda n: n * n - 8 * n + 7
d51 = [a51(n + 1) - a51(n) for n in range(1, 200)]
check("ex5.1 a_{n+1}-a_n = 2n-7 (checked on n=1..199)",
      all(d51[n - 1] == 2 * n - 7 for n in range(1, 200)))
check("ex5.1 a_{n+1} > a_n for all n >= 4",
      all(a51(n + 1) > a51(n) for n in range(4, 2000)))
check("ex5.1 a_{n+1} < a_n for n = 1,2,3 (decreasing at start), not for n=4",
      all(a51(n + 1) < a51(n) for n in (1, 2, 3)) and not a51(5) < a51(4))
a52 = lambda n: -2 / (n + 3 * mp.atan(n))
check("ex5.2 denominator n+3arctan n > 0 for n>=1",
      all(n + 3 * mp.atan(n) > 0 for n in range(1, 5000)))
check("ex5.2 a_n strictly increasing for n >= 1",
      all(a52(n + 1) > a52(n) for n in range(1, 5000)))

a81 = lambda n: mp.log(2 * n + mp.power(3, n), 2)
check("ex8.1 a_n = log2(2n+3^n) strictly increasing for n >= 1",
      all(a81(n + 1) > a81(n) for n in range(1, 2000)))
a82 = lambda n: mp.cos(mp.pi * n / 2)
vals82 = [a82(n) for n in range(1, 13)]
check("ex8.2 a_n = cos(pi n/2) values n=1..8 are 0,-1,0,1,0,-1,0,1",
      all(close(vals82[k], [0, -1, 0, 1][k % 4]) for k in range(8)))
check("ex8.2 both signs of differences occur in every tail (not monotone for any n0)",
      all(any(a82(n + 1) - a82(n) < -0.5 for n in range(n0, n0 + 4)) and
          any(a82(n + 1) - a82(n) > 0.5 for n in range(n0, n0 + 4))
          for n0 in range(1, 200)))
a83 = lambda n: mp.sin(10 * pi() / (n + 1))
check("ex8.3 a_{n+1} < a_n for all n >= 19",
      all(a83(n + 1) < a83(n) for n in range(19, 5000)))
check("ex8.3 a_19 > a_18 (so n0 cannot be below 19)",
      a83(19) > a83(18))

# ---------------- Exercise 6 (homework) ----------------
check("ex6.1 arccos(sin(11/7)) = (22-7pi)/14",
      close(mp.acos(mp.sin(mp.mpf(11) / 7)), (22 - 7 * pi()) / 14), f"value={mp.acos(mp.sin(mp.mpf(11)/7))}")
check("ex6.2 arccos(sin(3pi/5)) = pi/10",
      close(mp.acos(mp.sin(3 * pi() / 5)), pi() / 10))
check("ex6.3 arcsin(cos(-5/11)) = (11pi-10)/22",
      close(mp.asin(mp.cos(-mp.mpf(5) / 11)), (11 * pi() - 10) / 22))
check("ex6.4 arcsin(cos(-3pi/5)) = -pi/10",
      close(mp.asin(mp.cos(-3 * pi() / 5)), -pi() / 10))

# ---------------- Exercise 7: periodicity ----------------
f71 = lambda x: mp.cos(mp.acos(x))
check("ex7.1 cos(arccos x) = x on [-1,1]",
      all(close(f71(mp.mpf(k) / 50), mp.mpf(k) / 50) for k in range(-50, 51)))
f72 = lambda x: mp.acos(mp.cos(x))
check("ex7.1 arccos(cos x) has period 2pi", is_period(f72, 2 * pi(), xs))
check("ex7.1 arccos(cos x) does not have period pi", not is_period(f72, pi(), xs))
check("ex7.1 arccos(cos x) does not have period pi/2", not is_period(f72, pi() / 2, xs))
f73 = lambda x: mp.cos(x / pi())
check("ex7.2 cos(x/pi) has period 2pi^2", is_period(f73, 2 * pi() ** 2, xs))
check("ex7.2 cos(x/pi) does not have period pi^2", not is_period(f73, pi() ** 2, xs))
f74 = lambda x: (mp.sin(x) + mp.cos(x)) ** 2
check("ex7.2 (sin x+cos x)^2 = 1+sin 2x", all(close(f74(x), 1 + mp.sin(2 * x)) for x in xs))
check("ex7.2 (sin x+cos x)^2 has period pi", is_period(f74, pi(), xs))
check("ex7.2 (sin x+cos x)^2 does not have period pi/2", not is_period(f74, pi() / 2, xs))
f75 = lambda x: floor_(2 * mp.sin(x))
xs75 = [mp.mpf(k) / 101 for k in range(-700, 701)]
check("ex7.3 floor(2 sin x) has period 2pi", is_period(f75, 2 * pi(), xs75))
check("ex7.3 floor(2 sin x) does not have period pi", not is_period(f75, pi(), xs75))
# sin x = +-1 is not hit by the grid, so add the points x = pi/2 + k*pi explicitly
xs75_all = xs75 + [pi() / 2, 3 * pi() / 2, -pi() / 2]
check("ex7.3 floor(2 sin x) takes values -2,-1,0,1,2",
      {int(f75(x)) for x in xs75_all} == {-2, -1, 0, 1, 2})

print()
passed = sum(results)
print(f"{passed}/{len(results)} checks passed")
sys.exit(0 if passed == len(results) else 1)
