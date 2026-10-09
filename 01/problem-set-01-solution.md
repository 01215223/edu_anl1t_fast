# Powtórzenie ze szkoły średniej — rozwiązania (zestaw 01)

Zestaw zadań: [`problem-set-01.md`](problem-set-01.md) — zadania 1–6, wszystkie punkty.

**Konwencje**

- $\log$ bez podstawy oznacza $\log_{10}$ (konwencja szkolna); $\log_a$ to logarytm o podstawie $a$.
- $D_f$ — dziedzina, $R_f$ — zbiór wartości.
- Potęga $a^t$ o wykładniku rzeczywistym wymaga $a>0$; $\log_a b$ wymaga $a>0$, $a\neq1$, $b>0$.
- Zapis „funkcja maleje na $(-\infty,-2)$ i na $(-2,\infty)$” oznacza, że maleje na każdym z tych przedziałów osobno (nie na ich sumie).

---

## Zadanie 1

Dla $f(x)=x^x+\log_x\left(1+2\sqrt x+3x^2\right)$ wyznaczamy $f(-x)$, $f\left(\frac1x\right)$, $f(\sqrt x)$ oraz $f(x^2)$.

**Idea.** Każde z tych wyrażeń to $f(t)$, gdzie $t$ zależy od $x$. W definicji $f$ wpisujemy $t$ w miejsce każdego $x$. Wyrażenie $f(t)$ ma sens dokładnie wtedy, gdy $t\in D_f$, czyli gdy $t>0$ i $t\neq1$.

**Dziedzina funkcji $f$.**

- $x^x$ wymaga $x>0$;
- $\log_x(\dots)$ wymaga $x>0$ i $x\neq1$;
- $\sqrt x$ wymaga $x\geq0$;
- liczba logarytmowana $1+2\sqrt x+3x^2$ jest dodatnia dla $x\geq0$.

$$
D_f=(0,1)\cup(1,\infty)
$$

### 1.1. $f(-x)$

Podstawiamy $t=-x$:

$$
f(-x)=(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3x^2\right)
$$

Warunki: $-x>0\iff x<0$ oraz $-x\neq1\iff x\neq-1$. Pierwiastek $\sqrt{-x}$ wymaga $-x\geq0$, co już wynika z $x<0$.

$$
D_{f(-x)}=(-\infty,-1)\cup(-1,0)
$$

### 1.2. $f\left(\frac1x\right)$

Podstawiamy $t=\frac1x$. Dla $x>0$ mamy $\sqrt{\frac1x}=\frac{1}{\sqrt x}$ oraz $\left(\frac1x\right)^2=\frac{1}{x^2}$:

$$
f\left(\frac1x\right)=\left(\frac1x\right)^{\frac1x}+\log_{\frac1x}\left(1+\frac{2}{\sqrt x}+\frac{3}{x^2}\right)
$$

Warunki: $\frac1x>0\iff x>0$ oraz $\frac1x\neq1\iff x\neq1$.

$$
D_{f(1/x)}=(0,1)\cup(1,\infty)
$$

Uproszczenie: $\left(\frac1x\right)^{\frac1x}=x^{-\frac1x}$ oraz $\log_{\frac1x}b=-\log_x b$, więc

$$
f\left(\frac1x\right)=x^{-\frac1x}-\log_x\left(1+\frac{2}{\sqrt x}+\frac{3}{x^2}\right)
$$

### 1.3. $f(\sqrt x)$

Podstawiamy $t=\sqrt x$. Wtedy $\sqrt t=\sqrt{\sqrt x}=x^{\frac14}$ oraz $t^2=x$:

$$
f(\sqrt x)=(\sqrt x)^{\sqrt x}+\log_{\sqrt x}\left(1+2x^{\frac14}+3x\right)
$$

Warunki: $\sqrt x>0\iff x>0$ oraz $\sqrt x\neq1\iff x\neq1$.

$$
D_{f(\sqrt x)}=(0,1)\cup(1,\infty)
$$

Uproszczenie: $(\sqrt x)^{\sqrt x}=e^{\frac{\sqrt x}{2}\ln x}=x^{\frac{\sqrt x}{2}}$.

