# Powtórzenie ze szkoły średniej — odpowiedzi i rozwiązania

Zestaw zadań: [`problem-set-01.md`](problem-set-01.md) — zadania 1–6, wszystkie punkty.
Wersja w **czystym Markdown** (bez dyrektyw MyST/Sphinx), matematyka w LaTeX-u.

Wersja PDF (z generowanym spisem treści): [`problem-set-01-odpowiedzi.pdf`](problem-set-01-odpowiedzi.pdf) —
buduje ją skrypt `./build-odpowiedzi-pdf.sh` (pandoc → typst → PDF).

**Konwencje przyjęte w rozwiązaniach**

- $\log$ bez podstawy to $\log_{10}$ (konwencja szkolna), $\log_a$ to logarytm o podstawie $a$.
- $D_f$ — dziedzina, $R_f$ — zbiór wartości.
- $t^t$ i $a^t$ dla wykładnika rzeczywistego wymagają $a>0$; $\log_a b$ wymaga $a>0$, $a\neq 1$, $b>0$.
- Zapis „funkcja maleje na $(-\infty,-2)$ i na $(-2,\infty)$” znaczy: maleje **na każdym z tych przedziałów osobno** (nie na ich sumie).

---

## Zadanie 1

$$f(x)=x^x+\log_x\left(1+2\sqrt x+3x^2\right).$$

### Dziedzina funkcji $f$

- $x^x$ dla rzeczywistego wykładnika: potrzeba $x>0$;
- podstawa logarytmu: $x>0$, $x\neq 1$;
- liczba logarytmowana: $1+2\sqrt x+3x^2>0$ — spełnione automatycznie dla $x\ge 0$ (składniki nieujemne plus jedynka), a $\sqrt x$ i tak wymaga $x\ge 0$.

$$D_f=(0,1)\cup(1,\infty).$$

Wyrażenia $f(-x)$, $f(1/x)$, $f(\sqrt x)$, $f(x^2)$ to złożenia $x\mapsto f(t)$ z $t=-x,\ \tfrac1x,\ \sqrt x,\ x^2$.
Wystarczy więc nałożyć warunki $t>0$ i $t\neq 1$ (bo $t\in D_f$) oraz własne warunki „wewnętrznej” funkcji $t=g(x)$.

### 1. $f(-x)$, czyli $t=-x$

$$x<0 \quad (\text{bo } -x>0), \qquad x\neq -1 \quad (\text{bo } -x\neq 1),\qquad \sqrt{-x}\ \Rightarrow\ x\le 0.$$

$$\boxed{\;D_{f(-x)}=(-\infty,-1)\cup(-1,0)\;}$$

$$f(-x)=(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3x^2\right).$$

> **Uwaga.** To wyrażenie **istnieje** — dla $x<0$ liczymy po prostu wartość $f$ w punkcie dodatnim $-x$. Podstawa $-x$ jest dodatnia, więc $(-x)^{-x}$ też jest dobrze określone.

### 2. $f\left(\tfrac1x\right)$, czyli $t=\tfrac1x$

$$\frac1x>0\iff x>0,\qquad \frac1x\neq 1\iff x\neq 1 .$$

$$\boxed{\;D=(0,1)\cup(1,\infty)\;}$$

$$f\left(\frac1x\right)=\left(\frac1x\right)^{1/x}+\log_{1/x}\left(1+\frac{2}{\sqrt x}+\frac{3}{x^2}\right),\qquad \text{bo } \sqrt{\frac1x}=\frac1{\sqrt x}\ \ (x>0).$$

### 3. $f(\sqrt x)$, czyli $t=\sqrt x$

$$\sqrt x>0\iff x>0,\qquad \sqrt x\neq 1\iff x\neq 1,\qquad \sqrt{\sqrt x}=x^{1/4}.$$

$$\boxed{\;D=(0,1)\cup(1,\infty)\;}$$

$$f(\sqrt x)=(\sqrt x)^{\sqrt x}+\log_{\sqrt x}\left(1+2x^{1/4}+3x\right).$$

