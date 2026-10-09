"""Numeric checks of problem set 03 (sequences: 03a, functions: 03b).

Each claimed limit from 03a/problem-set-03-a-solution.md and 03b/problem-set-03-b-solution.md is
compared with the ORIGINAL expression evaluated at high precision (mpmath) for large n or for
x close to the point. This supports the claimed values but is not a proof.
Requires mpmath. Exits with status 1 if a check fails.
"""
import sys

import mpmath as mp

mp.mp.dps = 80
results = []


def check(name, ok, detail=""):
    results.append(bool(ok))
    print(f"[{'OK' if ok else 'FAIL'}] {name} {detail}")


def mpf(x):
    return mp.mpf(x)


def seq_limit(name, a, expected, big=(mpf(10) ** 6, mpf(10) ** 9), tol=mpf("1e-5")):
    """Checks a_n -> expected (finite) or a_n -> +inf (expected == mp.inf)."""
    v1, v2 = a(big[0]), a(big[1])
    if expected == mp.inf:
        ok = v1 > 10**4 and v2 > v1
        check(name, ok, f"a(1e6)={mp.nstr(v1, 8)} a(1e9)={mp.nstr(v2, 8)} -> +inf")
    else:
        ok = abs(v2 - expected) < tol
        check(name, ok, f"a(1e9)={mp.nstr(v2, 10)} expected {mp.nstr(expected, 10)}")


def fun_limit(name, f, x0, expected, side=0, tol=mpf("1e-5")):
    """Checks lim f(x) = expected as x -> x0 (side: +1 right, -1 left, 0 two-sided, not used at infinity)."""
    vals = []
    for k in (7, 14):
        h = mpf(10) ** (-k)
        if side == 0:
            cands = [x0 + h, x0 - h]
        else:
            cands = [x0 + side * h]
        vals.append([f(x) for x in cands])
    worst = max(abs(v - expected) for v in vals[1])  # smallest step only
    ok = worst < tol
    check(name, ok, f"max error at h=1e-14: {mp.nstr(max(abs(v - expected) for v in vals[1]), 3)}")


def fun_limit_inf(name, f, sign, expected, tol=mpf("1e-5")):
    """Checks lim f(x) = expected as x -> sign*infinity."""
    xs = [sign * mpf(10) ** k for k in (8, 12)]
    vals = [f(x) for x in xs]
    ok = abs(vals[1] - expected) < tol if expected != mp.inf else vals[1] > 1e6
    check(name, ok, f"f(x={mp.nstr(xs[1], 3)})={mp.nstr(vals[1], 10)} expected {mp.nstr(expected, 10) if expected != mp.inf else '+inf'}")


print("== 03a: sequences (zajęcia) ==")
seq_limit("03a 1.1 5n^2 - n arctan n -> +inf", lambda n: 5 * n**2 - n * mp.atan(n), mp.inf)
seq_limit("03a 1.2 (n+1/n)^8 / C(n+2,n)^5 * (1+...+n) -> 16",
          lambda n: (n + 1 / n) ** 8 / mp.binomial(n + 2, n) ** 5 * n * (n + 1) / 2, mpf(16))
seq_limit("03a 1.3 (2^n+3^n)/(4^n+3^n) -> 0", lambda n: (2**n + 3**n) / (4**n + 3**n), mpf(0))
seq_limit("03a 1.4 (4^n+2^n)/(2^(2n+1)+4^(n+1)+3^n) -> 1/6",
          lambda n: (4**n + 2**n) / (2 ** (2 * n + 1) + 4 ** (n + 1) + 3**n), mpf(1) / 6)
seq_limit("03a 1.5 sqrt(n^2+5n) - sqrt(n^2-n) -> 3",
          lambda n: mp.sqrt(n**2 + 5 * n) - mp.sqrt(n**2 - n), mpf(3))
seq_limit("03a 1.6 (sqrt(n^2+5)-n)/(sqrt(n^2+2)-n) -> 5/2",
          lambda n: (mp.sqrt(n**2 + 5) - n) / (mp.sqrt(n**2 + 2) - n), mpf(5) / 2)