### 1.4. $f(x^2)$

Podstawiamy $t=x^2$. Wtedy $\sqrt t=\sqrt{x^2}=|x|$ oraz $t^2=x^4$:

$$
f(x^2)=(x^2)^{x^2}+\log_{x^2}\left(1+2|x|+3x^4\right)
$$

Warunki: $x^2>0\iff x\neq0$ oraz $x^2\neq1\iff x\neq\pm1$.

$$
D_{f(x^2)}=\mathbb{R}\setminus\{-1,0,1\}
$$

Uproszczenie: $(x^2)^{x^2}=|x|^{2x^2}$ dla $x\neq0$.

**Podsumowanie zadania 1**

| Wyrażenie | Wzór | Dziedzina |
|---|---|---|
| $f(-x)$ | $(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3x^2\right)$ | $(-\infty,-1)\cup(-1,0)$ |
| $f\left(\frac1x\right)$ | $\left(\frac1x\right)^{\frac1x}+\log_{\frac1x}\left(1+\frac{2}{\sqrt x}+\frac{3}{x^2}\right)$ | $(0,1)\cup(1,\infty)$ |
| $f(\sqrt x)$ | $(\sqrt x)^{\sqrt x}+\log_{\sqrt x}\left(1+2x^{\frac14}+3x\right)$ | $(0,1)\cup(1,\infty)$ |
| $f(x^2)$ | $(x^2)^{x^2}+\log_{x^2}\left(1+2\lvert x\rvert+3x^4\right)$ | $\mathbb{R}\setminus\{-1,0,1\}$ |

---

## Zadanie 2

Dla każdej z funkcji wyznaczamy $D_f$, $R_f$, przedziały monotoniczności i szkicujemy wykres.

### 2.1. $f(x)=\dfrac{x^2-3x+2}{4-x^2}$

**Uproszczenie.** $x^2-3x+2=(x-1)(x-2)$ oraz $4-x^2=-(x-2)(x+2)$, więc dla $x\neq2$

$$
f(x)=\frac{(x-1)(x-2)}{-(x-2)(x+2)}=-\frac{x-1}{x+2}=-1+\frac{3}{x+2}.
$$

**Dziedzina.** $4-x^2\neq0\iff x\neq\pm2$:

$$
D_f=\mathbb{R}\setminus\{-2,2\}
$$

**Zbiór wartości.** Z równania $y=-1+\frac{3}{x+2}$ wynika $x=\frac{3}{y+1}-2$ dla $y\neq-1$.

- Dla $y=-1$ rozwiązania nie ma (asymptota pozioma).
- Dla $y=-\frac14$ dostajemy $x=2\notin D_f$, więc ta wartość nie jest przyjmowana.
- Dla każdej innej wartości $y$ rozwiązanie należy do $D_f$.

$$
R_f=\mathbb{R}\setminus\left\{-1,-\tfrac14\right\}
$$

**Monotoniczność.** $f'(x)=-\dfrac{3}{(x+2)^2}<0$ dla $x\in D_f$. Funkcja **maleje** na każdym z przedziałów $(-\infty,-2)$, $(-2,2)$, $(2,\infty)$.

**Wykres (szkic).**

- Asymptoty: pionowa $x=-2$, pozioma $y=-1$.
- Miejsce zerowe: $(1,0)$. Punkt przecięcia z osią $OY$: $\left(0,\frac12\right)$.
- „Dziura” w punkcie $\left(2,-\frac14\right)$: funkcja nie jest tam określona, a jej granica wynosi $-\frac14$.
- Prawa gałąź ($x>-2$): maleje od $+\infty$ (przy $x\to-2^+$) przez $\left(0,\frac12\right)$ i $(1,0)$ do dziury, a potem do asymptoty $y=-1$ (przy $x\to\infty$).
- Lewa gałąź ($x<-2$): maleje od $y=-1$ (przy $x\to-\infty$) do $-\infty$ (przy $x\to-2^-$).

| $x$ | $-4$ | $-3$ | $-1$ | $0$ | $1$ | $3$ | $4$ |
|---|---|---|---|---|---|---|---|
| $f(x)$ | $-\frac52$ | $-4$ | $2$ | $\frac12$ | $0$ | $-\frac25$ | $-\frac12$ |