### 4. $f(x^2)$, czyli $t=x^2$

$$x^2>0\iff x\neq 0,\qquad x^2\neq 1\iff x\neq \pm1,\qquad \sqrt{x^2}=|x|.$$

$$\boxed{\;D_{f(x^2)}=\mathbb R\setminus\{-1,0,1\}\;}$$

$$f(x^2)=(x^2)^{x^2}+\log_{x^2}\left(1+2|x|+3x^4\right).$$

---

## Zadanie 2

### 2.1. $f(x)=\dfrac{x^2-3x+2}{4-x^2}$

**Uproszczenie.**

$$x^2-3x+2=(x-1)(x-2),\qquad 4-x^2=-(x-2)(x+2),$$

$$\frac{(x-1)(x-2)}{-(x-2)(x+2)}=-\frac{x-1}{x+2}=-1+\frac{3}{x+2}\qquad (x\neq 2).$$

**Dziedzina.** $4-x^2\neq0\Rightarrow x\neq\pm2$:

$$\boxed{\;D_f=\mathbb R\setminus\{-2,2\}\;}$$

**Zbiór wartości.** Funkcja $y=-1+\dfrac{3}{x+2}$ przyjmuje wszystkie wartości poza $-1$ (asymptota pozioma). Dodatkowo punkt $x=2$ wypada z dziedziny, a pomijana wartość to

$$-1+\frac{3}{2+2}=-\frac14 .$$

Tej wartości nie da się już osiągnąć (równanie $-\frac{x-1}{x+2}=-\frac14$ daje $x=2$, które nie należy do dziedziny).

$$\boxed{\;R_f=\mathbb R\setminus\left\{-1,-\tfrac14\right\}\;}$$

**Monotoniczność.** $f'(x)=-\dfrac{3}{(x+2)^2}<0$ dla $x\neq-2$: funkcja **maleje** na każdym z przedziałów $(-\infty,-2)$, $(-2,2)$, $(2,\infty)$.

**Wykres.** Hiperbola $y=-1+\frac{3}{x+2}$: asymptoty $x=-2$ i $y=-1$; miejsce zerowe $x=1$; $f(0)=\frac12$; **„dziura”** (punkt usunięty) w $\left(2,-\frac14\right)$. Przechodzi przez $(1,0)$ i $\left(0,\frac12\right)$.

### 2.2. $f(x)=\dfrac{\log_{\sqrt2}\frac12-\log_3 x}{\log_3(9x)}\cdot\left(x^2-x-2\right)$

**Uproszczenie.** $\left(\sqrt2\right)^{-2}=\frac12$, więc $\log_{\sqrt2}\frac12=-2$. Dalej $\log_3(9x)=\log_3 9+\log_3 x=2+\log_3 x$. Licznik:

$$-2-\log_3 x=-\left(2+\log_3 x\right),$$

czyli **ułamek jest stały i równy $-1$** (tam, gdzie jest określony). Zatem

$$f(x)=-1\cdot\left(x^2-x-2\right)=-x^2+x+2=-\left(x-\tfrac12\right)^2+\tfrac94 .$$

**Dziedzina.** $x>0$ oraz $\log_3(9x)\neq0\iff 9x\neq1\iff x\neq\frac19$:

$$\boxed{\;D_f=\left(0,\tfrac19\right)\cup\left(\tfrac19,\infty\right)\;}$$

**Zbiór wartości.** Na $(0,\infty)$ parabola $g(x)=-x^2+x+2$ ma wierzchołek $\left(\frac12,\frac94\right)$ (ramiona w dół) i spełnia $g(0^+)\to2$, $g(x)\to-\infty$. Zbiór wartości na $(0,\infty)$ to $\left(-\infty,\frac94\right]$.

Punkt $x=\frac19$ wypada z dziedziny i odpowiada mu wartość $g\left(\frac19\right)=\frac{170}{81}\approx2{,}099$. Ale równanie $g(x)=\frac{170}{81}$ ma dwa pierwiastki: $x=\frac19$ oraz $x=\frac89$ — a $\frac89$ **należy** do dziedziny. Dziura nie zabiera więc nic ze zbioru wartości:

$$\boxed{\;R_f=\left(-\infty,\tfrac94\right]\;}$$

**Monotoniczność.** $f$ **rośnie** na $\left(0,\frac12\right)$ i **maleje** na $\left(\frac12,\infty\right)$ (osobno na obu kawałkach dziedziny oddzielonych dziurą).

**Wykres.** Prawa gałąź paraboli z ramionami w dół, z „dziurą” w $\left(\frac19,\frac{170}{81}\right)$; wierzchołek $\left(\frac12,\frac94\right)$; miejsce zerowe $x=2$ (drugie, $x=-1$, leży poza dziedziną); $\lim_{x\to0^+}f(x)=2$.

---

## Zadanie 3

### 3.1. $(1-x)(2-x)^2(x+3)^3<0$

Pierwiastki: $x=1$ (krotność 1 — zmiana znaku), $x=2$ (krotność 2 — **bez** zmiany znaku), $x=-3$ (krotność 3 — zmiana znaku). Najstarszy wyraz: $-x^6$, czyli dla dużych $|x|$ wyrażenie jest ujemne.

| przedział | $(-\infty,-3)$ | $(-3,1)$ | $(1,2)$ | $(2,\infty)$ |
|---|---|---|---|---|
| znak | $-$ | $+$ | $-$ | $-$ |

$$\boxed{\;x\in(-\infty,-3)\cup(1,2)\cup(2,\infty)\;}$$

### 3.2. $\dfrac{(x+3)^3}{(x^2-1)(x+1)}\ge0$

Mianownik: $(x^2-1)(x+1)=(x-1)(x+1)^2$, a $(x+1)^2>0$ dla $x\neq-1$. Znak ilorazu wyznacza więc $\dfrac{(x+3)^3}{x-1}$, a wyrażenie jest nieokreślone dla $x=-1$ oraz $x=1$.

- $x\in(-\infty,-3)$: $(-)\big/(-) \Rightarrow +$;
- $x=-3$: licznik $=0$, mianownik $=-16\neq0$ → wartość $0$, warunek $\ge0$ spełniony;
- $x\in(-3,-1)\cup(-1,1)$: $(-)$;
- $x=1$: mianownik $=0$ — nie należy;
- $x\in(1,\infty)$: $(+)$.

$$\boxed{\;x\in(-\infty,-3]\cup(1,\infty)\;}$$

### 3.3. $3\log(x+1)=\log\left(1-x^2\right)$

**Dziedzina:** $x+1>0$ i $1-x^2>0$, czyli $x\in(-1,1)$.

Korzystamy z $3\log(x+1)=\log(x+1)^3$ (wolno, bo $x+1>0$):

$$(x+1)^3=1-x^2\ \Longrightarrow\ x^3+3x^2+3x+1+x^2-1=0\ \Longrightarrow\ x^3+4x^2+3x=0,$$

$$x\left(x^2+4x+3\right)=x(x+1)(x+3)=0\ \Longrightarrow\ x\in\{0,-1,-3\}.$$

Z tych liczb w dziedzinie $(-1,1)$ leży tylko $x=0$. ($-1$ i $-3$ odrzucamy — nie należą do dziedziny.)

$$\boxed{\;x=0\;}$$

### 3.4. $\dfrac{x^2-x}{\log_2 x-1}\le0$

**Dziedzina:** $x>0$ i $\log_2 x\neq1\Rightarrow x\neq2$, czyli $x\in(0,2)\cup(2,\infty)$.

Licznik: $x^2-x=x(x-1)$, dla $x>0$ ma znak $x-1$; zero w $x=1$. Mianownik: $\log_2x-1>0\iff x>2$.

| przedział | $(0,1)$ | $1$ | $(1,2)$ | $(2,\infty)$ |
|---|---|---|---|---|
| znak | $+$ | $0$ | $-$ | $+$ |

