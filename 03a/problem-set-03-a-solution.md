# Granica ciągów liczbowych — rozwiązania (zestaw 03a)

Zestaw zadań: [`problem-set-03-a.md`](problem-set-03-a.md) — zadania 1–5 (zadania 1–2 na zajęcia, 3–5 domowe).

Skrypt sprawdzający liczbowo wszystkie granice: [`../03/scripts/check_set03.py`](../03/scripts/check_set03.py) (opis w [`../03/scripts/README.md`](../03/scripts/README.md)). Skrypt nie jest częścią rozwiązania.

**Oznaczenia.** $\lim$ oznacza $\lim_{n\to\infty}$. $\mathbb{N}=\{1,2,3,\dots\}$.

**Narzędzia, z których korzystamy.**

- Granica sumy, różnicy, iloczynu i ilorazu ciągów zbieżnych (iloraz tylko gdy granica mianownika jest różna od zera).
- Twierdzenie o trzech ciągach (ściskanie): jeśli $a_n\le b_n\le c_n$ dla dużych $n$ oraz $a_n\to g$, $c_n\to g$, to $b_n\to g$.
- $\sqrt[n]{n}\to1$ oraz $\sqrt[n]{c}\to1$ dla stałej $c\gt 0$.
- $\left(1+\frac1n\right)^n\to e$.
- **Lemat A.** Jeśli $c_n\to0$ i $c_n\neq0$, to $\dfrac{\ln(1+c_n)}{c_n}\to1$.
- **Lemat B.** Jeśli $c_n\to0$, $c_n\neq0$ i $d_nc_n\to L$, to $(1+c_n)^{d_n}\to e^{L}$.
  *Dowód.* $(1+c_n)^{d_n}=\exp\left(d_nc_n\cdot\frac{\ln(1+c_n)}{c_n}\right)$, a $d_nc_n\cdot\frac{\ln(1+c_n)}{c_n}\to L\cdot1=L$; następnie stosujemy ciągłość $\exp$.

---

## Zadanie 1 (na zajęcia)

### 1.1. $\lim \left(5n^2-n\arctan n\right)$

Dla każdego $n$ mamy $0\lt \arctan n\lt \dfrac{\pi}{2}$, więc

$$
5n^2-n\arctan n\ \ge\ 5n^2-\frac{\pi}{2}n=n\left(5n-\frac{\pi}{2}\right)\ \to\ +\infty.
$$

**Wynik:** $+\infty$.

### 1.2. $\lim \dfrac{\left(n+\frac1n\right)^8}{\left[C(n+2,n)\right]^5}\cdot\left(1+2+\dots+n\right)$

Liczymy każdy czynnik:

- $C(n+2,n)=\dfrac{(n+2)(n+1)}{2}$,
- $1+2+\dots+n=\dfrac{n(n+1)}{2}$,
- $\left(n+\frac1n\right)^8=\dfrac{(n^2+1)^8}{n^8}$.

Zatem wyrażenie równa się

$$
\frac{(n^2+1)^8}{n^8}\cdot\frac{n(n+1)}{2}\cdot\frac{2^5}{(n+1)^5(n+2)^5}
=\frac{16 (n^2+1)^8}{n^7 (n+1)^4 (n+2)^5}.
$$

Licznik i mianownik są wielomianami stopnia $16$ o współczynnikach wiodących $16\cdot1$ i $1$. Dzieląc przez $n^{16}$ dostajemy granicę $\dfrac{16}{1}=16$.

**Wynik:** $16$.

### 1.3. $\lim \dfrac{2^n+3^n}{4^n+3^n}$

Dzielimy licznik i mianownik przez $4^n$:

$$
\frac{\left(\frac12\right)^n+\left(\frac34\right)^n}{1+\left(\frac34\right)^n}\ \to\ \frac{0+0}{1+0}=0,
$$
bo $\left|\frac12\right|\lt 1$ i $\left|\frac34\right|\lt 1$.

**Wynik:** $0$.

### 1.4. $\lim \dfrac{4^n+2^n}{2^{2n+1}+4^{n+1}+3^n}$