print("== 03a: sequences (zajęcia, assumptions) ==")
with mp.workdps(600):
    bound_ok = all(abs(mp.cos(mp.factorial(n)) / (n + mp.asin(mpf(1) / n))) <= mpf(1) / n for n in range(1, 201))
check("03a 2.1 |cos(n!)/(n+arcsin(1/n))| <= 1/n for n = 1..200 (squeeze to 0)", bound_ok)
seq_limit("03a 2.2 n-th root of (4^n + n^13 3^n) -> 4",
          lambda n: mp.power(4**n + n**13 * 3**n, 1 / n), mpf(4))
seq_limit("03a 2.3 (n+2022)/(3n-(-1)^n) -> 1/3",
          lambda n: (n + 2022) / (3 * n - (-1) ** int(n)), mpf(1) / 3)
seq_limit("03a 2.4 (n+2)/(n+1))^n-root-part + ((n+1)/n)^2022 -> e+1",
          lambda n: ((n + 2) / (n + 1)) ** n + ((n + 1) / n) ** 2022, mp.e + 1)
seq_limit("03a 2.5 ((1-n^2)/(5-2n))^(n+1) (2/(n+1))^(n+1) -> e^(3/2)",
          lambda n: ((1 - n**2) / (5 - 2 * n)) ** (n + 1) * (2 / (n + 1)) ** (n + 1), mp.exp(mpf(3) / 2))
seq_limit("03a 2.6 ((2n^2+2n+1)/(2n^2+2))^(n+1) -> e",
          lambda n: ((2 * n**2 + 2 * n + 1) / (2 * n**2 + 2)) ** (n + 1), mp.e)

print("== 03a: sequences (domowe) ==")
seq_limit("03a 3.1 (3n^3 - sqrt(n^3+4n^6)) / (sqrt(n)-5n+383764)^3 -> -1/125",
          lambda n: (3 * n**3 - mp.sqrt(n**3 + 4 * n**6)) / (mp.sqrt(n) - 5 * n + 383764) ** 3, mpf(-1) / 125)
seq_limit("03a 3.2 sqrt(4n^2+n) - 2n -> 1/4", lambda n: mp.sqrt(4 * n**2 + n) - 2 * n, mpf(1) / 4)
seq_limit("03a 3.3 n(sqrt(2n^2+1)-sqrt(2n^2-1)) -> 1/sqrt(2)",
          lambda n: n * (mp.sqrt(2 * n**2 + 1) - mp.sqrt(2 * n**2 - 1)), 1 / mp.sqrt(2))
seq_limit("03a 3.4 (3^(n+1)+2^n)/(5^n+4*3^n) -> 0",
          lambda n: (3 ** (n + 1) + 2**n) / (5**n + 4 * 3**n), mpf(0))
seq_limit("03a 3.5 (4^n+5^n)/(3*4^n+2^n) -> +inf", lambda n: (4**n + 5**n) / (3 * 4**n + 2**n), mp.inf)
seq_limit("03a 3.6 (3^(n-1)+(-2)^n)/(3^(n+1)+(-2)^(n+2)) -> 1/9",
          lambda n: (3 ** (n - 1) + (-2) ** n) / (3 ** (n + 1) + (-2) ** (n + 2)), mpf(1) / 9)
seq_limit("03a 3.7 (2^(3n)+5^(n+1))/(3^(2n+1)+4^(n-1)) -> 0",
          lambda n: (2 ** (3 * n) + 5 ** (n + 1)) / (3 ** (2 * n + 1) + 4 ** (n - 1)), mpf(0))
seq_limit("03a 3.8 geometric sums ratio -> 4/3",
          lambda n: sum(mpf(1) / 2**k for k in range(0, int(n) + 1)) / sum(mpf(1) / 3**k for k in range(0, int(n) + 1)),
          mpf(4) / 3, big=(mpf(60), mpf(120)))
check("03a 4.1 same as 2.1: bound |cos(n!)/(n+arcsin(1/n))| <= 1/n for n = 1..200",
      bound_ok)