### 2.2. $f(x)=\dfrac{\log_{\sqrt2}\frac12-\log_3x}{\log_3(9x)}\cdot\left(x^2-x-2\right)$

**Uproszczenie.** $\log_{\sqrt2}\frac12=-2$, bo $(\sqrt2)^{-2}=\frac12$. Ponadto $\log_3(9x)=\log_3 9+\log_3x=2+\log_3x$. Ułamek jest więc równy

$$
\frac{-2-\log_3x}{2+\log_3x}=-1
$$

(o ile mianownik jest różny od zera). Stąd dla $x\in D_f$

$$
f(x)=-(x^2-x-2)=-x^2+x+2=-\left(x-\tfrac12\right)^2+\tfrac94.
$$

**Dziedzina.** $\log_3x$ wymaga $x>0$, a mianownik $\log_3(9x)\neq0\iff 9x\neq1$:

$$
D_f=\left(0,\tfrac19\right)\cup\left(\tfrac19,\infty\right)
$$

**Zbiór wartości.** Niech $g(x)=-x^2+x+2$. Na $\left(0,\frac12\right]$ funkcja $g$ rośnie, a jej wartości idą od $2$ (granica, której nie osiągamy) do $\frac94$. Na $\left[\frac12,\infty\right)$ funkcja $g$ maleje od $\frac94$ do $-\infty$. Zatem $g$ przyjmuje na $(0,\infty)$ dokładnie wartości z $\left(-\infty,\frac94\right]$.

Punkt $x=\frac19$ jest wyłączony, więc wartość $g\left(\frac19\right)=\frac{170}{81}$ mogłaby zniknąć. Równanie $g(x)=\frac{170}{81}$ ma jednak pierwiastki $x=\frac19$ oraz $x=\frac89$, a $\frac89\in D_f$. Żadna wartość nie znika:

$$
R_f=\left(-\infty,\tfrac94\right]
$$

**Monotoniczność.** $f'(x)=-2x+1$, więc $f'(x)>0$ dla $x<\frac12$ i $f'(x)<0$ dla $x>\frac12$. Ponieważ $\frac19\notin D_f$, przedział $\left(0,\frac12\right)$ trzeba podzielić:

- $f$ **rośnie** na $\left(0,\frac19\right)$ oraz na $\left(\frac19,\frac12\right)$,
- $f$ **maleje** na $\left(\frac12,\infty\right)$.

**Wykres (szkic).**

- Fragment paraboli $y=-x^2+x+2$ (ramiona w dół) dla $x>0$.
- Wierzchołek (maksimum): $\left(\frac12,\frac94\right)$.
- Miejsce zerowe: $(2,0)$. Drugie miejsce zerowe, $x=-1$, leży poza $D_f$.
- Punkt $(0,2)$ nie należy do wykresu (otwarty koniec), bo $0\notin D_f$; $f(x)\to2$ przy $x\to0^+$.
- „Dziura” w punkcie $\left(\frac19,\frac{170}{81}\right)$, gdzie $\frac{170}{81}\approx2{,}1$.
- Dla $x\to\infty$ wykres schodzi do $-\infty$.

| $x$ | $\frac13$ | $\frac12$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|---|
| $f(x)$ | $\frac{20}{9}$ | $\frac94$ | $2$ | $0$ | $-4$ |

---

## Zadanie 3

### 3.1. $(1-x)(2-x)^2(x+3)^3<0$

Pierwiastki: $x=1$ (krotność 1), $x=2$ (krotność 2), $x=-3$ (krotność 3). Znaki czynników i iloczynu:

| przedział | $(-\infty,-3)$ | $(-3,1)$ | $(1,2)$ | $(2,\infty)$ |
|---|---|---|---|---|
| $1-x$ | $+$ | $+$ | $-$ | $-$ |
| $(2-x)^2$ | $+$ | $+$ | $+$ | $+$ |
| $(x+3)^3$ | $-$ | $+$ | $+$ | $+$ |
| iloczyn | $-$ | $+$ | $-$ | $-$ |

