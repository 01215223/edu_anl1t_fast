import matplotlib.pyplot as plt
import numpy as np

# Konfiguracja siatki wykresów
fig, axs = plt.subplots(3, 2, figsize=(12, 14))
fig.suptitle(
    'Poprawione wykresy funkcji bez błędów numerycznych',
    fontsize=14,
    fontweight='bold',
)

x = np.linspace(-3 * np.pi, 3 * np.pi, 3000)

# 1. Ćw 2.1: f(x) = [x] (zastosowanie stylu 'step' zamiast ciągłej linii)
x_floor = np.linspace(-4, 4, 800)
y_floor = np.floor(x_floor)
axs[0, 0].step(x_floor, y_floor, where='post', color='blue', linewidth=2)
axs[0, 0].set_title('Ćw 2.1: f(x) = [x] (funkcja podłoga)')
axs[0, 0].set_ylim(-5, 5)
axs[0, 0].grid(True, linestyle='--', alpha=0.6)

# 2. Ćw 2.1: g(x) = x - [x] (maskowanie NaN na skokach, aby uniknąć pionowych kresek)
x_frac_plot, y_frac_plot = [], []
for val in np.linspace(-4, 4, 3000):
  frac = val - np.floor(val)
  if np.isclose(frac, 0.0, atol=1e-3) and val != -4:
    x_frac_plot.append(np.nan)
    y_frac_plot.append(np.nan)
  x_frac_plot.append(val)
  y_frac_plot.append(frac)

axs[0, 1].plot(x_frac_plot, y_frac_plot, color='red', linewidth=2)
axs[0, 1].set_title('Ćw 2.1: g(x) = x - [x] (część ułamkowa)')
axs[0, 1].set_ylim(-0.2, 1.2)
axs[0, 1].grid(True, linestyle='--', alpha=0.6)

# 3. Ćw 2.3: f2(x) = ctg(x) * |sin(x)|
# Używamy przekształcenia do cos(x) * sign(sin(x)) i maskujemy asymptoty
y_ctg_fixed = np.cos(x) * np.sign(np.sin(x))
y_ctg_fixed[np.isclose(np.sin(x), 0, atol=1e-2)] = (
    np.nan
)  # usunięcie pionowych kresek
axs[1, 0].plot(x, y_ctg_fixed, color='tab:orange', linewidth=2)
axs[1, 0].set_title('Ćw 2.3: f2(x) = ctg(x) * |sin(x)| (bez asymptot)')
axs[1, 0].set_ylim(-1.5, 1.5)
axs[1, 0].grid(True, linestyle='--', alpha=0.6)

# 4. Ćw 2.7: f2(x) = arccos(cos(x))
y_arccos_cos = np.arccos(np.cos(x))
axs[1, 1].plot(x, y_arccos_cos, color='purple', linewidth=2)
axs[1, 1].set_title('Ćw 2.7: f2(x) = arccos(cos(x))')
axs[1, 1].grid(True, linestyle='--', alpha=0.6)

# 5. Ćw 2.7: f2(x) = (sin(x) + cos(x))^2  [tożsamościowo równe 1 + sin(2x)]
y_trig_sq = (np.sin(x) + np.cos(x)) ** 2
axs[2, 0].plot(x, y_trig_sq, color='deeppink', linewidth=2)
axs[2, 0].set_title('Ćw 2.7: f2(x) = (sin(x) + cos(x))^2')
axs[2, 0].grid(True, linestyle='--', alpha=0.6)

# 6. Ćw 2.7: f(x) = [2 * sin(x)]
y_floor_sin = np.floor(2 * np.sin(x))
axs[2, 1].step(x, y_floor_sin, where='mid', color='black', linewidth=2)
axs[2, 1].set_title('Ćw 2.7: f(x) = [2 * sin(x)]')
axs[2, 1].set_ylim(-3, 3)
axs[2, 1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()