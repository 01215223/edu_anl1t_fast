# Zadanie 1 — rozwiązanie

Zestaw: [`problem-set-01.md`](problem-set-01.md), zadanie 1 (`prob-01-ex-01`).

Dana jest funkcja

$$
f(x) = x^x + \log_x\left(1 + 2\sqrt{x} + 3x^2\right).
$$

Należy wyznaczyć $f(-x)$, $f\left(\frac1x\right)$, $f(\sqrt{x})$ oraz $f(x^2)$.

## Idea

Każde z tych wyrażeń to $f(t)$, gdzie $t$ jest pewnym wyrażeniem zależnym od $x$. Wystarczy w definicji $f$ w każdym miejscu, w którym stoi $x$, wpisać $t$.

Wyrażenie $f(t)$ ma sens dokładnie wtedy, gdy $t$ należy do dziedziny $D_f$, czyli gdy $t>0$ i $t\neq 1$.

## Dziedzina funkcji $f$

- $x^x$ (potęga o wykładniku zmiennym) wymaga $x>0$,
- $\log_x(\dots)$ wymaga $x>0$ i $x\neq 1$,
- $\sqrt{x}$ wymaga $x\ge 0$,
- liczba logarytmowana $1+2\sqrt{x}+3x^2$ jest dodatnia dla $x\ge 0$ (jedynka i składniki nieujemne).

Zatem

$$
D_f=(0,1)\cup(1,\infty).
$$

## 1. $f(-x)$

Podstawiamy $t=-x$:

$$
f(-x)=(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3(-x)^2\right)=(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3x^2\right).
$$

Warunki:

- $-x>0 \iff x<0$,
- $-x\neq 1 \iff x\neq -1$.

Pierwiastek $\sqrt{-x}$ wymaga $-x\ge 0$, co już wynika z $x<0$.

$$
D_{f(-x)}=(-\infty,-1)\cup(-1,0)
$$

## 2. $f\left(\frac1x\right)$

Podstawiamy $t=\frac1x$. Dla $x>0$ mamy $\sqrt{\frac1x}=\frac{1}{\sqrt{x}}$ oraz $\left(\frac1x\right)^2=\frac{1}{x^2}$:

$$
f\left(\frac1x\right)=\left(\frac1x\right)^{\frac1x}+\log_{\frac1x}\left(1+\frac{2}{\sqrt{x}}+\frac{3}{x^2}\right).
$$

Warunki:

- $\frac1x>0 \iff x>0$,
- $\frac1x\neq 1 \iff x\neq 1$.

$$
D_{f(1/x)}=(0,1)\cup(1,\infty)
$$

Uproszczenie: $\left(\frac1x\right)^{\frac1x}=x^{-\frac1x}$ oraz $\log_{\frac1x}b=-\log_x b$, więc

$$
f\left(\frac1x\right)=x^{-\frac1x}-\log_x\left(1+\frac{2}{\sqrt{x}}+\frac{3}{x^2}\right).
$$

## 3. $f(\sqrt{x})$

Podstawiamy $t=\sqrt{x}$. Wtedy $\sqrt{t}=\sqrt{\sqrt{x}}=x^{\frac14}$ oraz $t^2=x$:

$$
f(\sqrt{x})=(\sqrt{x})^{\sqrt{x}}+\log_{\sqrt{x}}\left(1+2x^{\frac14}+3x\right).
$$

Warunki:

- $\sqrt{x}>0 \iff x>0$,
- $\sqrt{x}\neq 1 \iff x\neq 1$.

$$
D_{f(\sqrt{x})}=(0,1)\cup(1,\infty)
$$

Uproszczenie: $(\sqrt{x})^{\sqrt{x}}=e^{\sqrt{x}\cdot\frac12\ln x}=x^{\frac{\sqrt{x}}{2}}$.

## 4. $f(x^2)$

Podstawiamy $t=x^2$. Wtedy $\sqrt{t}=\sqrt{x^2}=|x|$ oraz $t^2=x^4$:

$$
f(x^2)=(x^2)^{x^2}+\log_{x^2}\left(1+2|x|+3x^4\right).
$$

Warunki:

- $x^2>0 \iff x\neq 0$,
- $x^2\neq 1 \iff x\neq -1$ i $x\neq 1$.

$$
D_{f(x^2)}=\mathbb{R}\setminus\{-1,0,1\}
$$

Uproszczenie: $(x^2)^{x^2}=|x|^{2x^2}$ dla $x\neq 0$.

## Podsumowanie

| Wyrażenie | Wzór | Dziedzina |
|---|---|---|
| $f(-x)$ | $(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3x^2\right)$ | $(-\infty,-1)\cup(-1,0)$ |
| $f\left(\frac1x\right)$ | $\left(\frac1x\right)^{\frac1x}+\log_{\frac1x}\left(1+\frac{2}{\sqrt{x}}+\frac{3}{x^2}\right)$ | $(0,1)\cup(1,\infty)$ |
| $f(\sqrt{x})$ | $(\sqrt{x})^{\sqrt{x}}+\log_{\sqrt{x}}\left(1+2x^{\frac14}+3x\right)$ | $(0,1)\cup(1,\infty)$ |
| $f(x^2)$ | $(x^2)^{x^2}+\log_{x^2}\left(1+2\lvert x\rvert+3x^4\right)$ | $\mathbb{R}\setminus\{-1,0,1\}$ |