seq_limit("03a 4.2 (3n^2-1)/(5n^2+cos n) -> 3/5", lambda n: (3 * n**2 - 1) / (5 * n**2 + mp.cos(n)), mpf(3) / 5)
seq_limit("03a 4.3 (3n^2 - n(-1)^n)/(sqrt(n)-5)^4 -> 3",
          lambda n: (3 * n**2 - n * (-1) ** int(n)) / (mp.sqrt(n) - 5) ** 4, mpf(3),
          big=(mpf(10) ** 12, mpf(10) ** 16), tol=mpf("1e-3"))
seq_limit("03a 4.4 n-th root of (4^n/n^12 + n 3^n + 5n^3) -> 4",
          lambda n: mp.power(4**n / n**12 + n * 3**n + 5 * n**3, 1 / n), mpf(4))
seq_limit("03a 4.5 (7^n/n^13 + n)^(1/n) -> 7",
          lambda n: mp.power(7**n / n**13 + n, 1 / n), mpf(7))
seq_limit("03a 4.6 ((n+1)/n)^2019 -> 1", lambda n: ((n + 1) / n) ** 2019, mpf(1))
seq_limit("03a 4.7 ((2^n+4^n)/(2^(2n)-2^n))^(2^n) -> e^2",
          lambda n: ((2**n + 4**n) / (2 ** (2 * n) - 2**n)) ** (2**n), mp.exp(2), big=(mpf(50), mpf(60)))
seq_limit("03a 4.8 ((3n)/(4n+1))^n * ((4n-3)/(3n+2))^n -> e^(-5/3)",
          lambda n: ((3 * n) / (4 * n + 1)) ** n * ((4 * n - 3) / (3 * n + 2)) ** n, mp.exp(mpf(-5) / 3))
seq_limit("03a 4.9 n(ln(n+3)-ln n) -> 3", lambda n: n * (mp.log(n + 3) - mp.log(n)), mpf(3))

print("== 03a: sequences (examples for indeterminate forms) ==")
ex_1inf = [(lambda n: mpf(1) ** n, mpf(1)), (lambda n: (1 + 1 / n) ** n, mp.e),
           (lambda n: (1 + 1 / n) ** (n**2), mp.inf), (lambda n: (1 - 1 / n) ** (n**2), mpf(0))]
for i, (a, L) in enumerate(ex_1inf):
    seq_limit(f"03a 5 example 1^inf #{i + 1}", a, L, big=(mpf(10) ** 3, mpf(10) ** 4), tol=mpf("1e-2"))
ex_00 = [(lambda n: (1 / n) / (1 / n), mpf(1)), (lambda n: (1 / n**2) / (1 / n), mpf(0)),
         (lambda n: (1 / n) / (1 / n**2), mp.inf), (lambda n: ((-1) ** int(n) / n) / (1 / n), None)]
for i, (a, L) in enumerate(ex_00[:3]):
    seq_limit(f"03a 5 example 0/0 #{i + 1}", a, L)
check("03a 5 example 0/0 #4 oscillates (values +1, -1)",
      abs(ex_00[3][0](mpf(10) ** 6) - 1) < 1e-9 and abs(ex_00[3][0](mpf(10) ** 6 + 1) + 1) < 1e-9)
ex_inf0 = [(lambda n: mp.exp(n**2) ** (1 / n), mp.inf), (lambda n: mp.exp(n**2) ** (1 / n**2), mp.e),
           (lambda n: mp.exp(n**2) ** (-1 / n), mpf(0)), (lambda n: mpf(n) ** (1 / n), mpf(1))]
for i, (a, L) in enumerate(ex_inf0):
    seq_limit(f"03a 5 example inf^0 #{i + 1}", a, L, big=(mpf(10) ** 2, mpf(10) ** 3), tol=mpf("1e-2"))
ex_infinf = [(lambda n: n / n, mpf(1)), (lambda n: n**2 / n, mp.inf), (lambda n: n / n**2, mpf(0))]
for i, (a, L) in enumerate(ex_infinf):
    seq_limit(f"03a 5 example inf/inf #{i + 1}", a, L)
check("03a 5 example inf/inf #4 oscillates (values +1, -1)",
      abs(((-1) ** 10**6) * mpf(10) ** 6 / mpf(10) ** 6 - 1) < 1e-9
      and abs(((-1) ** (10**6 + 1)) * mpf(10) ** 6 / mpf(10) ** 6 + 1) < 1e-9)

