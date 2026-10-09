---
title: "Pochodna funkcji"
lecture_number: 5
has_solutions: false
has_exercises: true
---

```{include} ../_includes/sagecell-loader.md
```

# Pochodna funkcji

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">

</script>
</div>
```

## Zadania na zajęcia

::::{exercise}
:label: prob-05-ex-01
:class: [exercise]

Korzystając z definicji  oblicz $f'(x)$  dla
$f(x)=\displaystyle\frac{1}{1+ \cos x}$.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-01`.
:::

::::

::::{exercise}
:label: prob-05-ex-02
:class: [exercise]

Zbadaj istnienie $f'(0)$ funkcji
$
\quad
   f(x)=\begin{cases}
      x^k\sin\frac{1}{x} & \text{dla } x\neq 0 \\
      0                  & \text{dla } x=0
   \end{cases}
\quad
$
w dwóch przypadkach, gdy $k=1$ i $k=2.$

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-10`, {numref}`lec-05-ex-01`.
:::

::::

::::{exercise}
:label: prob-05-ex-03
:class: [exercise]

Oblicz pochodną

```{math}
\begin{aligned}
f(x)
  = \ln \dfrac {\sin x} {\cos x}
  = \ln \sin x - \ln \cos x
  = \ln \tan x
\end{aligned}
```

  na trzy różne sposoby.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-02`, {numref}`lec-05-ex-03`.
:::

::::

::::{exercise}
:label: prob-05-ex-04
:class: [exercise]

Oblicz, zakładając że istnieje, pochodną funkcji:

:::{container} columns-2-auto

1. $f(x)=\sqrt{2x}\cdot \arctan x  + \sin(x^3+2x)$
2. $\displaystyle f(x)= \sqrt[5]{x^3}\cdot \tan\Paren{5x+1}$
3. $\displaystyle f(x)= \sqrt{\sin \Paren{3x^2-x}} -  \ln \frac 1 {5x^{x}}$
4. $f(x)=x^e \, \arcsin x - x^{\cos(2x)}$
5. $f(x)= \Paren{7x^2-2}^{13} + 2\log_x(\arctan x).$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-02`, {numref}`lec-05-ex-03`, {numref}`lec-05-ex-04`.
:::

::::

::::{exercise}
:label: prob-05-ex-05
:class: [exercise]

Pamiętając o regule de l'Hospitala, oblicz granicę funkcji:

:::{container} columns-2-auto

1. $\LimIn{0} \frac{\sin{x} + 2x}{\cos{x} - 3x -1}$
2. $\LimIn{+\infty} \frac{\sin{x} + 2x}{\cos{x} - 3x -1}$
3. $\LimIn{+\infty} \frac{1+ \ln \Paren{2x+1}} {3 - \ln x}$
4. $\LimIn{\frac{\pi}{2}^-}\frac{\tan x}{\ln\left(\frac{\pi}{2}-x\right)}$
5. $\LimIn{-\infty}x^2\cdot e^{2x}$
6. $\LimIn{1} \frac{x} {x-1} - \frac 1 {\ln x} .$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-05`.
:::

::::

## Zadania domowe

::::{exercise}
:label: prob-05-ex-06
:class: [exercise]

Korzystając z definicji  oblicz $f'(x)$  dla funkcji
$f(x)=\displaystyle\sqrt{3x+2}$.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-01`.
:::

::::

::::{exercise}
:label: prob-05-ex-07
:class: [exercise]

Zbadaj istnienie $f'(1)$ funkcji
$
\quad
f(x) = x\cdot |x-1| .$

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-10`, {numref}`lec-05-ex-01`.
:::

::::

::::{exercise}
:label: prob-05-ex-08
:class: [exercise]

Oblicz, zakładając że istnieje, pochodną funkcji:

:::{container} columns-2-auto

1. $f(x) = \ln \dfrac {x+ \sin x} {x - \cos x}$
2. $\displaystyle f(x)=\sqrt[5]{x^3\cos x} + \arctan e^{2x^3}$
3. $f(x) = \Paren{3x^2+5}^7 + \sin\Paren{\cos x}$
4. $f(x) = x\sqrt{4\sin x} +  \log_2 (x^3 - 2x^2)$
5. $f(x) = \dfrac 2 {\sqrt[3]{3x}} + \log_{x^2+4x} (x^3 - 2)$
6. $f(x) = 2^{\sin x} - 3\cos \left(\log_x x \right)$
7. $f(x) = \arcsin (\log_x(\cos x^3))$
8. $f(x) = x^{(x^2)} + \Paren{x^x}^2$
9. $f(x) = x^{(x^x)} + \Paren{x^x}^x$
10. $f(x)=\sqrt[x]{1+x}.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-02`, {numref}`lec-05-ex-03`, {numref}`lec-05-ex-04`.
:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 3.
var('x')
f3 = (3*x^2 + 5)^7 + sin(cos(x))
show("f =", f3)
show("f' =", f3.diff(x))

# Punkt 9.
f9 = x^(x^x) + (x^x)^x
show("f =", f9)
show("f' =", f9.diff(x))
</script>
</div>
```

::::{exercise}
:label: prob-05-ex-09
:class: [exercise]

Pamiętając o regule de l'Hospitala, oblicz granicę funkcji:

:::{container} columns-2-auto

1. $\LimIn{+\infty}\frac{e^x-e^{-x}}{e^x+e^{-x}}$
2. $\LimIn{0}\frac {x \cot x -1} {x^2} $
3. $\LimIn{0}\frac{2e^x-2e^{-x}-4x}{\sin x-x}$
4. $\LimIn{+\infty} \frac{\ln \Paren{x+2}} {\ln \Paren{x^2 + 1}}$
5. $\LimIn{+\infty} \frac{\arcsin \frac 1 x} {\arctan x - \frac x 2}$
6. $\LimIn{0}\frac{\cos x-1+\frac{1}{2}x^2}{x^4}$
7. $\LimIn{-\infty}x\cdot\left(\pi+2\arctan x\right)$
8. $\LimIn{0^-} x^2\cdot e^{-\frac 1 x}$
9. $\LimIn{0^+} x \ln x$
10. $\LimIn{0^+} \ln(1-x) \ln x.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-05-ex-05`.
:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 1.
var('x')
g1 = (e^x - e^(-x))/(e^x + e^(-x))
show(LatexExpr(r"\lim_{x\to +\infty}"), g1 == limit(g1, x=+oo))

# Punkt 10.
g10 = ln(1 - x)*ln(x)
show(LatexExpr(r"\lim_{x\to 0^+}"), g10 == limit(g10, x=0, dir='plus'))
</script>
</div>
```