Mamy $2^{2n+1}=2\cdot4^n$, $4^{n+1}=4\cdot4^n$, $3^n=\left(\frac34\right)^n4^n$. Dzielimy przez $4^n$:

$$
\frac{1+\left(\frac12\right)^n}{2+4+\left(\frac34\right)^n}\ \to\ \frac{1}{6}.
$$

**Wynik:** $\dfrac16$.

### 1.5. $\lim \left(\sqrt{n^2+5n}-\sqrt{n^2-n}\right)$

Mnożymy przez sprzężenie:

$$
\sqrt{n^2+5n}-\sqrt{n^2-n}=\frac{(n^2+5n)-(n^2-n)}{\sqrt{n^2+5n}+\sqrt{n^2-n}}=\frac{6n}{\sqrt{n^2+5n}+\sqrt{n^2-n}}.
$$
Dzielimy licznik i mianownik przez $n$:

$$
\frac{6}{\sqrt{1+\frac5n}+\sqrt{1-\frac1n}}\ \to\ \frac{6}{2}=3.
$$

**Wynik:** $3$.

### 1.6. $\lim \dfrac{\sqrt{n^2+5}-n}{\sqrt{n^2+2}-n}$

Mnożymy licznik i mianownik każdego ułamka przez sprzężenie:

$$
\sqrt{n^2+5}-n=\frac{5}{\sqrt{n^2+5}+n},  \sqrt{n^2+2}-n=\frac{2}{\sqrt{n^2+2}+n}.
$$
Zatem

$$
\frac{\sqrt{n^2+5}-n}{\sqrt{n^2+2}-n}=\frac52\cdot\frac{\sqrt{n^2+2}+n}{\sqrt{n^2+5}+n}
=\frac52\cdot\frac{\sqrt{1+\frac{2}{n^2}}+1}{\sqrt{1+\frac{5}{n^2}}+1}\ \to\ \frac52\cdot\frac{2}{2}=\frac52.
$$

**Wynik:** $\dfrac52$.

---

## Zadanie 2 (na zajęcia)

### 2.1. $\lim \dfrac{\cos(n!)}{n+\arcsin\frac1n}$

- Dla każdego $n\ge1$ mamy $|\cos(n!)|\le1$.
- Ponieważ $\arcsin\frac1n\ge0$ dla $n\ge1$, mianownik spełnia $n+\arcsin\frac1n\ge n\gt 0$.

Stąd

$$
\left|\frac{\cos(n!)}{n+\arcsin\frac1n}\right|\le\frac1n\ \to\ 0,
$$
i z twierdzenia o trzech ciągach granica równa się $0$. (Nie wolno tu napisać „$\cos(n!)$ nie ma granicy, więc nie ma granicy ilorazu”: ciąg $\cos(n!)$ jest ograniczony, a mianownik rośnie do $\infty$.)

**Wynik:** $0$.

### 2.2. $\lim \sqrt[n]{4^n+n^{13}\cdot3^n}$

Ponieważ $3^n\le4^n$, mamy

$$
4^n\ \le\ 4^n+n^{13}3^n\ \le\ 4^n+n^{13}4^n=(1+n^{13}) 4^n.
$$
Pierwiastkujemy stopnia $n$ (funkcja $t\mapsto\sqrt[n]t$ jest rosnąca dla $t\gt 0$):

$$
4\ \le\ \sqrt[n]{4^n+n^{13}3^n}\ \le\ 4\sqrt[n]{1+n^{13}}.
$$
Dla $n\ge1$ mamy $1\le1+n^{13}\le2n^{13}$, więc

$$
1\le\sqrt[n]{1+n^{13}}\le\sqrt[n]{2} \left(\sqrt[n]{n}\right)^{13}\to1\cdot1^{13}=1.
$$
Zatem $\sqrt[n]{1+n^{13}}\to1$, a z twierdzenia o trzech ciągach granica równa się $4$.

**Wynik:** $4$.

### 2.3. $\lim \dfrac{n+2022}{3n-(-1)^n}$