print("== 03b: functions (zajęcia) ==")
fun_limit("03b 1.1 (x^3-3x^2+3x-1)/(x^3-x^2-x+1) -> 0 at 1",
          lambda x: (x**3 - 3 * x**2 + 3 * x - 1) / (x**3 - x**2 - x + 1), mpf(1), mpf(0))
fun_limit("03b 1.2 (x - sqrt x)/(x + sqrt x) -> -1 at 0+",
          lambda x: (x - mp.sqrt(x)) / (x + mp.sqrt(x)), mpf(0), mpf(-1), side=1)
fun_limit("03b 1.3 tan 3x / sin 7x -> 3/7 at 0",
          lambda x: mp.tan(3 * x) / mp.sin(7 * x), mpf(0), mpf(3) / 7)
fun_limit("03b 1.4 sin(x^2-1)/(x+1) -> -2 at -1",
          lambda x: mp.sin(x**2 - 1) / (x + 1), mpf(-1), mpf(-2))
fun_limit("03b 1.5 ((x+1)/(2x))^(3/(x-1)) -> e^(-3/2) at 1+",
          lambda x: ((x + 1) / (2 * x)) ** (3 / (x - 1)), mpf(1), mp.exp(mpf(-3) / 2), side=1)
fun_limit_inf("03b 1.6 3x+1+sqrt(9x^2-2) -> 1 at -inf",
              lambda x: 3 * x + 1 + mp.sqrt(9 * x**2 - 2), -1, mpf(1))

print("== 03b: functions (zajęcia, assumptions) ==")
f_2 = lambda x: (1 - mp.sin(x)) ** (1 / x)
fun_limit("03b 2 (1-sin x)^(1/x) -> 1/e at 0+", f_2, mpf(0), mp.exp(-1), side=1)
fun_limit("03b 2 (1-sin x)^(1/x) -> 1/e at 0-", f_2, mpf(0), mp.exp(-1), side=-1)
fun_limit("03b 3.1 (1+|x|)^(1/x) -> e at 0+", lambda x: (1 + abs(x)) ** (1 / x), mpf(0), mp.e, side=1)
fun_limit("03b 3.1 (1+|x|)^(1/x) -> 1/e at 0-", lambda x: (1 + abs(x)) ** (1 / x), mpf(0), mp.exp(-1), side=-1)
check("03b 3.2 sin 3x takes value 0 at x_k=-2pi k/3 and 1 at x_k=pi/6-2pi k/3 (k=10^6)",
      abs(mp.sin(3 * (-2 * mp.pi * 10**6 / 3))) < 1e-40
      and abs(mp.sin(3 * (mp.pi / 6 - 2 * mp.pi * 10**6 / 3)) - 1) < 1e-40)

print("== 03b: functions (domowe) ==")
fun_limit("03b 4.1 tan 2x / x -> 2 at 0", lambda x: mp.tan(2 * x) / x, mpf(0), mpf(2))
fun_limit("03b 4.2 (1-cos 6x)/x^2 -> 18 at 0", lambda x: (1 - mp.cos(6 * x)) / x**2, mpf(0), mpf(18))
fun_limit("03b 4.3 cos x / cos 7x -> -1/7 at pi/2", lambda x: mp.cos(x) / mp.cos(7 * x), mp.pi / 2, mpf(-1) / 7)
fun_limit("03b 4.4 arctan(3x)/(7x) -> 3/7 at 0", lambda x: mp.atan(3 * x) / (7 * x), mpf(0), mpf(3) / 7)
fun_limit("03b 4.5 sin 7x / (4 - sqrt(5x+16)) -> -56/5 at 0",
          lambda x: mp.sin(7 * x) / (4 - mp.sqrt(5 * x + 16)), mpf(0), mpf(-56) / 5)
fun_limit("03b 4.6 (sqrt(x sqrt x) - 8)/(x^(1/4) - 2) -> 12 at 16",
          lambda x: (mp.sqrt(x * mp.sqrt(x)) - 8) / (mp.power(x, mpf(1) / 4) - 2), mpf(16), mpf(12))