W $x=1$ licznik się zeruje, a mianownik jest różny od zera, więc $x=1$ wchodzi do zbioru rozwiązań.

$$\boxed{\;x\in[1,2)\;}$$

### 3.5. $2^{|x|-1}\le\left(\dfrac12\right)^{|x|}$

$$\left(\frac12\right)^{|x|}=2^{-|x|},\qquad 2^{|x|-1}\le2^{-|x|}\iff |x|-1\le-|x|\iff 2|x|\le1\iff |x|\le\frac12 .$$

(nierówność dla $2^t$ jest równoważna nierówności wykładników, bo podstawa $2>1$)

$$\boxed{\;x\in\left[-\tfrac12,\tfrac12\right]\;}$$

---

## Zadanie 4

$$f(x)=\frac{1+2x}{x-x^2}+\sin\left(x^{-1}+\sqrt x\right).$$

### Dziedzina funkcji $f$

$$x-x^2=x(1-x)\neq0\Rightarrow x\neq0,\ x\neq1;\qquad \frac1x\Rightarrow x\neq0;\qquad \sqrt x\Rightarrow x\ge0 .$$

$$D_f=(0,1)\cup(1,\infty).$$

### 1. $f(-x)$

Warunki: $-x>0$, $-x\neq1$, $\sqrt{-x}$ ($x\le0$):

$$\boxed{\;D=(-\infty,-1)\cup(-1,0)\;}$$

$$f(-x)=\frac{1-2x}{-x-x^2}+\sin\left(-\frac1x+\sqrt{-x}\right)=\frac{2x-1}{x^2+x}+\sin\left(-\frac1x+\sqrt{-x}\right).$$

### 2. $f\left(\tfrac1x\right)$

Warunki: $\tfrac1x>0\Rightarrow x>0$, $\tfrac1x\neq1\Rightarrow x\neq1$ (mianownik $\tfrac1x-\tfrac1{x^2}=\tfrac{x-1}{x^2}\neq0$ daje to samo):

$$\boxed{\;D=(0,1)\cup(1,\infty)\;}$$

$$\frac{1+\frac2x}{\frac1x-\frac1{x^2}}=\frac{\frac{x+2}{x}}{\frac{x-1}{x^2}}=\frac{x(x+2)}{x-1},$$

$$f\left(\frac1x\right)=\frac{x(x+2)}{x-1}+\sin\left(x+\frac1{\sqrt x}\right).$$

### 3. $f(\sqrt x)$

Warunki: $\sqrt x>0\Rightarrow x>0$, $\sqrt x\neq1\Rightarrow x\neq1$:

$$\boxed{\;D=(0,1)\cup(1,\infty)\;}$$

$$f(\sqrt x)=\frac{1+2\sqrt x}{\sqrt x-x}+\sin\left(x^{-1/2}+x^{1/4}\right).$$

### 4. $f(x^2)$

Warunki: $x^2>0\Rightarrow x\neq0$, $x^2\neq1\Rightarrow x\neq\pm1$, oraz $\sqrt{x^2}=|x|$:

$$\boxed{\;D=\mathbb R\setminus\{-1,0,1\}\;}$$

$$f(x^2)=\frac{1+2x^2}{x^2-x^4}+\sin\left(\frac1{x^2}+|x|\right).$$

> **Uwaga.** Sinus przyjmuje każdą liczbę rzeczywistą, więc nie nakłada żadnych dodatkowych warunków — wszystkie ograniczenia pochodzą od mianownika, $x^{-1}$ i $\sqrt x$.

---

## Zadanie 5

### 5.1. $f(x)=\dfrac1{\sqrt{x^2-2x+1}}$

$$x^2-2x+1=(x-1)^2>0\iff x\neq1,\qquad f(x)=\frac1{\sqrt{(x-1)^2}}=\frac1{|x-1|}.$$

$$\boxed{\;D_f=\mathbb R\setminus\{1\},\qquad R_f=(0,\infty)\;}$$

**Monotoniczność:** maleje na $(-\infty,1)$, rośnie na $(1,\infty)$.