Iloczyn jest ujemny na $(-\infty,-3)\cup(1,2)\cup(2,\infty)$. W punktach $-3$, $1$ i $2$ jest równy $0$, więc nie spełnia ostrej nierówności.

**Odpowiedź:** $x\in(-\infty,-3)\cup(1,2)\cup(2,\infty)$.

### 3.2. $\dfrac{(x+3)^3}{(x^2-1)(x+1)}\geq0$

**Dziedzina.** $(x^2-1)(x+1)=(x-1)(x+1)^2\neq0\iff x\neq\pm1$.

| przedział | $(-\infty,-3)$ | $-3$ | $(-3,-1)$ | $-1$ | $(-1,1)$ | $1$ | $(1,\infty)$ |
|---|---|---|---|---|---|---|---|
| $(x+3)^3$ | $-$ | $0$ | $+$ | $+$ | $+$ | $+$ | $+$ |
| $(x^2-1)(x+1)$ | $-$ | $-$ | $-$ | $0$ | $-$ | $0$ | $+$ |
| iloraz | $+$ | $0$ | $-$ | nie istnieje | $-$ | nie istnieje | $+$ |

**Odpowiedź:** $x\in(-\infty,-3]\cup(1,\infty)$.

### 3.3. $3\log(x+1)=\log(1-x^2)$

**Dziedzina.** $x+1>0$ i $1-x^2>0$, czyli $x\in(-1,1)$.

Ponieważ $3\log(x+1)=\log(x+1)^3$, a logarytm jest różnowartościowy, w dziedzinie mamy

$$
(x+1)^3=1-x^2\iff(x+1)\left[(x+1)^2-(1-x)\right]=0\iff x(x+1)(x+3)=0.
$$

Stąd $x\in\{-3,-1,0\}$. W przedziale $(-1,1)$ leży tylko $x=0$. Sprawdzenie: $3\log1=0=\log1$.

**Odpowiedź:** $x=0$.

Uwaga: podstawa logarytmu nie ma tu znaczenia, bo jest taka sama po obu stronach.

### 3.4. $\dfrac{x^2-x}{\log_2x-1}\leq0$

**Dziedzina.** $x>0$ oraz $\log_2x\neq1\iff x\neq2$: $D=(0,2)\cup(2,\infty)$.

| przedział | $(0,1)$ | $1$ | $(1,2)$ | $2$ | $(2,\infty)$ |
|---|---|---|---|---|---|
| $x^2-x=x(x-1)$ | $-$ | $0$ | $+$ | $+$ | $+$ |
| $\log_2x-1$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| iloraz | $+$ | $0$ | $-$ | nie istnieje | $+$ |

**Odpowiedź:** $x\in[1,2)$.

W $x=1$ licznik się zeruje, a mianownik jest różny od zera, więc iloraz wynosi $0$ i nierówność „$\leq$” jest spełniona.

### 3.5. $2^{|x|-1}\leq\left(\dfrac12\right)^{|x|}$

Ponieważ $\left(\frac12\right)^{|x|}=2^{-|x|}$, a funkcja $t\mapsto2^t$ jest rosnąca (podstawa $2>1$), nierówność jest równoważna nierówności wykładników:

$$
\lvert x\rvert-1\leq-\lvert x\rvert\iff2\lvert x\rvert\leq1\iff\lvert x\rvert\leq\tfrac12.
$$

**Odpowiedź:** $x\in\left[-\tfrac12,\tfrac12\right]$.

---

## Zadanie 4

Dla $f(x)=\dfrac{1+2x}{x-x^2}+\sin\left(x^{-1}+\sqrt x\right)$.

**Dziedzina $f$.** $x-x^2=x(1-x)\neq0\iff x\neq0,\ x\neq1$; $x^{-1}$ wymaga $x\neq0$; $\sqrt x$ wymaga $x\geq0$:

$$
D_f=(0,1)\cup(1,\infty)
$$

Podstawiamy $t$ w miejsce $x$ tak samo jak w zadaniu 1. Warunek to $t\in D_f$, czyli $t>0$ i $t\neq1$.

### 4.1. $f(-x)$

