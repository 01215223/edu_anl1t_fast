---
title: "Ciągłość funkcji"
lecture_number: 4
has_solutions: false
has_exercises: true
---

```{include} ../_includes/sagecell-loader.md
```

# Ciągłość funkcji

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">

</script>
</div>
```

## Zadania na zajęcia

::::{exercise}
:label: prob-04-ex-01
:class: [exercise]

Wyznacz równania asymptot wykresu funkcji $f$, jeśli:

:::{container} columns-2-auto

1. $f(x)=e^{\frac{1}{x^2-4}}$
2. $f(x)=x+\arctan \Paren{\dfrac{2-x}{2+x}}$
3. $f(x)=\sqrt{x^2+1}-\sqrt{x^2-1}.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-07`, {numref}`lec-03-ex-08`, {numref}`lec-03-ex-09`, {numref}`lec-04-ex-01`.
:::

::::

::::{exercise}
:label: prob-04-ex-02
:class: [exercise]

Korzystając z definicji, twierdzeń, własności funkcji elementarnych
podanych na wykładzie zbadaj
ciągłość funkcji $f$ **w każdym punkcie należącym do jej dziedziny**;
w przypadku punktu nieciągłości określ jego rodzaj, jeśli
$f(x)=\begin{cases}
         (x+2)^2                                                & \text{dla } x< 1 \\
         \arcsin(x-1)                                           & \text{dla } x\in\Set{1,2} \\
         \dfrac 1 {\ln(x-1)} & \text{w p.p.}
      \end{cases} .$

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-02`.
:::

::::

::::{exercise}
:label: prob-04-ex-03
:class: [exercise]

Dla jakiej wartości parametrów $a, b\in\rr$ funkcja $f$ jest ciągła w $\rr$, jeśli

```{math}
\begin{aligned}
f(x)=\begin{cases}
         ax+b                                                        & \text{dla } x<1           \\
         \log_a x                                                    & \text{dla } 1\leq x\leq 4 \\
         \displaystyle\frac{\pi}{\arctan \left(\frac{1}{x-4}\right)} & \text{dla } x> 4
      \end{cases}\ .
\end{aligned}
```

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-02`.
:::

::::

::::{exercise}
:label: prob-04-ex-04
:class: [exercise]

Nie używając pochodnych funkcji, wykaż, że równanie

```{math}
\ln x+2x=1
```

ma dokładnie jedno rozwiązanie w przedziale $\left[\frac{1}{2}, 1\right]$.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-03`, {numref}`lec-04-ex-04`, {numref}`lec-04-ex-05`.
:::

::::

## Zadania domowe

::::{exercise}
:label: prob-04-ex-05
:class: [exercise]

Wyznacz równania asymptot wykresu funkcji $f$, jeśli:

:::{container} columns-2-auto

1. $f(x)=\sqrt{x^2+2x}+x$
2. $f(x)=\arcsin \Paren{\dfrac{1+x}{1-x}}$
3. $f(x)=(x+1)e^{\frac 1 x}$
4. $f(x)=\dfrac{2 + x\ln x }{3 \ln x}.$
5. $f(x)=\dfrac 1 {\ln x + \ln (3 - x)} .$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-07`, {numref}`lec-03-ex-08`, {numref}`lec-03-ex-09`, {numref}`lec-04-ex-01`.
:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 4.
var('x y')
f = (2 + x*ln(x))/(3*ln(x))

# Metoda szukania asymptot ukośnych (dziedzina x > 0, wiec tylko +oo):
m = limit(f/x, x=+oo)
k = limit(f - m*x, x=+oo)
show("asymptota ukośna:", y == m*x + k)

# Asymptota pionowa w x = 1 (mianownik ln(x) = 0):
show("asymptota pionowa x = 1, bo granica w x = 1^+ równa:", limit(f, x=1, dir='plus'))
</script>
</div>
```

::::{exercise}
:label: prob-04-ex-06
:class: [exercise]

Korzystając z definicji, twierdzeń, własności funkcji elementarnych
podanych na wykładzie uzasadnij
ciągłość funkcji $f$ w każdym punkcie należącym do jej dziedziny;
w przypadku punktu nieciągłości określ jego rodzaj, jeśli:

1. $f(x)=\begin{cases}
   e^{\frac{1}{x}} & \text{dla } x\neq 0 \\
   0               & \text{dla } x=0
   \end{cases}$
2. $
   \begin{aligned}
   f(x)=\begin{cases}
   (x+2)^2                                                & \text{dla } x=-1 \\
   \arcsin(x-1)                                           & \text{dla } x=1  \\
   (1-x)\arctan \left(\displaystyle\frac{1}{1-x^2}\right) & \text{w p.p.}
   \end{cases}
   \end{aligned}
   $

3. $
   \begin{aligned}
   f(x)=\begin{cases}
   \displaystyle\frac{x}{\sin x} & \text{dla } x\in(-\pi, 2\pi)\setminus\Set{0, \pi} \\
   \sin x                        & \text{dla } x\in\Set{0, \pi}
   \end{cases}
   \end{aligned}
   $

4. $
   \begin{aligned}
   f(x)=
   \begin{cases}
   \arcctg \left(\displaystyle\frac{1}{x}\right) & \text{dla } x\neq 0 \\
   0                                             & \text{dla } x=0
   \end{cases}\ .
   \end{aligned}
   $

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-02`.
:::

::::

::::{exercise}
:label: prob-04-ex-07
:class: [exercise]

Dla jakiej wartości parametrów $a, b\in\rr$ funkcja $f$ jest ciągła w $\rr$, jeśli
$f(x)=\begin{cases}
         b+3(x-1)^2            & \text{dla } x\leq 0 \\
         x\cdot\sin\frac{a}{x} & \text{dla } x>0
      \end{cases} .$

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-02`.
:::

::::

::::{exercise}
:label: prob-04-ex-08
:class: [exercise]

Wykaż, że równanie  $e^x-2\cos x=0$ ma pierwiastek w przedziale $(0, 1)$.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-04`, {numref}`lec-04-ex-03`, {numref}`lec-04-ex-05`.
:::

::::

::::{exercise}
:label: prob-04-ex-09
:class: [exercise]

Nie używając pochodnych funkcji, uzasadnij, że równanie $x^x=3$
ma dokładnie jedno rozwiązanie w przedziale $(1, 2)$.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-04-ex-05`, {numref}`lec-04-ex-03`, {numref}`lec-04-ex-04`.
:::

::::
