---
title: "Funkcje"
lecture_number: 2
has_solutions: false
has_exercises: true
---

```{include} ../_includes/sagecell-loader.md
```

# Funkcje

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">

</script>
</div>
```

## Zadania na zajęcia

::::{exercise}
:label: prob-02-ex-01
:class: [exercise]

Dla $x\in\rr$ symbol $[x]$ oznacza największą liczbę całkowitą nie większą niż $x.$
Naszkicuj wykresy funkcji:

$$
f(x) = [x], \quad g(x)=x-[x].
$$

Można wspomóc się pakietem [GEOGEBRA](https://www.geogebra.org/calculator) lub powyższą komórką Sage,
ale należy przemyśleć jak to uzasadnić z pomocą obliczeń.
::::

::::{exercise}
:label: prob-02-ex-02
:class: [exercise]

Oblicz wartość wyrażenia:

:::{container} columns-2-auto

1. $\arccos\left(\sin\left(\displaystyle\frac{32}{5}\pi\right)\right)$
2. $\arcsin\left(\cos\left(-\displaystyle\frac{7}{11}\pi\right)\right).$

:::

::::

::::{exercise}
:label: prob-02-ex-03
:class: [exercise]

Naszkicuj wykresy funkcji i
na tej podstawie zbadaj, czy są okresowe podając okres podstawowy (jeśli ma to sens) dla:

1. $f_1(x) = \sin\Paren{\arcsin(x)} \qtq[oraz] f_2(x) = \arcsin\Paren{\sin x}$
2. $f_1(x)=\sin(\pi x) \qtq[oraz] f_2(x)=\ctg x\cdot |\sin x|.$

Można wspomóc się pakietem [GEOGEBRA](https://www.geogebra.org/calculator) lub powyższą komórką Sage,
ale należy przemyśleć jak to uzasadnić z pomocą obliczeń.
::::

::::{exercise}
:label: prob-02-ex-04
:class: [exercise]

Korzystając z definicji, zbadaj parzystość funkcji:

:::{container} columns-2-auto

1. $f(x)=x\cdot\Paren{2^x-2^{-x}}$
2. $f(x)=\log_2\Paren{x+\sqrt{x^2+1}}.$

:::

::::

::::{exercise}
:label: prob-02-ex-05
:class: [exercise]

Rozstrzygnij,
czy ciąg $\Paren{a_n}$ o podanych wyrazach jest monotoniczny.
Jeśli to możliwe podaj $n_0\in \nn$
takie, że dla każdego $n \geq n_0$ zachodzi $a_{n+1} > a_n$
lub dla każdego $n \geq n_0$ zachodzi $a_{n+1} < a_n$.

:::{container} columns-2-auto

1. $a_n = n^2 - 8n + 7$
2. $a_n = -\dfrac 2 {n + 3\arctan n}.$

:::

::::

## Zadania domowe

::::{exercise}
:label: prob-02-ex-06
:class: [exercise]

Oblicz wartość wyrażenia:

:::{container} columns-2-auto

1. $\arccos\Paren{\sin\Paren{\dfrac{11}{7}}}$
2. $\arccos\Paren{\sin\Paren{\dfrac{3}{5}\pi}}$
3. $\arcsin\Paren{\cos\Paren{-\dfrac{5}{11}}}$
4. $\arcsin\Paren{\cos\Paren{-\dfrac{3}{5}\pi}} .$

:::

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 1.
f1 = arccos(sin(11/7))
show(f1," = ",f1.simplify())
</script>
</div>
```

::::{exercise}
:label: prob-02-ex-07
:class: [exercise]

Naszkicuj wykresy funkcji i
na tej podstawie zbadaj, czy są okresowe podając okres podstawowy (jeśli ma to sens) dla:

1. $f_1(x) = \cos\Paren{\arccos(x)} \qtq[oraz] f_2(x) = \arccos\Paren{\cos x}$
2. $f_1(x) = \cos\dfrac x \pi \qtq[oraz] f_2(x)=(\sin x+\cos x)^2$
3. $f(x)=[2\sin x]\ .$

::::

```{raw} html
<div class="sagecell-widget sagecell-exercise">
<script type="text/x-sage">
# Punkt 3.
var('x')
f = floor(2*sin(x))
T = 2*pi
show(plot(f, (x, -4*pi, 4*pi),
        aspect_ratio=1,
        thickness=2) +
     line2d([(T, -3), (T, 3)], color='green', linestyle='--'),
     transparent=True,
     frame=False,
     figsize=8)
</script>
</div>
```

::::{exercise}
:label: prob-02-ex-08
:class: [exercise]

Rozstrzygnij,
czy ciąg $\Paren{a_n}$ o podanych wyrazach jest monotoniczny.
Jeśli to możliwe podaj $n_0\in \nn$
takie, że dla każdego $n \geq n_0$ zachodzi $a_{n+1} > a_n$
lub dla każdego $n \geq n_0$ zachodzi $a_{n+1} < a_n$.

:::{container} columns-3-auto

1. $a_n = \log_2 {2n + 3^n}$
2. $a_n = \cos{\dfrac{\pi n} 2}$
3. $a_n = \sin\Paren{\dfrac {10\pi} {n+1}} .$

:::

::::