Dzielimy licznik i mianownik przez $n$:

$$
\frac{1+\frac{2022}{n}}{3-\frac{(-1)^n}{n}}.
$$
Mamy $\left|\frac{(-1)^n}{n}\right|\le\frac1n\to0$, więc mianownik zbiega do $3\neq0$. Z twierdzeń o granicy ilorazu:

$$
\frac{1+0}{3-0}=\frac13.
$$

**Wynik:** $\dfrac13$.

### 2.4. $\lim \sqrt[\frac1n]{\dfrac{n+2}{n+1}}+\left(\dfrac{n+1}{n}\right)^{2022}$

Pierwiastek stopnia $\frac1n$ to potęgowanie do potęgi $n$: $\sqrt[1/n]{x}=x^n$. Zatem pierwszy składnik to

$$
\left(\frac{n+2}{n+1}\right)^n=\left(1+\frac{1}{n+1}\right)^n=\frac{\left(1+\frac{1}{n+1}\right)^{n+1}}{1+\frac{1}{n+1}}.
$$
Z $\left(1+\frac1m\right)^m\to e$ (przy $m=n+1$) licznik zbiega do $e$, a mianownik do $1$. Zatem pierwszy składnik $\to e$.

Drugi składnik: $\left(\frac{n+1}{n}\right)^{2022}=\left(1+\frac1n\right)^{2022}\to1^{2022}=1$.

Suma daje granicę $e+1$.

**Wynik:** $e+1$.

### 2.5. $\lim \left(\dfrac{1-n^2}{5-2n}\right)^{n+1}\cdot\left(\dfrac{2}{n+1}\right)^{n+1}$

Ponieważ obie potęgi mają ten sam wykładnik $n+1$, łączymy podstawy:

$$
\frac{1-n^2}{5-2n}\cdot\frac{2}{n+1}=\frac{2(1-n)(1+n)}{(5-2n)(n+1)}=\frac{2(1-n)}{5-2n}=\frac{2(n-1)}{2n-5}=1+\frac{3}{2n-5}.
$$
Zatem wyrażenie równa się $\left(1+c_n\right)^{d_n}$, gdzie

$$
c_n=\frac{3}{2n-5}\to0,  d_n=n+1,  d_nc_n=\frac{3(n+1)}{2n-5}\to\frac32.
$$
Z lematu B granica równa się $e^{3/2}$.

*Uwaga o założeniach.* Podstawa $\frac{1-n^2}{5-2n}\cdot\frac{2}{n+1}$ zbiega do $1$, a wykładnik do $\infty$, więc mamy symbol $1^\infty$. Osobno pierwszy czynnik zbiega do $+\infty$, a drugi do $0$ (symbol $\infty\cdot0$), więc iloczynu nie wolno liczyć jako iloczynu granic, tylko łącznie, jak wyżej.

**Wynik:** $e^{3/2}$.

### 2.6. $\lim \left(\dfrac{2n^2+2n+1}{2n^2+2}\right)^{n+1}$

Podstawa to

$$
\frac{2n^2+2n+1}{2n^2+2}=1+\frac{2n-1}{2n^2+2}=1+c_n,  c_n\to0.
$$
Wykładnik $d_n=n+1$ spełnia

$$
d_nc_n=\frac{(n+1)(2n-1)}{2n^2+2}\to\frac{2}{2}=1.
$$
Z lematu B granica równa się $e^{1}=e$.

**Wynik:** $e$.

---

## Zadanie 3 (domowe)

### 3.1. $\lim \dfrac{3n^3-\sqrt{n^3+4n^6}}{\left(\sqrt n-5n+383764\right)^3}$

Dzielimy licznik i mianownik przez $n^3$.

- $\dfrac{\sqrt{n^3+4n^6}}{n^3}=\sqrt{\dfrac{n^3+4n^6}{n^6}}=\sqrt{4+\dfrac{1}{n^3}}\to2$, więc licznik$/n^3\to3-2=1$.
- $\dfrac{\sqrt n-5n+383764}{n}=\dfrac{1}{\sqrt n}-5+\dfrac{383764}{n}\to-5$, więc mianownik$/n^3\to(-5)^3=-125$.

