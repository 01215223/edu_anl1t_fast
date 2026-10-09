# Granica funkcji — rozwiązania (zestaw 03b)

Zestaw zadań: [`problem-set-03-b.md`](problem-set-03-b.md) — zadania 1–6 (zadania 1–3 na zajęcia, 4–6 domowe).

Skrypt sprawdzający liczbowo wszystkie granice: [`../03a/scripts/check_set03.py`](../03a/scripts/check_set03.py) (opis w [`../03a/scripts/README.md`](../03a/scripts/README.md)). Skrypt nie jest częścią rozwiązania.

**Oznaczenia.** Funkcje hiperboliczne z zadania 6 zapisujemy jako $\cosh$, $\sinh$, $\tanh$ (w treści zadania: ch, sh, th).

**Narzędzia, z których korzystamy** (żadnej reguły de l'Hospitala):

- Granice podstawowe: $\dfrac{\sin t}{t}\to1$ i $\dfrac{\tan t}{t}\to1$ przy $t\to0$; $\dfrac{\ln(1+t)}{t}\to1$ przy $t\to0$; $\left(1+t\right)^{1/t}\to e$ przy $t\to0$.
- Jeśli $\dfrac{1-\cos t}{t^2}\to\dfrac12$ przy $t\to0$ (z $1-\cos t=2\sin^2\frac t2$).
- Twierdzenie o trzech funkcjach (ściskanie), granica iloczynu, sumy i ilorazu.
- **Lemat C.** Jeśli $c(x)\to0$, $c(x)\neq0$ i $d(x) c(x)\to L$, to $\left(1+c(x)\right)^{d(x)}\to e^{L}$. (Dowód jak w zadaniu 2.5 z zestawu 03a: $\exp\left(d(x)c(x)\cdot\frac{\ln(1+c(x))}{c(x)}\right)$.)

---

## Zadanie 1 (na zajęcia)

### 1.1. $\lim_{x\to1}\dfrac{x^3-3x^2+3x-1}{x^3-x^2-x+1}$

Licznik to $(x-1)^3$ (wzór skróconego mnożenia). Mianownik rozkładamy przez grupowanie: $x^3-x^2-x+1=x^2(x-1)-(x-1)=(x-1)(x^2-1)=(x-1)^2(x+1)$.

Dla $x\neq1$:

$$
\frac{(x-1)^3}{(x-1)^2(x+1)}=\frac{x-1}{x+1}\ \to\ \frac{0}{2}=0.
$$

**Wynik:** $0$.

### 1.2. $\lim_{x\to0^+}\dfrac{x-\sqrt x}{x+\sqrt x}$

Dla $x\gt 0$ dzielimy licznik i mianownik przez $\sqrt x$:

$$
\frac{x-\sqrt x}{x+\sqrt x}=\frac{\sqrt x-1}{\sqrt x+1}.
$$
Gdy $x\to0^+$, to $\sqrt x\to0^+$ (funkcja $\sqrt{\cdot}$ jest ciągła w $0$), więc wyrażenie zbiega do $\dfrac{0-1}{0+1}=-1$.

**Wynik:** $-1$.

### 1.3. $\lim_{x\to0}\dfrac{\tan3x}{\sin7x}$

Zapisujemy $\tan3x=\dfrac{\sin3x}{\cos3x}$ i dzielimy przez $3x$ oraz $7x$:

$$
\frac{\tan3x}{\sin7x}=\frac{\sin3x}{3x}\cdot\frac{7x}{\sin7x}\cdot\frac{3}{7}\cdot\frac{1}{\cos3x}.
$$
Gdy $x\to0$, czynniki $\dfrac{\sin3x}{3x}\to1$, $\dfrac{7x}{\sin7x}\to1$, $\dfrac1{\cos3x}\to1$. Granica równa się $\dfrac37$.

**Wynik:** $\dfrac37$.

### 1.4. $\lim_{x\to-1}\dfrac{\sin(x^2-1)}{x+1}$

Zauważamy, że $x^2-1=(x-1)(x+1)$. Dla $x\neq-1$ oznaczmy $u=x^2-1\neq0$ (dla $x$ bliskich $-1$ jest $x\neq\pm1$). Wtedy

$$
\frac{\sin(x^2-1)}{x+1}=\frac{\sin u}{u}\cdot\frac{u}{x+1}=\frac{\sin u}{u}\cdot(x-1).
$$
Gdy $x\to-1$, to $u\to0$, więc $\dfrac{\sin u}{u}\to1$, a $x-1\to-2$. Granica równa się $-2$.

**Wynik:** $-2$.

### 1.5. $\lim_{x\to1^+}\left(\dfrac{x+1}{2x}\right)^{\frac{3}{x-1}}$

Podstawa:

$$
\frac{x+1}{2x}=1+\frac{1-x}{2x}=1+c(x),  c(x)=\frac{1-x}{2x}\to0.
$$
Wykładnik i iloczyn:

$$
d(x) c(x)=\frac{3}{x-1}\cdot\frac{1-x}{2x}=-\frac{3}{2x}\ \to\ -\frac32.
$$
Z lematu C granica równa się $e^{-3/2}$. (Dla $x\gt 1$ mamy $c(x)\neq0$, więc lemat stosuje się bez zastrzeżeń.)

**Wynik:** $e^{-3/2}$.

### 1.6. $\lim_{x\to-\infty}\left(3x+1+\sqrt{9x^2-2}\right)$

Wyrażenie $3x+\sqrt{9x^2-2}$ daje postać $-\infty+\infty$, więc mnożymy przez sprzężenie:

$$
\left(3x+\sqrt{9x^2-2}\right)\left(\sqrt{9x^2-2}-3x\right)=9x^2-2-9x^2=-2.
$$
Stąd dla $x$ takich, że $\sqrt{9x^2-2}-3x\neq0$:

$$
3x+\sqrt{9x^2-2}=\frac{-2}{\sqrt{9x^2-2}-3x}.
$$
Dla $x\lt 0$ mamy $\sqrt{9x^2-2}=|x|\sqrt{9-\frac{2}{x^2}}=-x\sqrt{9-\frac{2}{x^2}}$, więc

$$
\sqrt{9x^2-2}-3x=-x\sqrt{9-\frac2{x^2}}-3x=-x\left(\sqrt{9-\frac2{x^2}}+3\right)\ \to\ +\infty,
$$
bo $-x\to+\infty$, a nawias zbiega do $6$. Zatem $\dfrac{-2}{\sqrt{9x^2-2}-3x}\to0$ i

$$
\lim_{x\to-\infty}\left(3x+1+\sqrt{9x^2-2}\right)=0+1=1.
$$

**Wynik:** $1$.

---

## Zadanie 2 (na zajęcia)

Funkcja $f(x)=(1-\sin x)^{1/x}$ jest określona dla $1-\sin x\gt 0$, czyli dla $\sin x\neq1$, a więc w sąsiedztwie $0$ (obie strony) jest dobrze określona. Przedstawiamy ją jako

$$
f(x)=\exp\left(\frac{\ln(1-\sin x)}{x}\right).
$$
Zajmiemy się wykładnikiem $g(x)=\dfrac{\ln(1-\sin x)}{x}$. Zapisujemy

$$
g(x)=\frac{\ln(1-\sin x)}{-\sin x}\cdot\frac{-\sin x}{x}.
$$

- Gdy $x\to0$, to $s=\sin x\to0$, $s\neq0$ dla $x\neq0$ bliskich zeru, więc z granicy $\dfrac{\ln(1+u)}{u}\to1$ (przy $u=-s\to0$) pierwszy czynnik zbiega do $1$.
- Drugi czynnik: $\dfrac{-\sin x}{x}\to-1$.

Zatem $g(x)\to-1$ (z obu stron), a z ciągłości $\exp$:

$$
\lim_{x\to0}(1-\sin x)^{1/x}=e^{-1}
$$

(granice prawostronna i lewostronna są równe).

*Odpowiedź na pytanie:* **tak**, granica $\lim_{x\to0}(1-\sin x)^{1/x}$ istnieje i wynosi $\dfrac1e$.

*Uwaga.* Dla $x\to0^+$ podstawa $1-\sin x$ jest mniejsza od $1$, a dla $x\to0^-$ większa od $1$. Mimo to obie granice jednostronne są równe $\frac1e$, bo wykładnik $\frac{\ln(1-\sin x)}{x}$ zbiega do $-1$ z obu stron.

**Wynik:**

- $\lim_{x\to0^+}(1-\sin x)^{1/x}=\frac1e$,
- $\lim_{x\to0^-}(1-\sin x)^{1/x}=\frac1e$,
- granica dwustronna istnieje i równa się $\dfrac1e$.

---

## Zadanie 3 (na zajęcia)

### 3.1. $\lim_{x\to0}(1+|x|)^{1/x}$ nie istnieje

Granica dwustronna istnieje tylko wtedy, gdy obie granice jednostronne są równe.

- **Prawostronna:** dla $x\gt 0$ mamy $|x|=x$, więc $(1+x)^{1/x}\to e$ (granica podstawowa).
- **Lewostronna:** dla $x\lt 0$ podstawiamy $t=-x\gt 0$. Wtedy $|x|=t$, $\frac1x=-\frac1t$, więc

$$
(1+|x|)^{1/x}=(1+t)^{-1/t}=\frac{1}{(1+t)^{1/t}}\ \to\ \frac1e.
$$

Ponieważ $e\neq\frac1e$, granica dwustronna nie istnieje.

### 3.2. $\lim_{x\to-\infty}\sin3x$ nie istnieje

Wskażemy dwa ciągi $x_k\to-\infty$ z różnymi granicami wartości funkcji (kryterium Heinego).

- $x_k=-\dfrac{2\pi k}{3}$: wtedy $\sin3x_k=\sin(-2\pi k)=0$ dla każdego $k$.
- $x_k=\dfrac{\pi}{6}-\dfrac{2\pi k}{3}$: wtedy $3x_k=\dfrac\pi2-2\pi k$, więc $\sin3x_k=\sin\dfrac\pi2=1$ dla każdego $k$.

Oba ciągi zbiegają do $-\infty$ (dla $k\to\infty$), a wartości funkcji są różne ($0$ i $1$). Zatem granica nie istnieje.

---

## Zadanie 4 (domowe)

### 4.1. $\lim_{x\to0}\dfrac{\tan2x}{x}$

$$
\frac{\tan2x}{x}=\frac{\tan2x}{2x}\cdot2\ \to\ 1\cdot2=2.
$$

**Wynik:** $2$.

### 4.2. $\lim_{x\to0}\dfrac{1-\cos6x}{x^2}$

Korzystamy z $1-\cos t=2\sin^2\frac t2$ dla $t=6x$:

$$
\frac{1-\cos6x}{x^2}=\frac{2\sin^2 3x}{x^2}=2\cdot9\cdot\left(\frac{\sin3x}{3x}\right)^2\ \to\ 18\cdot1=18.
$$

**Wynik:** $18$.

### 4.3. $\lim_{x\to\frac\pi2}\dfrac{\cos x}{\cos7x}$

Podstawiamy $x=\frac\pi2+t$, $t\to0$. Wtedy

$$
\cos x=\cos\left(\frac\pi2+t\right)=-\sin t,
$$

$$
\cos7x=\cos\left(\frac{7\pi}{2}+7t\right)=\cos\left(3\pi+\frac\pi2+7t\right)=-\cos\left(\frac\pi2+7t\right)=\sin7t.
$$
Zatem

$$
\frac{\cos x}{\cos7x}=\frac{-\sin t}{\sin7t}=-\frac{\sin t}{t}\cdot\frac{7t}{\sin7t}\cdot\frac17\ \to\ -\frac17.
$$

**Wynik:** $-\dfrac17$.

### 4.4. $\lim_{x\to0}\dfrac{\arctan3x}{7x}$

Podstawiamy $u=\arctan3x$. Wtedy $u\to0$ przy $x\to0$, $3x=\tan u$ i

$$
\frac{\arctan3x}{7x}=\frac{u}{\frac73\tan u}=\frac37\cdot\frac{u}{\tan u}\to\frac37\cdot1=\frac37.
$$

**Wynik:** $\dfrac37$.

### 4.5. $\lim_{x\to0}\dfrac{\sin7x}{4-\sqrt{5x+16}}$

Mnożymy licznik i mianownik przez sprzężenie mianownika:

$$
4-\sqrt{5x+16}=\frac{16-(5x+16)}{4+\sqrt{5x+16}}=\frac{-5x}{4+\sqrt{5x+16}}.
$$
Zatem

$$
\frac{\sin7x}{4-\sqrt{5x+16}}=\frac{\sin7x}{-5x}\cdot\left(4+\sqrt{5x+16}\right)=-\frac75\cdot\frac{\sin7x}{7x}\cdot\left(4+\sqrt{5x+16}\right).
$$
Gdy $x\to0$: $\dfrac{\sin7x}{7x}\to1$, a $4+\sqrt{5x+16}\to4+4=8$. Granica równa się $-\dfrac75\cdot8=-\dfrac{56}{5}$.

**Wynik:** $-\dfrac{56}{5}$.

### 4.6. $\lim_{x\to16}\dfrac{\sqrt{x\sqrt x}-8}{\sqrt[4]{x}-2}$

Dla $x\gt 0$ mamy $\sqrt{x\sqrt x}=\sqrt{x^{3/2}}=x^{3/4}$. Podstawiamy $t=\sqrt[4]{x}\gt 0$. Wtedy $x^{3/4}=t^3$, a $x\to16$ oznacza $t\to2$. Wyrażenie równa się

$$
\frac{t^3-8}{t-2}=\frac{(t-2)(t^2+2t+4)}{t-2}=t^2+2t+4\ \to\ 4+4+4=12.
$$

**Wynik:** $12$.

### 4.7. $\lim_{x\to0}\dfrac{\sqrt{x^2+4}-2}{\sqrt{x^2+9}-3}$

Mnożymy każdy ułamek przez sprzężenie licznika:

$$
\sqrt{x^2+4}-2=\frac{x^2}{\sqrt{x^2+4}+2}, \sqrt{x^2+9}-3=\frac{x^2}{\sqrt{x^2+9}+3}.
$$
Dla $x\neq0$:

$$
\frac{\sqrt{x^2+4}-2}{\sqrt{x^2+9}-3}=\frac{\sqrt{x^2+9}+3}{\sqrt{x^2+4}+2}\ \to\ \frac{3+3}{2+2}=\frac32.
$$

**Wynik:** $\dfrac32$.

### 4.8. $\lim_{x\to1^+}\left(\dfrac{3-x^2}{x+1}\right)^{\frac{1}{x-1}}$

Podstawa dla $x\to1$ zbiega do $\frac{3-1}{2}=1$. Zapisujemy ją jako $1+c(x)$:

$$
\frac{3-x^2}{x+1}-1=\frac{3-x^2-x-1}{x+1}=\frac{-x^2-x+2}{x+1}=-\frac{(x+2)(x-1)}{x+1}=c(x).
$$
Wykładnik $d(x)=\dfrac{1}{x-1}$ daje

$$
d(x) c(x)=-\frac{(x+2)}{x+1}\ \to\ -\frac32.
$$
Z lematu C granica równa się $e^{-3/2}$.

**Wynik:** $e^{-3/2}$.

### 4.9. $\lim_{x\to0}(\cos x)^{\cot^2x}$

Zapisujemy $(\cos x)^{\cot^2x}=\exp\left(\cot^2x\cdot\ln\cos x\right)$ i liczymy wykładnik. Mamy

$$
\cot^2x\cdot\ln\cos x=\frac{\cos^2x}{\sin^2x}\cdot\ln\cos x=\cos^2x\cdot\frac{x^2}{\sin^2x}\cdot\frac{\ln\cos x}{x^2}.
$$
Sprawdzamy kolejne granice:

- $\cos^2x\to1$ oraz $\dfrac{x^2}{\sin^2x}\to1$.
- Dla $\ln\cos x$ piszemy $\ln\cos x=\ln(1+c)$, gdzie $c=\cos x-1=-2\sin^2\frac x2$ i $c\to0$, $c\neq0$ dla $x\neq0$ bliskich zeru. Z $\dfrac{\ln(1+c)}{c}\to1$ oraz $\dfrac{c}{x^2}=-\dfrac{2\sin^2\frac x2}{x^2}=-\dfrac12\left(\dfrac{\sin\frac x2}{\frac x2}\right)^2\to-\dfrac12$ dostajemy

$$
\frac{\ln\cos x}{x^2}=\frac{\ln(1+c)}{c}\cdot\frac{c}{x^2}\to1\cdot\left(-\frac12\right)=-\frac12.
$$

Zatem wykładnik zbiega do $1\cdot1\cdot\left(-\dfrac12\right)=-\dfrac12$, a granica równa się $e^{-1/2}$.

**Wynik:** $e^{-1/2}$.

### 4.10. $\lim_{x\to+\infty}\left(\sqrt{e^x+1}-\sqrt{e^x-1}\right)$

Mnożymy przez sprzężenie:

$$
\sqrt{e^x+1}-\sqrt{e^x-1}=\frac{(e^x+1)-(e^x-1)}{\sqrt{e^x+1}+\sqrt{e^x-1}}=\frac{2}{\sqrt{e^x+1}+\sqrt{e^x-1}}.
$$
Mianownik zbiega do $+\infty$ (bo $e^x\to\infty$), więc granica równa się $0$.

**Wynik:** $0$.

### 4.11. $\lim_{x\to-\infty}\dfrac{\sqrt{2x^2+x+1}}{x}$

Dla $x\lt 0$ mamy $\sqrt{2x^2+x+1}=|x|\sqrt{2+\frac1x+\frac1{x^2}}=-x\sqrt{2+\frac1x+\frac1{x^2}}$. Dzielimy przez $x$:

$$
\frac{\sqrt{2x^2+x+1}}{x}=\frac{-x\sqrt{2+\frac1x+\frac1{x^2}}}{x}=-\sqrt{2+\frac1x+\frac1{x^2}}\ \to\ -\sqrt2.
$$

**Wynik:** $-\sqrt2$.

### 4.12. $\lim_{x\to-\infty}\left(\sqrt{(x+3)(x-4)}+x\right)$

Mamy $(x+3)(x-4)=x^2-x-12$. Postać $\infty-\infty$ przekształcamy przez sprzężenie:

$$
\sqrt{x^2-x-12}+x=\frac{(x^2-x-12)-x^2}{\sqrt{x^2-x-12}-x}=\frac{-x-12}{\sqrt{x^2-x-12}-x}.
$$
Dla $x\lt 0$ mamy $\sqrt{x^2-x-12}=-x\sqrt{1-\frac1x-\frac{12}{x^2}}$, więc mianownik to

$$
\sqrt{x^2-x-12}-x=-x\left(\sqrt{1-\frac1x-\frac{12}{x^2}}+1\right)\ \to\ +\infty,
$$
bo $-x\to+\infty$, a nawias zbiega do $2$. Licznik $-x-12\approx-x$. Zatem

$$
\frac{-x-12}{-x\left(\sqrt{1-\frac1x-\frac{12}{x^2}}+1\right)}=\frac{-x-12}{-x}\cdot\frac{1}{\sqrt{1-\frac1x-\frac{12}{x^2}}+1}\ \to\ 1\cdot\frac12=\frac12.
$$

**Wynik:** $\dfrac12$.

### 4.13. $\lim_{x\to-\infty}\dfrac{\sqrt{2-x}-\sqrt{1-x}}{x+\sqrt{x^2+2x+3}}$

*Licznik.* Mnożymy przez sprzężenie:

$$
\sqrt{2-x}-\sqrt{1-x}=\frac{(2-x)-(1-x)}{\sqrt{2-x}+\sqrt{1-x}}=\frac{1}{\sqrt{2-x}+\sqrt{1-x}}\ \to\ 0,
$$
bo dla $x\to-\infty$ mianownik zbiega do $+\infty$.

*Mianownik.* Mnożymy przez sprzężenie:

$$
x+\sqrt{x^2+2x+3}=\frac{(x^2+2x+3)-x^2}{\sqrt{x^2+2x+3}-x}=\frac{2x+3}{\sqrt{x^2+2x+3}-x}.
$$
Dla $x\lt 0$ mamy $\sqrt{x^2+2x+3}-x=-x\left(\sqrt{1+\frac2x+\frac3{x^2}}+1\right)\to+\infty$, a $2x+3\approx2x$. Zatem

$$
\frac{2x+3}{-x\left(\sqrt{1+\frac2x+\frac3{x^2}}+1\right)}\to\frac{2x}{-x\cdot2}=-1.
$$
Mianownik całego ułamka zbiega więc do $-1$, a licznik do $0$. Granica równa się $\dfrac{0}{-1}=0$.

**Wynik:** $0$.

### 4.14. $\lim_{x\to+\infty}x\cdot\arctan\dfrac1x$

Podstawiamy $u=\frac1x\to0^+$:

$$
x\arctan\frac1x=\frac{\arctan u}{u}\to1,
$$
bo $\lim_{u\to0}\dfrac{\arctan u}{u}=1$ (np. z $\arctan u=\arcsin\dfrac{u}{\sqrt{1+u^2}}$ lub z reguły granicy funkcji odwrotnej do $\tan$).

**Wynik:** $1$.

---

## Zadanie 5 (domowe)

### 5.1. $\lim_{x\to0^+}\cos\dfrac2x$ nie istnieje

Znajdziemy dwa ciągi $x_k\to0^+$ z różnymi granicami wartości funkcji.

- $x_k=\dfrac{1}{\pi k}$: wtedy $\dfrac2{x_k}=2\pi k$, więc $\cos\dfrac2{x_k}=1$.
- $x_k=\dfrac{4}{\pi(4k+1)}$: wtedy $\dfrac2{x_k}=\dfrac{\pi(4k+1)}{2}=2\pi k+\dfrac\pi2$, więc $\cos\dfrac2{x_k}=0$.

Oba ciągi zbiegają do $0^+$, a wartości są różne ($1$ i $0$). Zatem granica nie istnieje.

### 5.2. $\lim_{x\to1}2^{\frac{1}{x-1}}$ nie istnieje

- **Prawostronna:** dla $x\to1^+$ mamy $\dfrac{1}{x-1}\to+\infty$, więc $2^{\frac1{x-1}}\to+\infty$.
- **Lewostronna:** dla $x\to1^-$ mamy $\dfrac{1}{x-1}\to-\infty$, więc $2^{\frac1{x-1}}\to0$.

Granica prawostronna jest nieskończona, a lewostronna równa $0$. Granica dwustronna nie istnieje (nie jest ani skończona, ani $\pm\infty$ z obu stron).

### 5.3. $\lim_{x\to0}\sin\left(\arctan\dfrac1x\right)$ nie istnieje

Dla $u\in\mathbb{R}$ zachodzi $\sin(\arctan u)=\dfrac{u}{\sqrt{1+u^2}}$ (z trójkąta prostokątnego o przyprostokątnych $1$ i $u$). Dla $u=\frac1x$, $x\neq0$:

$$
\sin\left(\arctan\frac1x\right)=\frac{\frac1x}{\sqrt{1+\frac1{x^2}}}=\frac{1}{x}\cdot\frac{|x|}{\sqrt{1+x^2}}.
$$
Dla $x\gt 0$ mamy $\frac{1}{x}\cdot\frac{|x|}{\sqrt{1+x^2}}=\frac{1}{\sqrt{1+x^2}}\to1$, a dla $x\lt 0$ mamy $\frac{1}{x}\cdot\frac{|x|}{\sqrt{1+x^2}}=-\frac{1}{\sqrt{1+x^2}}\to-1$.

Granice jednostronne są więc różne ($+1$ z prawej, $-1$ z lewej), zatem granica nie istnieje.

---

## Zadanie 6 (domowe)

Dla $x\in\mathbb{R}$ przyjmujemy

$$
\cosh x=\frac{e^x+e^{-x}}{2}, \sinh x=\frac{e^x-e^{-x}}{2}, \tanh x=\frac{\sinh x}{\cosh x}.
$$

### 6.1. $\cosh^2x-\sinh^2x=1$

$$
\cosh^2x-\sinh^2x=\frac{(e^x+e^{-x})^2-(e^x-e^{-x})^2}{4}=\frac{4e^xe^{-x}}{4}=1.
$$

### 6.2. $\cosh^2x+\sinh^2x=\cosh2x$

$$
\cosh^2x+\sinh^2x=\frac{(e^x+e^{-x})^2+(e^x-e^{-x})^2}{4}=\frac{2e^{2x}+2e^{-2x}}{4}=\frac{e^{2x}+e^{-2x}}{2}=\cosh2x.
$$

### 6.3. $\sinh2x=2\sinh x\cosh x$

$$
2\sinh x\cosh x=2\cdot\frac{(e^x-e^{-x})(e^x+e^{-x})}{4}=\frac{e^{2x}-e^{-2x}}{2}=\sinh2x.
$$

### 6.4. $\cosh^2x=\dfrac{1}{1-\tanh^2x}$

Z 6.1 po podzieleniu przez $\cosh^2x\neq0$ dostajemy $1-\dfrac{\sinh^2x}{\cosh^2x}=\dfrac{1}{\cosh^2x}$, czyli $1-\tanh^2x=\dfrac{1}{\cosh^2x}$. Ponieważ prawa strona jest dodatnia, mianownik $1-\tanh^2x$ jest różny od zera i po odwróceniu dostajemy $\cosh^2x=\dfrac{1}{1-\tanh^2x}$.

---

## Podsumowanie

| Zadanie | Wynik |
|---|---|
| 1.1 | $0$ |
| 1.2 | $-1$ |
| 1.3 | $\dfrac37$ |
| 1.4 | $-2$ |
| 1.5 | $e^{-3/2}$ |
| 1.6 | $1$ |
| 2 | granica istnieje, $\dfrac1e$ (obie strony) |
| 3.1 | granica nie istnieje (prawa $e$, lewa $\dfrac1e$) |
| 3.2 | granica nie istnieje |
| 4.1 | $2$ |
| 4.2 | $18$ |
| 4.3 | $-\dfrac17$ |
| 4.4 | $\dfrac37$ |
| 4.5 | $-\dfrac{56}{5}$ |
| 4.6 | $12$ |
| 4.7 | $\dfrac32$ |
| 4.8 | $e^{-3/2}$ |
| 4.9 | $e^{-1/2}$ |
| 4.10 | $0$ |
| 4.11 | $-\sqrt2$ |
| 4.12 | $\dfrac12$ |
| 4.13 | $0$ |
| 4.14 | $1$ |
| 5.1 | granica nie istnieje |
| 5.2 | granica nie istnieje |
| 5.3 | granica nie istnieje (prawa $1$, lewa $-1$) |
| 6.1–6.4 | tożsamości udowodnione powyżej |