$$
f(-x)=\frac{1-2x}{-x-x^2}+\sin\left(-\frac1x+\sqrt{-x}\right)=\frac{2x-1}{x^2+x}+\sin\left(-\frac1x+\sqrt{-x}\right)
$$

Warunki: $-x>0\iff x<0$ oraz $-x\neq1\iff x\neq-1$:

$$
D_{f(-x)}=(-\infty,-1)\cup(-1,0)
$$

### 4.2. $f\left(\frac1x\right)$

Tu $\left(\frac1x\right)^{-1}=x$, $\sqrt{\frac1x}=\frac{1}{\sqrt x}$ oraz

$$
\frac{1+\frac2x}{\frac1x-\frac1{x^2}}=\frac{\frac{x+2}{x}}{\frac{x-1}{x^2}}=\frac{x(x+2)}{x-1}.
$$

Zatem

$$
f\left(\frac1x\right)=\frac{x(x+2)}{x-1}+\sin\left(x+\frac{1}{\sqrt x}\right)
$$

Warunki: $\frac1x>0\iff x>0$ oraz $\frac1x\neq1\iff x\neq1$:

$$
D_{f(1/x)}=(0,1)\cup(1,\infty)
$$

### 4.3. $f(\sqrt x)$

Tu $t^{-1}=x^{-\frac12}$, $\sqrt t=x^{\frac14}$ oraz $t-t^2=\sqrt x-x$:

$$
f(\sqrt x)=\frac{1+2\sqrt x}{\sqrt x-x}+\sin\left(x^{-\frac12}+x^{\frac14}\right)
$$

Warunki: $\sqrt x>0\iff x>0$ oraz $\sqrt x\neq1\iff x\neq1$:

$$
D_{f(\sqrt x)}=(0,1)\cup(1,\infty)
$$

### 4.4. $f(x^2)$

Tu $t^{-1}=\frac{1}{x^2}$, $\sqrt t=|x|$ oraz $t-t^2=x^2-x^4$:

$$
f(x^2)=\frac{1+2x^2}{x^2-x^4}+\sin\left(\frac{1}{x^2}+|x|\right)
$$

Warunki: $x^2>0\iff x\neq0$ oraz $x^2\neq1\iff x\neq\pm1$:

$$
D_{f(x^2)}=\mathbb{R}\setminus\{-1,0,1\}
$$

**Uwaga.** Sinus przyjmuje każdą wartość rzeczywistą, więc nie nakłada dodatkowych warunków. Wszystkie ograniczenia pochodzą od mianowników, $x^{-1}$ i $\sqrt x$.

---

## Zadanie 5

### 5.1. $f(x)=\dfrac{1}{\sqrt{x^2-2x+1}}$

**Uproszczenie.** $x^2-2x+1=(x-1)^2$, więc $\sqrt{(x-1)^2}=|x-1|$ i

$$
f(x)=\frac{1}{|x-1|}.
$$

**Dziedzina.** Pierwiastek jest w mianowniku, więc $(x-1)^2>0\iff x\neq1$:

$$
D_f=\mathbb{R}\setminus\{1\}
$$

**Zbiór wartości.** Dla $x\in D_f$ mamy $f(x)>0$. Dla dowolnego $y>0$ równanie $\frac{1}{|x-1|}=y$ ma rozwiązania $x=1\pm\frac1y$, różne od $1$. Zatem

$$
R_f=(0,\infty)
$$

**Monotoniczność.**

- Dla $x<1$: $f(x)=\dfrac{1}{1-x}$ oraz $f'(x)=\dfrac{1}{(1-x)^2}>0$. Funkcja **rośnie** na $(-\infty,1)$. Sprawdzenie: $f(0)=1<2=f\left(\frac12\right)$.
- Dla $x>1$: $f(x)=\dfrac{1}{x-1}$ oraz $f'(x)=-\dfrac{1}{(x-1)^2}<0$. Funkcja **maleje** na $(1,\infty)$.

**Wykres (szkic).** Dwie gałęzie hiperboli $y=\frac{1}{|x|}$ przesunięte o $1$ w prawo. Wykres jest symetryczny względem prostej $x=1$.