Stąd granica równa się $\dfrac{1}{-125}=-\dfrac{1}{125}$. (Stała $383764$ nie ma wpływu na granicę.)

**Wynik:** $-\dfrac{1}{125}$.

### 3.2. $\lim \left(\sqrt{4n^2+n}-2n\right)$

Mnożymy przez sprzężenie:

$$
\sqrt{4n^2+n}-2n=\frac{n}{\sqrt{4n^2+n}+2n}=\frac{1}{\sqrt{4+\frac1n}+2}\to\frac{1}{4}.
$$

**Wynik:** $\dfrac14$.

### 3.3. $\lim n\left(\sqrt{2n^2+1}-\sqrt{2n^2-1}\right)$

$$
n\left(\sqrt{2n^2+1}-\sqrt{2n^2-1}\right)=\frac{2n}{\sqrt{2n^2+1}+\sqrt{2n^2-1}}
=\frac{2}{\sqrt{2+\frac{1}{n^2}}+\sqrt{2-\frac{1}{n^2}}}\to\frac{2}{2\sqrt2}=\frac{1}{\sqrt2}.
$$

**Wynik:** $\dfrac{1}{\sqrt2}=\dfrac{\sqrt2}{2}$.

### 3.4. $\lim \dfrac{3^{n+1}+2^n}{5^n+4\cdot3^n}$

Dzielimy licznik i mianownik przez $5^n$. Mamy $3^{n+1}=3\cdot3^n$, więc

$$
\frac{3\left(\frac35\right)^n+\left(\frac25\right)^n}{1+4\left(\frac35\right)^n}\ \to\ \frac{0}{1}=0.
$$

**Wynik:** $0$.

### 3.5. $\lim \dfrac{4^n+5^n}{3\cdot4^n+2^n}$

Dzielimy przez $5^n$:

$$
\frac{\left(\frac45\right)^n+1}{3\left(\frac45\right)^n+\left(\frac25\right)^n}.
$$
Licznik zbiega do $1$. Mianownik jest dodatni dla każdego $n$ i zbiega do $0$. Zatem ułamek rośnie do $+\infty$ (przy dodatnim liczniku i dodatnim mianowniku zbiegającym do zera).

*Sprawdzenie:* dla $n=10$ wyrażenie wynosi około $3{,}1$, dla $n=20$ około $29$, a dla $n=100$ jest już rzędu $10^{9}$ (wzrost jak $\frac13\left(\frac54\right)^n$).

**Wynik:** $+\infty$.

### 3.6. $\lim \dfrac{3^{n-1}+(-2)^n}{3^{n+1}+(-2)^{n+2}}$

Ponieważ $(-2)^{n+2}=4\cdot(-2)^n$, dzielimy licznik i mianownik przez $3^n$:

$$
\frac{\frac13+\left(-\frac23\right)^n}{3+4\left(-\frac23\right)^n}.
$$
Ponieważ $\left|-\frac23\right|\lt 1$, mamy $\left(-\frac23\right)^n\to0$. Granica równa się $\dfrac{1/3}{3}=\dfrac19$.

**Wynik:** $\dfrac19$.

### 3.7. $\lim \dfrac{2^{3n}+5^{n+1}}{3^{2n+1}+4^{n-1}}$

Zapisujemy potęgi: $2^{3n}=8^n$, $5^{n+1}=5\cdot5^n$, $3^{2n+1}=3\cdot9^n$, $4^{n-1}=\frac14\cdot4^n$. Dzielimy przez $9^n$:

$$
\frac{\left(\frac89\right)^n+5\left(\frac59\right)^n}{3+\frac14\left(\frac49\right)^n}\ \to\ \frac{0}{3}=0.
$$

**Wynik:** $0$.

### 3.8. $\lim \dfrac{1+\frac12+\frac14+\dots+\frac{1}{2^n}}{1+\frac13+\frac19+\dots+\frac{1}{3^n}}$