**Wykres:** wykres $y=\frac1{|x|}$ przesunięty o $1$ w prawo; asymptoty: pionowa $x=1$, pozioma $y=0$; ramiona biegną do $+\infty$ przy $x\to1^{\pm}$ i do $0$ przy $x\to\pm\infty$.

### 5.2. $f(x)=\dfrac{x^2+x+6}{2\log_5(x+1)}\cdot\log_5\left(x^2+2x+1\right)$

$$\log_5\left(x^2+2x+1\right)=\log_5(x+1)^2=2\log_5(x+1)\qquad (x+1>0),$$

$$f(x)=\frac{x^2+x+6}{2\log_5(x+1)}\cdot 2\log_5(x+1)=x^2+x+6 .$$

**Dziedzina:** $x+1>0\Rightarrow x>-1$ oraz $\log_5(x+1)\neq0\Rightarrow x+1\neq1\Rightarrow x\neq0$:

$$\boxed{\;D_f=(-1,0)\cup(0,\infty),\qquad f(x)=x^2+x+6\;}$$

**Zbiór wartości.** Wierzchołek paraboli $x=-\frac12$, wartość $f\left(-\frac12\right)=\frac{23}{4}$.

- na $(-1,0)$: wartości od $\frac{23}{4}$ (w $x=-\frac12$, osiągane) do $6$ ($x=-1$, $x=0$ — **nieosiągane**, krańce przedziału otwarte) → $\left[\frac{23}{4},6\right)$;
- na $(0,\infty)$: wartości $>6$, wszystkie → $(6,\infty)$.

$$\boxed{\;R_f=\left[\tfrac{23}{4},6\right)\cup(6,\infty)\;}$$

> **Uwaga.** Wartość $6$ **nie jest przyjmowana**: równanie $x^2+x+6=6$, czyli $x(x+1)=0$, ma pierwiastki $x=0$ (dziura) i $x=-1$ (poza dziedziną).

**Monotoniczność:** maleje na $\left(-1,-\frac12\right)$; rośnie na $\left(-\frac12,0\right)$ i na $(0,\infty)$ (można to złączyć: rośnie na $\left(-\frac12,\infty\right)\setminus\{0\}$).

**Wykres:** gałąź paraboli z ramionami w górę dla $x>-1$, wierzchołek $\left(-\frac12,\frac{23}{4}\right)$, „dziura” w $(0,6)$, zera poza dziedziną.

---

## Zadanie 6

### 6.1. $\sqrt{x+4}>x-8$

**Dziedzina:** $x\ge-4$.

**Przypadek 1: $x<8$.** Wtedy $x-8<0\le\sqrt{x+4}$, więc nierówność jest spełniona automatycznie: $x\in[-4,8)$.

**Przypadek 2: $x\ge8$.** Obie strony są nieujemne, wolno podnieść do kwadratu:

$$x+4>(x-8)^2\iff x+4>x^2-16x+64\iff x^2-17x+60<0\iff (x-5)(x-12)<0,$$

czyli $x\in(5,12)$; z warunkiem $x\ge8$ daje to $x\in[8,12)$.

$$\boxed{\;x\in[-4,12)\;}$$

> **Uwaga.** Podniesienie do kwadratu bez rozbicia na przypadki daje tylko $x\in(5,12)$ i **gubi** rozwiązania z przedziału $[-4,5]$, gdzie prawa strona jest ujemna.

### 6.2. $\sqrt{x+5}=5-\sqrt{x+10}$

**Dziedzina:** $x\ge-5$; dodatkowo prawa strona musi być nieujemna: $5-\sqrt{x+10}\ge0\Rightarrow x\le15$.

$$x+5=25-10\sqrt{x+10}+x+10\ \Longrightarrow\ 10\sqrt{x+10}=30\ \Longrightarrow\ \sqrt{x+10}=3\ \Longrightarrow\ x=-1 .$$

Sprawdzenie: $\sqrt4=2$ oraz $5-\sqrt9=5-3=2$ — zgadza się; $-1\in[-5,15]$.