- Asymptoty: pionowa $x=1$, pozioma $y=0$.
- Nie przecina osi $OX$. Punkt przecięcia z osią $OY$: $(0,1)$.
- Lewa gałąź: rośnie od $0$ (przy $x\to-\infty$) do $+\infty$ (przy $x\to1^-$).
- Prawa gałąź: maleje od $+\infty$ (przy $x\to1^+$) do $0$ (przy $x\to+\infty$).

| $x$ | $-1$ | $0$ | $\frac12$ | $\frac32$ | $2$ | $3$ |
|---|---|---|---|---|---|---|
| $f(x)$ | $\frac12$ | $1$ | $2$ | $2$ | $1$ | $\frac12$ |

### 5.2. $f(x)=\dfrac{x^2+x+6}{2\log_5(x+1)}\cdot\log_5\left(x^2+2x+1\right)$

**Uproszczenie.** Dla $x>-1$ mamy $\log_5(x^2+2x+1)=\log_5(x+1)^2=2\log_5(x+1)$, więc dla $x\in D_f$

$$
f(x)=\frac{x^2+x+6}{2\log_5(x+1)}\cdot2\log_5(x+1)=x^2+x+6.
$$

**Dziedzina.** $\log_5(x+1)$ wymaga $x+1>0$, a mianownik $2\log_5(x+1)\neq0\iff x+1\neq1\iff x\neq0$:

$$
D_f=(-1,0)\cup(0,\infty)
$$

**Zbiór wartości.** Wierzchołek paraboli to $x=-\frac12$, a $f\left(-\frac12\right)=\frac{23}{4}$.

- Na $(-1,0)$ najmniejszą wartością jest $\frac{23}{4}$ (w $x=-\frac12$). Przy $x\to-1^+$ i $x\to0^-$ wartości dążą do $6$, ale nie są osiągane. Dostajemy $\left[\frac{23}{4},6\right)$.
- Na $(0,\infty)$ funkcja rośnie od $6$ (nieosiągane, bo $0\notin D_f$) do $+\infty$. Dostajemy $(6,\infty)$.

$$
R_f=\left[\tfrac{23}{4},6\right)\cup(6,\infty)
$$

Wartość $6$ nie należy do $R_f$: równanie $x^2+x+6=6$ ma pierwiastki $x=0$ i $x=-1$, a oba są poza $D_f$.

**Monotoniczność.** $f'(x)=2x+1$:

- $f$ **maleje** na $\left(-1,-\frac12\right)$,
- $f$ **rośnie** na $\left(-\frac12,0\right)$ oraz na $(0,\infty)$.

**Wykres (szkic).** Fragment paraboli $y=x^2+x+6$ (ramiona w górę):

- wierzchołek $\left(-\frac12,\frac{23}{4}\right)$ — najniższy punkt wykresu,
- punkty otwarte (nienależące do wykresu): $(-1,6)$ i $(0,6)$ — „dziura” w $(0,6)$,
- brak miejsc zerowych, bo wyróżnik $1-24<0$; $x=0$ nie należy do dziedziny, więc wykres nie przecina osi $OY$.

| $x$ | $-\frac34$ | $-\frac12$ | $-\frac14$ | $1$ | $2$ |
|---|---|---|---|---|---|
| $f(x)$ | $\frac{93}{16}$ | $\frac{23}{4}$ | $\frac{93}{16}$ | $8$ | $12$ |

---

## Zadanie 6

### 6.1. $\sqrt{x+4}>x-8$

**Dziedzina:** $x+4\geq0\iff x\geq-4$.

- *Przypadek 1: $x<8$.* Prawa strona jest ujemna, a lewa nieujemna, więc nierówność jest spełniona dla wszystkich $x\in[-4,8)$.
- *Przypadek 2: $x\geq8$.* Obie strony są nieujemne, więc podnosimy do kwadratu:

$$
x+4>(x-8)^2\iff x^2-17x+60<0\iff(x-5)(x-12)<0\iff5<x<12.
$$

Z warunkiem $x\geq8$ daje to $x\in[8,12)$.

Suma przypadków: $[-4,8)\cup[8,12)=[-4,12)$.