Obie sumy są sumami ciągów geometrycznych o $n+1$ wyrazach: $1+q+q^2+\dots+q^n=\dfrac{1-q^{n+1}}{1-q}$ dla $q\neq1$.

- Licznik ($q=\frac12$): $\frac{1-\left(\frac12\right)^{n+1}}{\frac12}=2\left(1-\left(\frac12\right)^{n+1}\right)\to2$.
- Mianownik ($q=\frac13$): $\frac{1-\left(\frac13\right)^{n+1}}{\frac23}=\frac32\left(1-\left(\frac13\right)^{n+1}\right)\to\frac32$.

Stąd granica równa się $\dfrac{2}{3/2}=\dfrac43$.

**Wynik:** $\dfrac43$.

---

## Zadanie 4 (domowe)

Ten zestaw zadań ma założenia w treści: każde przejście wymaga sprawdzenia, że stosowane twierdzenie działa.

### 4.1. $\lim \dfrac{\cos(n!)}{n+\arcsin\frac1n}$

To samo zadanie co 2.1. Ponieważ $\left|\dfrac{\cos(n!)}{n+\arcsin\frac1n}\right|\le\dfrac1n\to0$, granica równa się $0$.

**Wynik:** $0$.

### 4.2. $\lim \dfrac{3n^2-1}{5n^2+\cos n}$

Dzielimy przez $n^2$:

$$
\frac{3-\frac{1}{n^2}}{5+\frac{\cos n}{n^2}}.
$$
Ponieważ $\left|\dfrac{\cos n}{n^2}\right|\le\dfrac{1}{n^2}\to0$, mianownik zbiega do $5\neq0$. Granica równa się $\dfrac35$.

**Wynik:** $\dfrac35$.

### 4.3. $\lim \dfrac{3n^2-n(-1)^n}{(\sqrt n-5)^4}$

Mianownik zapisujemy jako

$$
(\sqrt n-5)^4=\left(\sqrt n\right)^4\left(1-\frac{5}{\sqrt n}\right)^4=n^2\left(1-\frac{5}{\sqrt n}\right)^4.
$$
Dzielimy licznik i mianownik przez $n^2$:

$$
\frac{3-\frac{(-1)^n}{n}}{\left(1-\frac{5}{\sqrt n}\right)^4}\ \to\ \frac{3-0}{1}=3.
$$
(Zbieżność jest wolna, rzędu $\frac{1}{\sqrt n}$, więc dla $n=10^9$ wynik to dopiero około $3{,}0019$.)

**Wynik:** $3$.

### 4.4. $\lim \sqrt[n]{\dfrac{4^n}{n^{12}}+n\cdot3^n+5n^3}$

Oznaczmy $S_n=\dfrac{4^n}{n^{12}}+n\cdot3^n+5n^3$.

*Dolne oszacowanie.* $S_n\ge\dfrac{4^n}{n^{12}}$, więc

$$
\sqrt[n]{S_n}\ \ge\ \frac{4}{\left(\sqrt[n]{n}\right)^{12}}\to4.
$$

*Górne oszacowanie.* Dla $n\ge5$ mamy $5n^3\le4^n$. Dowód indukcyjny: dla $n=5$ jest $625\le1024$, a jeśli $5n^3\le4^n$, to $5(n+1)^3\le4\cdot5n^3\le4^{n+1}$, bo $(n+1)^3\le4n^3$ dla $n\ge5$. Ponadto $\dfrac{4^n}{n^{12}}\le4^n$ oraz $n\cdot3^n\le n\cdot4^n$. Zatem dla $n\ge5$

$$
S_n\le4^n+n4^n+4^n=(n+2)\cdot4^n
$$

stąd $\sqrt[n]{S_n}\le4\sqrt[n]{n+2}$.
Ponieważ $n+2\le3n$ dla $n\ge1$, mamy $\sqrt[n]{n+2}\le\sqrt[n]{3} \sqrt[n]{n}\to1$.

Z twierdzenia o trzech ciągach granica równa się $4$.

