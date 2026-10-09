---
title: "Granica funkcji"
lecture_number: 3
has_solutions: false
has_exercises: true
file_format: mystnb
kernelspec:
  name: sagemath
  display_name: SageMath
---

```{include} ../_includes/sagecell-loader.md
```

# Granica funkcji

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">

</script>
</div>
```

## Zadania na zajęcia

::::{exercise}
:label: prob-03b-ex-01
:class: [exercise]

Zwracając uwagę na założenia twierdzeń,
z których korzystasz
oblicz granicę funkcji
(**nie wolno korzystać z reguły de l'Hospitala!**):

:::{container} columns-2-auto

1. $\LimIn{1} \dfrac{x^3 -3x^2 + 3x - 1} {x^3 - x^2 - x + 1} $
2. $\LimIn{0^+} \dfrac{x - \sqrt x}{x+ \sqrt x}$
3. $\LimIn{0} \dfrac{\tan 3x}{\sin 7x}$
4. $\LimIn{-1} \dfrac{\sin(x^2-1)}{x+1}$
5. $\LimIn{1^+}\left(\frac{x+1}{2x}\right)^{\frac{3}{x-1}}$
6. $\LimIn{-\infty} 3x +1 + \sqrt{9x^2 -2}.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-03`, {numref}`lec-03-ex-05`, {numref}`lec-03-ex-06`.
:::

::::

::::{exercise}
:label: prob-03b-ex-02
:class: [exercise]

Zwracając baczną uwagę na założenia twierdzeń, z których korzystasz
oblicz granice jednostronne funkcji $\displaystyle (1-\sin x)^{\frac{1}{x}}$
w punkcie $x_0=0$.
Czy istnieje granica $\displaystyle \lim_{x\to 0} (1-\sin x)^{\frac{1}{x}}$?

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-03`, {numref}`lec-03-ex-04`.
:::

::::

::::{exercise}
:label: prob-03b-ex-03
:class: [exercise]

Wykaż, że nie istnieje granica:

:::{container} columns-2-auto

1. $\LimIn{0}(1+|x|)^{\frac{1}{x}}$
2. $\LimIn{-\infty}\sin 3x.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-01`, {numref}`lec-03-ex-02`, {numref}`lec-03-ex-04`.
:::

::::

## Zadania domowe

::::{exercise}
:label: prob-03b-ex-04
:class: [exercise]

Zwracając uwagę na założenia twierdzeń, z których korzystasz
oblicz granicę funkcji
(**nie wolno korzystać z reguły de l'Hospitala!**):

:::{container} columns-2-auto

1. $\LimIn{0} \dfrac{ \tan 2x}{x}$
2. $\LimIn{0} \dfrac{1-\cos 6x}{x^2}$
3. $\LimIn{\frac{\pi}{2}} \frac{\cos x}{\cos 7x}$
4. $\LimIn{0} \dfrac{\arctan 3x}{7x}$
5. $\LimIn{0} \dfrac{\sin 7x}{4-\sqrt{5x+16}}$
6. $\LimIn{16} \dfrac{\sqrt{x \sqrt x} -8}{\sqrt[4]{x} -2}$
7. $\LimIn{0} \dfrac{\sqrt{x^2 + 4} -2}{\sqrt{x^2 + 9} -3}$
8. $\LimIn{1^+} \Paren{\dfrac {3-x^2} {x+1} }^{\frac 1 {x-1}}$
9. $\LimIn{0} (\cos x)^{\cot^2x}$
10. $\LimIn{+\infty} \sqrt{e^x + 1} - \sqrt{e^x - 1}$
11. $\LimIn{-\infty} \frac{\sqrt{2x^2+x+1}}{x}$
12. $\LimIn{-\infty} \sqrt{(x+3)(x-4)} + x$
13. $\LimIn{-\infty} \frac{\sqrt{2-x}-\sqrt{1-x}}{x+\sqrt{x^2+2x+3}}$
14. $\LimIn{+\infty} x\cdot\arctan \frac 1 x.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-03`, {numref}`lec-03-ex-05`, {numref}`lec-03-ex-06`.
:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 6.
var('x')
p6 = (sqrt(x*sqrt(x)) - 8)/(x^(1/4) - 2)
show(LatexExpr(r"\lim_{x\to 16}"), p6 == limit(p6, x=16))

# Punkt 12.
p12 = sqrt((x + 3)*(x - 4)) + x
show(LatexExpr(r"\lim_{x\to -\infty}"), p12 == limit(p12, x=-oo))
</script>
</div>
```

::::{exercise}
:label: prob-03b-ex-05
:class: [exercise]

Wykaż, że nie istnieje granica:

:::{container} columns-2-auto

1. $\LimIn{0^+}\cos\left(\frac{2}{x}\right)$
2. $\LimIn{1}2^{\frac{1}{x-1}}$
3. $\LimIn{0}\sin\left(\arctan \frac{1}{x}\right).$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-03-ex-01`, {numref}`lec-03-ex-02`, {numref}`lec-03-ex-04`.
:::

::::

::::{exercise}
:label: prob-03b-ex-06
:class: [exercise]

Wykaż, że dla $x\in\rr$ zachodzą równości:

:::{container} columns-2-auto

1. $\Ch^2 x - \Sh^2 x  = 1$
2. $\Ch^2 x + \Sh^2 x  = \Ch 2x$
3. $\Sh 2x = 2\Sh x \Ch x $
4. $\displaystyle {\Ch^2 x} = \frac 1 {1-\Th^2 x}.$

:::

::::