**Uwaga.** Samo podniesienie do kwadratu daje tylko $(5,12)$ i gubi rozwiązania z $[-4,5]$, gdzie prawa strona $x-8$ jest ujemna. Dlatego trzeba rozpatrzyć przypadki osobno.

**Odpowiedź:** $x\in[-4,12)$.

### 6.2. $\sqrt{x+5}=5-\sqrt{x+10}$

**Dziedzina:** $x+5\geq0\iff x\geq-5$.

Równanie ma postać $\sqrt{x+5}+\sqrt{x+10}=5$. Podnosimy obie strony do kwadratu:

$$
x+5=25-10\sqrt{x+10}+(x+10)\ \Longrightarrow\ 10\sqrt{x+10}=30\ \Longrightarrow\ \sqrt{x+10}=3\ \Longrightarrow\ x=-1.
$$

Sprawdzenie: $\sqrt4=2$ oraz $5-\sqrt9=2$. Rozwiązanie jest jedyne, bo lewa strona $\sqrt{x+5}+\sqrt{x+10}$ jest rosnąca.

**Odpowiedź:** $x=-1$.

### 6.3. $(1-x)^{-1}(2-x)^{-2}(x-3)\geq0$

Zapis: $\dfrac{x-3}{(1-x)(2-x)^2}\geq0$.

**Dziedzina:** $x\neq1$ i $x\neq2$, bo muszą istnieć $(1-x)^{-1}$ i $(2-x)^{-2}$. Dla $x\neq2$ czynnik $(2-x)^2$ jest dodatni, więc o znaku decyduje $\dfrac{x-3}{1-x}$.

| przedział | $(-\infty,1)$ | $1$ | $(1,2)$ | $2$ | $(2,3)$ | $3$ | $(3,\infty)$ |
|---|---|---|---|---|---|---|---|
| $x-3$ | $-$ | $-$ | $-$ | $-$ | $-$ | $0$ | $+$ |
| $1-x$ | $+$ | $0$ | $-$ | $-$ | $-$ | $-$ | $-$ |
| iloraz | $-$ | nie istnieje | $+$ | nie istnieje | $+$ | $0$ | $-$ |

**Odpowiedź:** $x\in(1,2)\cup(2,3]$.

**Uwaga.** Iloraz jest dodatni po obu stronach punktu $x=2$, ale sam punkt nie należy do rozwiązań: wyrażenie $(2-x)^{-2}$ w nim nie istnieje.

### 6.4. $\log_3(x+1)+\log_{\sqrt3}(x+1)+\log_{\frac13}(x+1)=6$

**Dziedzina:** $x+1>0\iff x>-1$.

Niech $t=\log_3(x+1)$. Zmieniamy podstawy na $3$, korzystając ze wzoru $\log_a b=\dfrac{\log_3 b}{\log_3 a}$:

$$
\log_{\sqrt3}(x+1)=\frac{t}{\log_3\sqrt3}=\frac{t}{\frac12}=2t,\qquad\log_{\frac13}(x+1)=\frac{t}{\log_3\frac13}=\frac{t}{-1}=-t.
$$

Równanie przyjmuje postać $t+2t-t=6$, czyli $2t=6$, a stąd $t=3$. Zatem $x+1=3^3=27$, czyli $x=26$.

Sprawdzenie: $\log_327+\log_{\sqrt3}27+\log_{\frac13}27=3+6-3=6$.

**Odpowiedź:** $x=26$.

### 6.5. $(\log x-1)(\log x-10)(x+2)\leq0$

Tu $\log=\log_{10}$. Dziedzina: $x>0$. Dla $x>0$ czynnik $x+2$ jest dodatni, więc

$$
(\log x-1)(\log x-10)\leq0\iff1\leq\log x\leq10\iff10\leq x\leq10^{10}.
$$

**Odpowiedź:** $x\in\left[10,\,10^{10}\right]$.

Uwaga: przy innej podstawie logarytmu przedział byłby inny (dla $\ln$ byłoby to $[e,e^{10}]$).

### 6.6. $\dfrac{\log_2x-1}{x^2-x}\leq0$

**Dziedzina.** $x>0$ oraz $x^2-x=x(x-1)\neq0$, czyli $x\neq1$: $D=(0,1)\cup(1,\infty)$.

