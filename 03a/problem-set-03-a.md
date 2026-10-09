---
title: "Granica ciągów liczbowych"
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

# Granica ciągów liczbowych

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">

</script>
</div>
```

## Zadania na zajęcia

::::{exercise}
:label: prob-03a-ex-01
:class: [exercise]

Oblicz granicę ciągu liczbowego:

:::{container} columns-2-auto

1. $\LimInfty 5n^2 - n\cdot\arctan n$
2. $\LimInfty
    \dfrac{\Paren{n+\frac 1 n}^8}
    {\Brack{{{n+2}\choose {n}}}^5}
    \cdot \Paren{1+2+3+\ldots +n}
    $
3. $\LimInfty \dfrac{2^n+3^n}{4^n+3^n}$
4. $\LimInfty \dfrac{4^n+2^n}{2^{2n+1}+4^{n+1} + 3^n}.$
5. $\LimInfty \sqrt{n^2 + 5n} - \sqrt{n^2 - n}$
6. $\LimInfty \dfrac{\sqrt{n^2+5}-n}{\sqrt{n^2+2}-n}$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-02-ex-05`, {numref}`lec-02-ex-03`.
:::

::::

::::{exercise}
:label: prob-03a-ex-02
:class: [exercise]

Zwracając uwagę na założenia twierdzeń, z których korzystasz
oblicz granicę ciągu liczbowego:

:::{container} columns-2-auto

1. $\LimInfty  \dfrac{\cos\Paren{n!}}{n+\arcsin \frac 1 n }$
2. $\LimInfty \sqrt[n]{{4^n} + n^{13}\cdot 3^n}$
3. $\LimInfty \frac {n + 2022}{3n-(-1)^n}$
4. $\LimInfty \sqrt[\frac 1 n]{\frac{n+2}{n+1}} + \left( \dfrac{n+1}{n}\right)^{2022}$
5. $\LimInfty \Paren{\dfrac{1-n^2}{5 -2n}}^{n+1}\cdot \Paren{\frac 2 {n+1}}^{n+1}$
6. $\LimInfty \left( \dfrac{2n^2+2n+1}{2n^2+2}\right)^{n+1}.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-02-ex-01`, {numref}`lec-02-ex-02`, {numref}`lec-02-ex-04`.
:::

::::

## Zadania domowe

::::{exercise}
:label: prob-03a-ex-03
:class: [exercise]

Oblicz granicę ciągu liczbowego:

:::{container} columns-2-auto

1. $\LimInfty \dfrac {3n^3 - \sqrt{n^3 + 4n^6}} {\Paren{\sqrt{n} - 5n + 383764}^{3}}$
2. $\LimInfty \sqrt{4n^2 + n} - 2n$
3. $\LimInfty n\Paren{\sqrt{2n^2 + 1}-\sqrt{2n^2-1}}$
4. $\LimInfty \dfrac{3^{n+1}+2^n}{5^n+4\cdot 3^n}$
5. $\LimInfty \dfrac{4^n+5^n}{3\cdot 4^n+2^n}.$
6. $\LimInfty \displaystyle\frac{3^{n-1}+(-2)^{n}}{3^{n+1}+(-2)^{n+2}}$
7. $\LimInfty \dfrac{2^{3n}+5^{n+1}}{3^{2n+1}+4^{n-1}}$
8. $\LimInfty\displaystyle \frac{1+\frac{1}{2}+\frac{1}{4}+\ldots+\frac{1}{2^n}}{1+\frac{1}{3}+\frac{1}{9}+\ldots+\frac{1}{3^n}}.$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-02-ex-03`, {numref}`lec-02-ex-05`.
:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 2.
var('n')
p2 = sqrt(4*n^2 + n) - 2*n
show(LatexExpr(r"\lim_{n\to\infty}"), p2 == limit(p2, n=oo))

# Punkt 5.
p5 = (4^n + 5^n)/(3*4^n + 2^n)
show(LatexExpr(r"\lim_{n\to\infty}"), p5 == limit(p5, n=oo))
</script>
</div>
```

::::{exercise}
:label: prob-03a-ex-04
:class: [exercise]

Zwracając uwagę na założenia twierdzeń, z których korzystasz
oblicz granicę ciągu liczbowego:

:::{container} columns-2-auto

1. $\LimInfty \dfrac{\cos\Paren{n!}}{n+\arcsin \frac 1 n }$
2. $\LimInfty \dfrac {3n^2 - 1} {5n^2 + \cos n}$
3. $\LimInfty \dfrac {3n^2 - n\cdot(-1)^n} {(\sqrt n - 5)^4}$
4. $\LimInfty \sqrt[n]{\frac{4^n}{n^{12}} +n\cdot 3^n+5n^3}$
5. $\LimInfty \Paren{\frac {7^n}{n^{13}}+n}^{\frac 1 n}$
6. $\LimInfty \left( \dfrac{n+1}{n}\right)^{2019}$
7. $\LimInfty \Paren{\dfrac{2^n+4^n}{2^{2n}-2^n}}^{2^n}$
8. $\LimInfty \Paren{\dfrac{3n}{4n+1}}^{n}\cdot \Paren{\dfrac{4n-3}{3n+2}}^{n}$
9. $\LimInfty n\cdot\left[\ln(n+3)-\ln n\right]$
:::

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-02-ex-01`, {numref}`lec-02-ex-02`, {numref}`lec-02-ex-04`.
:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 7.
var('n')
p7 = ((2^n + 4^n)/(2^(2*n) - 2^n))^(2^n)
show(LatexExpr(r"\lim_{n\to\infty}"), p7 == limit(p7, n=oo))

# Punkt 9.
p9 = n*(ln(n + 3) - ln(n))
show(LatexExpr(r"\lim_{n\to\infty}"), p9 == limit(p9, n=oo))
</script>
</div>
```

::::{exercise}
:label: prob-03a-ex-05
:class: [exercise]

Pokaż przykłady ciągów świadczące o tym, że symbole $\displaystyle 1^\infty$,
$\displaystyle \frac 0 0$, $\displaystyle \infty^0$ i $\displaystyle \frac \infty \infty$
są nieoznaczone.

:::{note}
:class: [see-lecture]

Warto spojrzeć na {numref}`lec-02-ex-04`.
:::

::::
