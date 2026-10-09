---
title: "Powtórzenie ze szkoły średniej"
lecture_number: 1
has_solutions: false
has_exercises: true
---

```{include} ../_includes/sagecell-loader.md
```

# Powtórzenie ze szkoły średniej

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">

</script>
</div>
```

## Zadania na zajęcia

::::{exercise}
:label: prob-01-ex-01
:class: [exercise]

Dla funkcji $f(x) = x^x + \log_x \Paren{1+ 2\sqrt x + 3x^2}$ wyznacz:

$$
f(-x),\quad f\Paren{\frac 1 x},\quad f(\sqrt x)\quad \text{ oraz } \quad f\Paren{x^2}.
$$

::::

::::{exercise}
:label: prob-01-ex-02
:class: [exercise]

Wyznacz dziedzinę $D_f$, zbiór wartości $R_f$,
przedziały monotoniczności oraz naszkicuj wykres funkcji $f$, jeśli:

:::{container} columns-2-auto

1. $f(x)=\displaystyle\frac{x^2-3x+2}{4-x^2}$

2. $f(x)=\displaystyle\frac
    {\log_{\sqrt 2} \Paren{\frac 1 2} - \log_3 x}
    {\log_3\Paren{9x}}
    \cdot \Paren{x^2-x-2}
    \ .
   $

:::

::::

::::{exercise}
:label: prob-01-ex-03
:class: [exercise]

Rozwiąż równanie/nierówność:

:::{container} columns-2-auto

1. $(1-x)(2-x)^2 (x+3)^3 < 0$
2. $\dfrac {(x+3)^3}{(x^2 - 1)(x+1)} \geq 0$
3. $3\log(x+1)=\log\Paren{1-x^2}$
4. $\displaystyle\frac{x^2-x}{\log_2x-1}\leq 0$
5. $2^{|x|-1}\leq \Paren{\displaystyle\frac{1}{2}}^{|x|}.$

:::

::::

## Zadania domowe

::::{exercise}
:label: prob-01-ex-04
:class: [exercise]

Dla funkcji $f(x) = \dfrac {1+2x}{x - x^2} + \sin\Paren{x^{-1} + \sqrt x}$
wyznacz

$$
f(-x),\quad f\Paren{\frac 1 x},\quad f(\sqrt x)\quad \text{ oraz } \quad f\Paren{x^2}.
$$

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 1.
var('x')
f(x) = (1 + 2*x)/(x - x^2) + sin(x^(-1) + sqrt(x))

show("f(-x) = ", f(-x))
show("f(1/x) = ", f(1/x))
show("f(sqrt(x)) = ", f(sqrt(x)))
show("f(x^2) = ", f(x^2))
</script>
</div>
```

::::{exercise}
:label: prob-01-ex-05
:class: [exercise]

Wyznacz dziedzinę $D_f$, zbiór wartości $R_f$,
przedziały monotoniczności oraz naszkicuj wykres funkcji $f$, jeśli:

:::{container} columns-2-auto

1. $f(x)=\displaystyle\frac{1}{\sqrt{x^2-2x+1}}$
2. $f(x)=\displaystyle\frac{x^2+x+6}{2\log_5 (x+1)}\cdot \log_5\Paren{x^2 +2x + 1}.$

:::

::::

::::{exercise}
:label: prob-01-ex-06
:class: [exercise]

Rozwiąż równanie/nierówność:

1. $\sqrt{x + 4} > x-8$
2. $\sqrt{x + 5} = 5 - \sqrt{x+10}$
3. $(1-x)^{-1}(2-x)^{-2} (x-3) \geq 0$
4. $\log_3(x+1) + \log_{\sqrt 3} (x+1) + \log_{\frac 1 3}(x+1) = 6$
5. $(\log x - 1)(\log x - 10)(x+2) \leq 0$
6. $\displaystyle \frac{\log_2x-1}{x^2-x}\leq 0$
7. $\Paren{2^{|x+2|}}^2 - 4\cdot 2^{1-x} < 0.$

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
var('x')
# Punkt 1: sqrt(x+4) > x-8
f1 = x + 4 > (x - 8)^2
show(f1)
show("Rozwiązanie niepełne (dlaczego?):", solve(f1, x))

# Punkt 4: log_3(x+1) + log_sqrt(3)(x+1) + log_(1/3)(x+1) = 6
f4 = log(x + 1, 3) + log(x + 1, sqrt(3)) + log(x + 1, 1/3) == 6
show(f4)
show("Rozwiązanie poprawne:", solve(f4, x))
</script>
</div>
```
