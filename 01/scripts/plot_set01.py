"""Plots the graphs of the sketch exercises 2.1, 2.2, 5.1 and 5.2 of problem set 01.

Used to check the sketch descriptions in 01/problem-set-01-solution.md. The PNG is written next to
this script by default (it is git-ignored); pass another output path as the first argument.
Requires numpy and matplotlib.
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(11, 9))

# 2.1  f(x) = (x^2-3x+2)/(4-x^2) on R\{-2,2}
ax = axes[0, 0]
x = np.linspace(-8, 8, 40000)
x = x[(np.abs(x + 2) > 1e-3) & (np.abs(x - 2) > 1e-3)]
y = (x**2 - 3*x + 2) / (4 - x**2)
ax.plot(x, y, lw=1.2)
ax.plot([1, 0], [0, 0.5], "ko", ms=4)
ax.plot([2], [-0.25], "o", mfc="white", mec="red", ms=8)
ax.axhline(-1, ls="--", c="gray", lw=0.8)
ax.axvline(-2, ls="--", c="gray", lw=0.8)
ax.set_ylim(-8, 8); ax.set_xlim(-8, 8)
ax.set_title("2.1  f(x)=(x^2-3x+2)/(4-x^2)")
ax.grid(alpha=0.3)

# 2.2  f(x) = -x^2+x+2 on (0,1/9) U (1/9,inf)  (plotted on the domain only)
ax = axes[0, 1]
x1 = np.linspace(1e-4, 1/9 - 1e-4, 2000)
x2 = np.linspace(1/9 + 1e-4, 4, 4000)
ax.plot(x1, -x1**2 + x1 + 2, lw=1.2, c="C0")
ax.plot(x2, -x2**2 + x2 + 2, lw=1.2, c="C0")
ax.plot([1/9], [170/81], "o", mfc="white", mec="red", ms=8)
ax.plot([0], [2], "o", mfc="white", mec="C0", ms=7)
ax.plot([2], [0], "ko", ms=4)
ax.plot([0.5], [2.25], "k^", ms=5)
ax.set_ylim(-6, 3); ax.set_xlim(-0.2, 4)
ax.set_title("2.2  f(x)=-x^2+x+2 on D_f")
ax.grid(alpha=0.3)

# 5.1  f(x) = 1/|x-1|
ax = axes[1, 0]
x = np.linspace(-4, 6, 40000)
x = x[np.abs(x - 1) > 1e-3]
ax.plot(x, 1/np.abs(x - 1), lw=1.2)
ax.axvline(1, ls="--", c="gray", lw=0.8)
ax.axhline(0, ls="--", c="gray", lw=0.8)
ax.set_ylim(0, 6); ax.set_xlim(-4, 6)
ax.set_title("5.1  f(x)=1/|x-1|")
ax.grid(alpha=0.3)

# 5.2  f(x) = x^2+x+6 on (-1,0) U (0,inf)
ax = axes[1, 1]
x1 = np.linspace(-1 + 1e-4, -1e-4, 2000)
x2 = np.linspace(1e-4, 4, 2000)
ax.plot(x1, x1**2 + x1 + 6, lw=1.2, c="C0")
ax.plot(x2, x2**2 + x2 + 6, lw=1.2, c="C0")
ax.plot([-1, 0], [6, 6], "o", mfc="white", mec="red", ms=8)
ax.plot([-0.5], [23/4], "k^", ms=5)
ax.set_ylim(4, 20); ax.set_xlim(-1.5, 4)
ax.set_title("5.2  f(x)=x^2+x+6 on D_f")
ax.grid(alpha=0.3)

fig.tight_layout()
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots_set01.png")
fig.savefig(out, dpi=80)
print("saved", out)
