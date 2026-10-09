"""Plots the sketches of problem set 02 (exercises 1, 3.1, 3.2, 7.3) for a visual check.

The PNG is written next to this script by default (it is git-ignored); pass another output
path as the first argument. Requires numpy and matplotlib.
"""
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Ex 1: f(x) = [x] and g(x) = x - [x]
ax = axes[0, 0]
x = np.linspace(-3, 3, 6000)
ax.plot(x, np.floor(x), lw=1.5, label="f=[x]")
ax.plot(x, x - np.floor(x), lw=1.5, label="g=x-[x]")
ax.set_title("1. f(x)=[x], g(x)=x-[x]")
ax.set_ylim(-3, 3)
ax.legend()
ax.grid(alpha=0.3)

# Ex 3.1: sin(arcsin x) on [-1,1] and arcsin(sin x)
ax = axes[0, 1]
x = np.linspace(-1, 1, 2000)
ax.plot(x, np.sin(np.arcsin(x)), lw=1.5, label="sin(arcsin x)")
x2 = np.linspace(-4 * np.pi, 4 * np.pi, 8000)
ax2 = axes[0, 2]
ax2.plot(x2, np.arcsin(np.sin(x2)), lw=1.5, label="arcsin(sin x)")
ax2.set_title("3.1  arcsin(sin x) (period 2pi)")
ax2.grid(alpha=0.3)
ax.set_title("3.1  sin(arcsin x) on [-1,1]")
ax.grid(alpha=0.3)

# Ex 3.2: sin(pi x) and cot(x)|sin x|
ax = axes[1, 0]
x = np.linspace(-4, 4, 8000)
ax.plot(x, np.sin(np.pi * x), lw=1.5)
ax.set_title("3.2  sin(pi x) (period 2)")
ax.grid(alpha=0.3)

ax = axes[1, 1]
x = np.linspace(-4 * np.pi, 4 * np.pi, 40000)
x = x[np.abs(np.sin(x)) > 1e-3]
ax.plot(x, np.cos(x) / np.sin(x) * np.abs(np.sin(x)), lw=1.2)
ax.set_ylim(-1.5, 1.5)
ax.set_title("3.2  cot(x)|sin x| (period pi)")
ax.grid(alpha=0.3)

# Ex 7.3: floor(2 sin x)
ax = axes[1, 2]
x = np.linspace(-4 * np.pi, 4 * np.pi, 20000)
ax.plot(x, np.floor(2 * np.sin(x)), lw=1.5)
T = 2 * np.pi
ax.axvline(T, ls="--", c="green", lw=1)
ax.set_title("7.3  [2 sin x] (period 2pi)")
ax.grid(alpha=0.3)

fig.tight_layout()
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots_set02.png")
fig.savefig(out, dpi=110)
print(f"written {out}")