$$\boxed{\;x=-1\;}$$

### 6.3. $(1-x)^{-1}(2-x)^{-2}(x-3)\ge0$

$$\frac{x-3}{(1-x)(2-x)^2}\ge0,\qquad (2-x)^2>0\ \text{dla}\ x\neq2 .$$

Znak wyznacza więc $\dfrac{x-3}{1-x}$; wyrażenie nieokreślone dla $x=1$ i $x=2$.

| przedział | $(-\infty,1)$ | $1$ | $(1,2)$ | $(2,3)$ | $3$ | $(3,\infty)$ |
|---|---|---|---|---|---|---|
| znak | $-$ | nieokr. | $+$ | $+$ | $0$ | $-$ |

W $x=3$ licznik się zeruje, a mianownik jest różny od zera.

$$\boxed{\;x\in(1,3]\;}$$

### 6.4. $\log_3(x+1)+\log_{\sqrt3}(x+1)+\log_{1/3}(x+1)=6$

**Dziedzina:** $x+1>0\Rightarrow x>-1$. Niech $t=\log_3(x+1)$ i zamieńmy podstawy:

$$\log_{\sqrt3}(x+1)=\frac{t}{\log_3\sqrt3}=\frac{t}{\frac12}=2t,\qquad \log_{1/3}(x+1)=\frac{t}{\log_3\frac13}=\frac{t}{-1}=-t .$$

$$t+2t-t=2t=6\ \Longrightarrow\ t=3\ \Longrightarrow\ x+1=3^3=27\ \Longrightarrow\ x=26 .$$

$$\boxed{\;x=26\;}$$

### 6.5. $(\log x-1)(\log x-10)(x+2)\le0$

**Dziedzina:** $x>0$, więc $x+2>0$ i czynnik $(x+2)$ nie wpływa na znak. Zostaje

$$(\log x-1)(\log x-10)\le0\iff 1\le\log x\le10\iff 10^1\le x\le10^{10}.$$

$$\boxed{\;x\in\left[10,\ 10^{10}\right]\;}$$

### 6.6. $\dfrac{\log_2x-1}{x^2-x}\le0$

**Dziedzina:** $x>0$ i $x\neq1$. Licznik zeruje się w $x=2$; mianownik $x(x-1)$ ma znak: ujemny na $(0,1)$, dodatni na $(1,\infty)$.

- $(0,1)$: $\log_2x-1<0$ i mianownik $<0$ → iloraz $>0$ — odrzucamy;
- $(1,2)$: licznik $<0$, mianownik $>0$ → OK;
- $x=2$: licznik $=0$, mianownik $=2\neq0$ → OK;
- $(2,\infty)$: oba dodatnie → $>0$ — odrzucamy.

$$\boxed{\;x\in(1,2]\;}$$

> **Uwaga.** Porównaj z 3.4 — to odwrócenie licznika i mianownika: odpowiedzi „zamieniają się końcami”, $\ (1,2]$ wobec $[1,2)$. Domknięcie zawsze idzie za miejscem zerowym **licznika**.

### 6.7. $\left(2^{|x+2|}\right)^2-4\cdot2^{1-x}<0$

$$\left(2^{|x+2|}\right)^2=2^{2|x+2|},\qquad 4\cdot2^{1-x}=2^2\cdot2^{1-x}=2^{3-x},$$

$$2^{2|x+2|}<2^{3-x}\iff 2|x+2|<3-x .$$

**Przypadek 1: $x\ge-2$.** $\ 2(x+2)<3-x\iff 3x<-1\iff x<-\frac13$, czyli $x\in\left[-2,-\frac13\right)$.

**Przypadek 2: $x<-2$.** $\ -2(x+2)<3-x\iff -2x-4<3-x\iff x>-7$, czyli $x\in(-7,-2)$.

$$\boxed{\;x\in\left(-7,-\tfrac13\right)\;}$$

