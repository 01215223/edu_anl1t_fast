import matplotlib.pyplot as plt
import numpy as np

# Przygotowanie siatki wykresów (4 wiersze, 3 kolumny)
fig, axs = plt.subplots(4, 3, figsize=(16, 16))
fig.suptitle(
    'Wykresy funkcji z zadań: Analiza 1 (ANL1T)',
    fontsize=16,
    fontweight='bold',
)

# 1. Ćw 2.1: f(x) = [x]
x_gen = np.linspace(-3, 3, 600)
y_floor = np.floor(x_gen)
axs[0, 0].plot(x_gen, y_floor, drawstyle='steps-pre', color='b', linewidth=2)
axs[0, 0].set_title('Ćw 2.1: f(x) = [x]')
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# 2. Ćw 2.1: g(x) = x - [x]
y_frac = x_gen - np.floor(x_gen)
axs[0, 1].plot(x_gen, y_frac, color='r', linewidth=2)
axs[0, 1].set_title('Ćw 2.1: g(x) = x - [x]')
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# 3. Ćw 2.3: f1(x) = sin(arcsin(x))
x_arc = np.linspace(-1, 1, 300)
y_sin_arcsin = np.sin(np.arcsin(x_arc))
axs[0, 2].plot(x_arc, y_sin_arcsin, color='g', linewidth=2)
axs[0, 2].set_title('Ćw 2.3: f1(x) = sin(arcsin(x))')
axs[0, 2].grid(True, linestyle='--', alpha=0.6)

# 4. Ćw 2.3: f2(x) = arcsin(sin(x))
x_trig = np.linspace(-2 * np.pi, 2 * np.pi, 800)
y_arcsin_sin = np.arcsin(np.sin(x_trig))
axs[1, 0].plot(x_trig, y_arcsin_sin, color='m', linewidth=2)
axs[1, 0].set_title('Ćw 2.3: f2(x) = arcsin(sin(x))')
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# 5. Ćw 2.3: f1(x) = sin(pi * x)
y_sin_pi = np.sin(np.pi * x_trig)
axs[1, 1].plot(x_trig, y_sin_pi, color='c', linewidth=2)
axs[1, 1].set_title('Ćw 2.3: f1(x) = sin(pi * x)')
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

# 6. Ćw 2.3: f2(x) = ctg(x) * |sin(x)|
with np.errstate(divide='ignore', invalid='ignore'):
  y_ctg = (1.0 / np.tan(x_trig)) * np.abs(np.sin(x_trig))
axs[1, 2].plot(x_trig, y_ctg, color='tab:orange', linewidth=2)
axs[1, 2].set_title('Ćw 2.3: f2(x) = ctg(x)*|sin(x)|')
axs[1, 2].set_ylim(-2, 2)
axs[1, 2].grid(True, linestyle='--', alpha=0.6)

# 7. Ćw 2.7: f1(x) = cos(arccos(x))
y_cos_arccos = np.cos(np.arccos(x_arc))
axs[2, 0].plot(x_arc, y_cos_arccos, color='brown', linewidth=2)
axs[2, 0].set_title('Ćw 2.7: f1(x) = cos(arccos(x))')
axs[2, 0].grid(True, linestyle='--', alpha=0.6)

# 8. Ćw 2.7: f2(x) = arccos(cos(x))
y_arccos_cos = np.arccos(np.cos(x_trig))
axs[2, 1].plot(x_trig, y_arccos_cos, color='purple', linewidth=2)
axs[2, 1].set_title('Ćw 2.7: f2(x) = arccos(cos(x))')
axs[2, 1].grid(True, linestyle='--', alpha=0.6)

# 9. Ćw 2.7: f1(x) = cos(x / pi)
y_cos_div_pi = np.cos(x_trig / np.pi)
axs[2, 2].plot(x_trig, y_cos_div_pi, color='olive', linewidth=2)
axs[2, 2].set_title('Ćw 2.7: f1(x) = cos(x / pi)')
axs[2, 2].grid(True, linestyle='--', alpha=0.6)

# 10. Ćw 2.7: f2(x) = (sin(x) + cos(x))^2
y_sin_cos_sq = (np.sin(x_trig) + np.cos(x_trig)) ** 2
axs[3, 0].plot(x_trig, y_sin_cos_sq, color='deeppink', linewidth=2)
axs[3, 0].set_title('Ćw 2.7: f2(x) = (sin(x)+cos(x))^2')
axs[3, 0].grid(True, linestyle='--', alpha=0.6)

# 11. Ćw 2.7: f(x) = [2 * sin(x)]
y_floor_sin = np.floor(2 * np.sin(x_trig))
axs[3, 1].plot(x_trig, y_floor_sin, drawstyle='steps-pre', color='k', linewidth=2)
axs[3, 1].set_title('Ćw 2.7: f(x) = [2 * sin(x)]')
axs[3, 1].grid(True, linestyle='--', alpha=0.6)

# Ukrycie ostatniego pustego pola w siatce
axs[3, 2].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