| przedział | $(0,1)$ | $(1,2)$ | $2$ | $(2,\infty)$ |
|---|---|---|---|---|
| $\log_2x-1$ | $-$ | $-$ | $0$ | $+$ |
| $x^2-x$ | $-$ | $+$ | $+$ | $+$ |
| iloraz | $+$ | $-$ | $0$ | $+$ |

**Odpowiedź:** $x\in(1,2]$.

Uwaga: domknięty koniec przedziału pojawia się tylko tam, gdzie zeruje się licznik. Tutaj to $x=2$, a w zadaniu 3.4 — $x=1$.

### 6.7. $\left(2^{|x+2|}\right)^2-4\cdot2^{1-x}<0$

Mamy $\left(2^{|x+2|}\right)^2=2^{2|x+2|}$ oraz $4\cdot2^{1-x}=2^{3-x}$. Ponieważ $t\mapsto2^t$ jest rosnąca:

$$
2^{2|x+2|}<2^{3-x}\iff2|x+2|<3-x.
$$

- *Przypadek 1: $x\geq-2$.* Wtedy $2(x+2)<3-x\iff3x<-1\iff x<-\frac13$. Wynik: $\left[-2,-\frac13\right)$.
- *Przypadek 2: $x<-2$.* Wtedy $-2(x+2)<3-x\iff-x<7\iff x>-7$. Wynik: $(-7,-2)$.

Suma: $(-7,-2)\cup\left[-2,-\frac13\right)=\left(-7,-\frac13\right)$.

**Odpowiedź:** $x\in\left(-7,-\frac13\right)$.

Uwaga: w krańcach $x=-7$ i $x=-\frac13$ obie strony są równe ($2^{10}=4\cdot2^{8}$ oraz $2^{10/3}=4\cdot2^{4/3}$), więc te punkty są wyłączone.

---

## Podsumowanie

| Zadanie | Odpowiedź |
|---|---|
| 1 | $D_f=(0,1)\cup(1,\infty)$; wzory dla $f(-x)$, $f\left(\frac1x\right)$, $f(\sqrt x)$, $f(x^2)$ — patrz wyżej |
| 2.1 | $D_f=\mathbb{R}\setminus\{-2,2\}$, $R_f=\mathbb{R}\setminus\left\{-1,-\frac14\right\}$, maleje na $(-\infty,-2)$, $(-2,2)$, $(2,\infty)$ |
| 2.2 | $D_f=\left(0,\frac19\right)\cup\left(\frac19,\infty\right)$, $R_f=\left(-\infty,\frac94\right]$, rośnie na $\left(0,\frac19\right)$ i $\left(\frac19,\frac12\right)$, maleje na $\left(\frac12,\infty\right)$ |
| 3.1 | $x\in(-\infty,-3)\cup(1,2)\cup(2,\infty)$ |
| 3.2 | $x\in(-\infty,-3]\cup(1,\infty)$ |
| 3.3 | $x=0$ |
| 3.4 | $x\in[1,2)$ |
| 3.5 | $x\in\left[-\frac12,\frac12\right]$ |
| 4 | $D_f=(0,1)\cup(1,\infty)$; wzory dla czterech wyrażeń — patrz wyżej |
| 5.1 | $D_f=\mathbb{R}\setminus\{1\}$, $R_f=(0,\infty)$, rośnie na $(-\infty,1)$, maleje na $(1,\infty)$ |
| 5.2 | $f(x)=x^2+x+6$ na $(-1,0)\cup(0,\infty)$; $R_f=\left[\frac{23}{4},6\right)\cup(6,\infty)$; maleje na $\left(-1,-\frac12\right)$; rośnie na $\left(-\frac12,0\right)$ i $(0,\infty)$ |
| 6.1 | $x\in[-4,12)$ |
| 6.2 | $x=-1$ |
| 6.3 | $x\in(1,2)\cup(2,3]$ |
| 6.4 | $x=26$ |
| 6.5 | $x\in\left[10,10^{10}\right]$ |
| 6.6 | $x\in(1,2]$ |
| 6.7 | $x\in\left(-7,-\frac13\right)$ |