fun_limit("03b 4.7 (sqrt(x^2+4)-2)/(sqrt(x^2+9)-3) -> 3/2 at 0",
          lambda x: (mp.sqrt(x**2 + 4) - 2) / (mp.sqrt(x**2 + 9) - 3), mpf(0), mpf(3) / 2)
fun_limit("03b 4.8 ((3-x^2)/(x+1))^(1/(x-1)) -> e^(-3/2) at 1+",
          lambda x: ((3 - x**2) / (x + 1)) ** (1 / (x - 1)), mpf(1), mp.exp(mpf(-3) / 2), side=1)
fun_limit("03b 4.9 (cos x)^(cot^2 x) -> e^(-1/2) at 0",
          lambda x: mp.cos(x) ** (mp.cot(x) ** 2), mpf(0), mp.exp(mpf(-1) / 2))
fun_limit_inf("03b 4.10 sqrt(e^x+1)-sqrt(e^x-1) -> 0 at +inf",
              lambda x: mp.sqrt(mp.exp(x) + 1) - mp.sqrt(mp.exp(x) - 1), 1, mpf(0))
fun_limit_inf("03b 4.11 sqrt(2x^2+x+1)/x -> -sqrt2 at -inf",
              lambda x: mp.sqrt(2 * x**2 + x + 1) / x, -1, -mp.sqrt(2))
fun_limit_inf("03b 4.12 sqrt((x+3)(x-4)) + x -> 1/2 at -inf",
              lambda x: mp.sqrt((x + 3) * (x - 4)) + x, -1, mpf(1) / 2)
fun_limit_inf("03b 4.13 (sqrt(2-x)-sqrt(1-x))/(x+sqrt(x^2+2x+3)) -> 0 at -inf",
              lambda x: (mp.sqrt(2 - x) - mp.sqrt(1 - x)) / (x + mp.sqrt(x**2 + 2 * x + 3)), -1, mpf(0))
fun_limit_inf("03b 4.14 x arctan(1/x) -> 1 at +inf", lambda x: x * mp.atan(1 / x), 1, mpf(1))

print("== 03b: functions (no limit) ==")
check("03b 5.1 cos(2/x) equals 1 at x=1/(pi k) and 0 at x=4/(pi(1+4k)) (k=10^6)",
      abs(mp.cos(2 / (1 / (mp.pi * 10**6))) - 1) < 1e-30
      and abs(mp.cos(2 / (4 / (mp.pi * (1 + 4 * 10**6))))) < 1e-30)
check("03b 5.2 2^(1/(x-1)): right side large, left side small (x = 1 +- 1e-6)",
      2 ** (1 / (mpf(10) ** -6)) > 10**100 and 2 ** (1 / (-mpf(10) ** -6)) < mpf(10) ** -100)
check("03b 5.3 sin(arctan(1/x)) = sgn(x)/sqrt(1+x^2): values +1 and -1 near 0",
      abs(mp.sin(mp.atan(1 / mpf(10) ** -6)) - 1) < 1e-9
      and abs(mp.sin(mp.atan(1 / (-mpf(10) ** -6))) + 1) < 1e-9)
check("03b 3.1 sign-check: (1+|x|)^(1/x) differs on both sides (e != 1/e)",
      abs(mp.e - mp.exp(-1)) > 1)

print("== 03b: identities (domowe 6) ==")
xs = [mpf(k) / 7 - mpf(2) for k in range(0, 29)]
ch = mp.cosh
sh = mp.sinh
check("03b 6.1 ch^2 - sh^2 = 1", all(abs(ch(x) ** 2 - sh(x) ** 2 - 1) < 1e-60 for x in xs))
check("03b 6.2 ch^2 + sh^2 = ch 2x", all(abs(ch(x) ** 2 + sh(x) ** 2 - ch(2 * x)) < 1e-60 for x in xs))
check("03b 6.3 sh 2x = 2 sh x ch x", all(abs(sh(2 * x) - 2 * sh(x) * ch(x)) < 1e-60 for x in xs))
check("03b 6.4 ch^2 = 1/(1 - th^2)", all(abs(ch(x) ** 2 - 1 / (1 - mp.tanh(x) ** 2)) < 1e-50 for x in xs))

print()
passed = sum(results)
print(f"{passed}/{len(results)} checks passed")
sys.exit(0 if passed == len(results) else 1)