**Wynik:** $4$.

### 4.5. $\lim \left(\dfrac{7^n}{n^{13}}+n\right)^{1/n}$

Oznaczmy $S_n=\dfrac{7^n}{n^{13}}+n$.

- Dolne: $S_n\ge\dfrac{7^n}{n^{13}}$, więc $\sqrt[n]{S_n}\ge\dfrac{7}{\left(\sqrt[n]{n}\right)^{13}}\to7$.
- Górne: $n\le7^n$ oraz $\dfrac{7^n}{n^{13}}\le7^n$, więc $S_n\le2\cdot7^n$ i $\sqrt[n]{S_n}\le7\sqrt[n]{2}\to7$.

Z twierdzenia o trzech ciągach granica równa się $7$.

**Wynik:** $7$.

### 4.6. $\lim \left(\dfrac{n+1}{n}\right)^{2019}$

$\dfrac{n+1}{n}=1+\dfrac1n\to1$, a potęgowanie o stałym wykładniku jest ciągłe, więc granica równa się $1^{2019}=1$.

**Wynik:** $1$.

### 4.7. $\lim \left(\dfrac{2^n+4^n}{2^{2n}-2^n}\right)^{2^n}$

Ponieważ $2^{2n}=4^n$, dzielimy licznik i mianownik podstawy przez $4^n$. Niech $q_n=\left(\frac12\right)^n$. Wtedy $\frac{2^n}{4^n}=q_n$ i

$$
\frac{2^n+4^n}{4^n-2^n}=\frac{1+q_n}{1-q_n}=1+\frac{2q_n}{1-q_n}=1+c_n
$$

gdzie $c_n=\dfrac{2q_n}{1-q_n}\gt 0$ oraz $c_n\to0$.
Wykładnik to $d_n=2^n$, a

$$
d_nc_n=\frac{2\cdot2^n\cdot2^{-n}}{1-2^{-n}}=\frac{2}{1-2^{-n}}\to2.
$$
Z lematu B granica równa się $e^{2}$.

**Wynik:** $e^2$.

### 4.8. $\lim \left(\dfrac{3n}{4n+1}\right)^n\cdot\left(\dfrac{4n-3}{3n+2}\right)^n$

Wykładniki są równe ($n$), więc łączymy podstawy:

$$
\left(\frac{3n(4n-3)}{(4n+1)(3n+2)}\right)^n=\left(\frac{12n^2-9n}{12n^2+11n+2}\right)^n.
$$
Podstawa to

$$
\frac{12n^2-9n}{12n^2+11n+2}=1+\frac{-20n-2}{12n^2+11n+2}=1+c_n,
$$
gdzie $c_n\to0$ i $c_n\neq0$. Ponadto

$$
n\cdot c_n=\frac{n(-20n-2)}{12n^2+11n+2}\to-\frac{20}{12}=-\frac53.
$$
Z lematu B granica równa się $e^{-5/3}$.

**Wynik:** $e^{-5/3}$.

### 4.9. $\lim n\left[\ln(n+3)-\ln n\right]$

Z własności logarytmu $\ln(n+3)-\ln n=\ln\left(1+\dfrac3n\right)$, więc

$$
n\ln\left(1+\frac3n\right)=3\cdot\frac{\ln\left(1+\frac3n\right)}{\frac3n}\to3\cdot1=3
$$
na podstawie lematu A z $c_n=\dfrac3n$.

**Wynik:** $3$.

---

## Zadanie 5 (domowe)

Symbol nieoznaczony oznacza, że sama postać $\lim a_n^{ b_n}$ (lub $\lim\frac{a_n}{b_n}$) z granic składowych nie wystarcza do obliczenia granicy: dla różnych ciągów o tej samej postaci granice wychodzą różne. Poniżej po jednym przykładzie dla każdej granicy.

### $1^\infty$

Postać: $a_n\to1$, $b_n\to\infty$.