> **Uwaga.** Krańce są otwarte: dla $x=-7$ i dla $x=-\frac13$ obie strony są **równe** ($2^{10}=4\cdot2^{8}$, $\ 2^{10/3}=4\cdot2^{4/3}$), a nierówność jest ostra.

---

## Ściągawka — same odpowiedzi

| # | Odpowiedź |
|---|---|
| 1 | $f(-x)=(-x)^{-x}+\log_{-x}\left(1+2\sqrt{-x}+3x^2\right)$, $D=(-\infty,-1)\cup(-1,0)$; $f\left(\frac1x\right)=\left(\frac1x\right)^{1/x}+\log_{1/x}\left(1+\frac2{\sqrt x}+\frac3{x^2}\right)$, $D=(0,1)\cup(1,\infty)$; $f(\sqrt x)=(\sqrt x)^{\sqrt x}+\log_{\sqrt x}\left(1+2x^{1/4}+3x\right)$, $D=(0,1)\cup(1,\infty)$; $f(x^2)=(x^2)^{x^2}+\log_{x^2}\left(1+2\lvert x\rvert+3x^4\right)$, $D=\mathbb R\setminus\{-1,0,1\}$ |
| 2.1 | $f(x)=-\frac{x-1}{x+2}=-1+\frac3{x+2}$; $D_f=\mathbb R\setminus\{-2,2\}$; $R_f=\mathbb R\setminus\left\{-1,-\frac14\right\}$; maleje na $(-\infty,-2),(-2,2),(2,\infty)$; asymptoty $x=-2,\ y=-1$; dziura $\left(2,-\frac14\right)$ |
| 2.2 | $f(x)=-x^2+x+2$; $D_f=\left(0,\frac19\right)\cup\left(\frac19,\infty\right)$; $R_f=\left(-\infty,\frac94\right]$; rośnie na $\left(0,\frac12\right)$, maleje na $\left(\frac12,\infty\right)$; dziura $\left(\frac19,\frac{170}{81}\right)$ |
| 3.1 | $(-\infty,-3)\cup(1,2)\cup(2,\infty)$ |
| 3.2 | $(-\infty,-3]\cup(1,\infty)$ |
| 3.3 | $x=0$ |
| 3.4 | $[1,2)$ |
| 3.5 | $\left[-\frac12,\frac12\right]$ |
| 4 | $f(-x)=\frac{2x-1}{x^2+x}+\sin\left(-\frac1x+\sqrt{-x}\right)$, $D=(-\infty,-1)\cup(-1,0)$; $f\left(\frac1x\right)=\frac{x(x+2)}{x-1}+\sin\left(x+\frac1{\sqrt x}\right)$, $D=(0,1)\cup(1,\infty)$; $f(\sqrt x)=\frac{1+2\sqrt x}{\sqrt x-x}+\sin\left(x^{-1/2}+x^{1/4}\right)$, $D=(0,1)\cup(1,\infty)$; $f(x^2)=\frac{1+2x^2}{x^2-x^4}+\sin\left(\frac1{x^2}+\lvert x\rvert\right)$, $D=\mathbb R\setminus\{-1,0,1\}$ |
| 5.1 | $f(x)=\frac1{\lvert x-1\rvert}$; $D_f=\mathbb R\setminus\{1\}$; $R_f=(0,\infty)$; maleje na $(-\infty,1)$, rośnie na $(1,\infty)$ |
| 5.2 | $f(x)=x^2+x+6$; $D_f=(-1,0)\cup(0,\infty)$; $R_f=\left[\frac{23}{4},6\right)\cup(6,\infty)$; maleje na $\left(-1,-\frac12\right)$, rośnie na $\left(-\frac12,0\right)$ i $(0,\infty)$; dziura $(0,6)$ |
| 6.1 | $[-4,12)$ |
| 6.2 | $x=-1$ |
| 6.3 | $(1,3]$ |
| 6.4 | $x=26$ |
| 6.5 | $\left[10,10^{10}\right]$ |
| 6.6 | $(1,2]$ |
| 6.7 | $\left(-7,-\frac13\right)$ |