| Ciąg | Granica |
|---|---|
| $a_n=\left(1+\frac1n\right)^{n}$, podstawa $\to1$, wykładnik $\to\infty$ | $e$ |
| $b_n=\left(1+\frac1n\right)^{n^2}$ | $+\infty$ |
| $c_n=1^{n}=1$ | $1$ |
| $d_n=\left(1-\frac1n\right)^{n^2}$ | $0$ |

Uzasadnienia:

- $\left(1+\frac1n\right)^{n^2}\ge1+n^2\cdot\frac1n=1+n\to\infty$ (nierówność Bernoulliego).
- $\left(1-\frac1n\right)^{n^2}\le e^{-n}$ dla $n\ge2$, bo $\ln\left(1-\frac1n\right)\le-\frac1n$ (z nierówności $\ln(1-x)\le-x$ dla $x\lt 1$), więc $\ln d_n\le n^2\cdot\left(-\frac1n\right)=-n$.

### $\dfrac00$

Postać: licznik $\to0$, mianownik $\to0$ (mianownik różny od zera dla każdego $n$).

| Ciąg | Granica |
|---|---|
| $\dfrac{1/n}{1/n}=1$ | $1$ |
| $\dfrac{1/n^2}{1/n}=\dfrac1n$ | $0$ |
| $\dfrac{1/n}{1/n^2}=n$ | $+\infty$ |
| $\dfrac{(-1)^n/n}{1/n}=(-1)^n$ | granica nie istnieje |

Ostatni ciąg pokazuje, że nawet gdy licznik i mianownik zbiegają do zera, iloraz może nie mieć granicy.

### $\infty^0$

Postać: podstawa $\to\infty$, wykładnik $\to0$.

| Ciąg | Granica |
|---|---|
| $\left(e^{n^2}\right)^{1/n}=e^{n}$ | $+\infty$ |
| $\left(e^{n^2}\right)^{1/n^2}=e$ | $e$ |
| $\left(e^{n^2}\right)^{-1/n}=e^{-n}$ | $0$ |
| $n^{1/n}$ | $1$ |

Uzasadnienie: $\left(e^{n^2}\right)^{1/n}=e^{n}$, $\left(e^{n^2}\right)^{1/n^2}=e^{1}$, $\left(e^{n^2}\right)^{-1/n}=e^{-n}$ oraz $n^{1/n}=\sqrt[n]{n}\to1$.

### $\dfrac\infty\infty$

Postać: licznik i mianownik $\to\infty$ (co do wartości bezwzględnej).

| Ciąg | Granica |
|---|---|
| $\dfrac{n}{n}=1$ | $1$ |
| $\dfrac{n^2}{n}=n$ | $+\infty$ |
| $\dfrac{n}{n^2}=\dfrac1n$ | $0$ |
| $\dfrac{(-1)^n n}{n}=(-1)^n$ | granica nie istnieje |

---

## Podsumowanie

| Zadanie | Wynik |
|---|---|
| 1.1 | $+\infty$ |
| 1.2 | $16$ |
| 1.3 | $0$ |
| 1.4 | $\dfrac16$ |
| 1.5 | $3$ |
| 1.6 | $\dfrac52$ |
| 2.1 | $0$ |
| 2.2 | $4$ |
| 2.3 | $\dfrac13$ |
| 2.4 | $e+1$ |
| 2.5 | $e^{3/2}$ |
| 2.6 | $e$ |
| 3.1 | $-\dfrac{1}{125}$ |
| 3.2 | $\dfrac14$ |
| 3.3 | $\dfrac{\sqrt2}{2}$ |
| 3.4 | $0$ |
| 3.5 | $+\infty$ |
| 3.6 | $\dfrac19$ |
| 3.7 | $0$ |
| 3.8 | $\dfrac43$ |
| 4.1 | $0$ |
| 4.2 | $\dfrac35$ |
| 4.3 | $3$ |
| 4.4 | $4$ |
| 4.5 | $7$ |
| 4.6 | $1$ |
| 4.7 | $e^2$ |
| 4.8 | $e^{-5/3}$ |
| 4.9 | $3$ |
| 5 | przykłady w tabelach powyżej |
