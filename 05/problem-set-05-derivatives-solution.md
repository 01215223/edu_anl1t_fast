Oto kompletne rozwiązania zadań z przygotowanego przez Ciebie skryptu lekcji o pochodnych funkcji.
------------------------------
## Zadanie 1
Oblicz pochodną funkcji $f(x) = \frac{1}{1 + \cos x}$ bezpośrednio z definicji.
Korzystamy z definicji pochodnej jako granicy ilorazu różnicowego:
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$ 
Podstawiamy wzór funkcji:
$$f(x+h) - f(x) = \frac{1}{1 + \cos(x+h)} - \frac{1}{1 + \cos x} = \frac{\cos x - \cos(x+h)}{(1 + \cos(x+h))(1 + \cos x)}$$ 
Stosujemy wzór na różnicę cosinusów $\cos \alpha - \cos \beta = -2 \sin \frac{\alpha + \beta}{2} \sin \frac{\alpha - \beta}{2}$:
$$\cos x - \cos(x+h) = -2 \sin\left(\frac{2x+h}{2}\right) \sin\left(-\frac{h}{2}\right) = 2 \sin\left(x + \frac{h}{2}\right) \sin\left(\frac{h}{2}\right)$$ 
Wracamy do granicy:
$$f'(x) = \lim_{h \to 0} \frac{2 \sin\left(x + \frac{h}{2}\right) \sin\left(\frac{h}{2}\right)}{h \cdot (1 + \cos(x+h))(1 + \cos x)}$$ 
Zauważmy, że $\lim_{h \to 0} \frac{\sin(h/2)}{h/2} = 1$:
$$f'(x) = \lim_{h \to 0} \left[ \frac{\sin\left(\frac{h}{2}\right)}{\frac{h}{2}} \cdot \frac{\sin\left(x + \frac{h}{2}\right)}{(1 + \cos(x+h))(1 + \cos x)} \right] = 1 \cdot \frac{\sin x}{(1 + \cos x)^2} = \frac{\sin x}{(1 + \cos x)^2}$$ 
------------------------------
## Zadanie 2
Zbadaj istnienie f'(0) funkcji $f(x) = \begin{cases} x^k\sin\frac{1}{x} & \text{dla } x\neq 0 \\ 0 & \text{dla } x=0 \end{cases}$ dla k=1 i k=2.
Badamy istnienie granicy ilorazu różnicowego w punkcie x₀ = 0:
$$f'(0) = \lim_{h \to 0} \frac{f(0+h) - f(0)}{h} = \lim_{h \to 0} \frac{h^k \sin\frac{1}{h} - 0}{h} = \lim_{h \to 0} h^{k-1} \sin\frac{1}{h}$$ 

* Dla k=1: $\lim_{h \to 0} \sin\frac{1}{h}$ nie istnieje, ponieważ funkcja oscyluje nieskończenie wiele razy między -1 a 1 w otoczeniu zera. Pochodna f'(0) nie istnieje.
* Dla k=2: $\lim_{h \to 0} h \sin\frac{1}{h} = 0$, na mocy twierdzenia o trzech funkcjach (ponieważ $-h \le h \sin\frac{1}{h} \le h$ dla h>0). Pochodna f'(0) istnieje i wynosi 0.

------------------------------
## Zadanie 3
Oblicz pochodną funkcji $f(x) = \ln \tan x$ na trzy sposoby podane w treści.
Przed przystąpieniem do obliczeń zakładamy, że x należy do dziedziny, czyli $\tan x > 0 \implies x \in (k\pi, \frac{\pi}{2} + k\pi)$.

* Sposób 1: Pochodna logarytmu ilorazu $f(x) = \ln \frac{\sin x}{\cos x}$
$$f'(x) = \frac{1}{\frac{\sin x}{\cos x}} \cdot \left( \frac{\sin x}{\cos x} \right)' = \frac{\cos x}{\sin x} \cdot \frac{\cos x \cdot \cos x - \sin x \cdot (-\sin x)}{\cos^2 x} = \frac{\cos x}{\sin x} \cdot \frac{1}{\cos^2 x} = \frac{1}{\sin x \cos x}$$ 
* Sposób 2: Pochodna różnicy logarytmów $f(x) = \ln \sin x - \ln \cos x$
$$f'(x) = (\ln \sin x)' - (\ln \cos x)' = \frac{1}{\sin x} \cdot \cos x - \frac{1}{\cos x} \cdot (-\sin x) = \frac{\cos x}{\sin x} + \frac{\sin x}{\cos x} = \frac{\cos^2 x + \sin^2 x}{\sin x \cos x} = \frac{1}{\sin x \cos x}$$ 
* Sposób 3: Bezpośrednia pochodna z funkcji złożonej $f(x) = \ln \tan x$
$$f'(x) = \frac{1}{\tan x} \cdot (\tan x)' = \frac{\cos x}{\sin x} \cdot \frac{1}{\cos^2 x} = \frac{1}{\sin x \cos x}$$ 

(Uwaga: Korzystając ze wzoru na sinus podwojonego kąta, wynik można zapisać jako $\frac{2}{\sin 2x}$).
------------------------------
## Zadanie 4
Oblicz pochodne podanych funkcji:

   1. $f(x)=\sqrt{2x}\cdot \arctan x + \sin(x^3+2x)$
   Stosujemy wzór na pochodną iloczynu oraz pochodną funkcji złożonej:
   $$f'(x) = \frac{2}{2\sqrt{2x}} \cdot \arctan x + \sqrt{2x} \cdot \frac{1}{1+x^2} + \cos(x^3+2x) \cdot (3x^2+2) = \frac{\arctan x}{\sqrt{2x}} + \frac{\sqrt{2x}}{1+x^2} + (3x^2+2)\cos(x^3+2x)$$ 
   2. $f(x)= \sqrt[5]{x^3}\cdot \tan(5x+1) = x^{3/5} \cdot \tan(5x+1)$
   $$f'(x) = \frac{3}{5}x^{-2/5} \cdot \tan(5x+1) + x^{3/5} \cdot \frac{1}{\cos^2(5x+1)} \cdot 5 = \frac{3\tan(5x+1)}{5\sqrt[5]{x^2}} + \frac{5\sqrt[5]{x^3}}{\cos^2(5x+1)}$$ 
   3. $f(x)= \sqrt{\sin (3x^2-x)} - \ln \frac 1 {5x^{x}}$
   Najpierw uprośćmy drugi człon: $- \ln \frac 1 {5x^x} = \ln(5x^x) = \ln 5 + \ln x^x = \ln 5 + x \ln x$. Pochodna z $(x\ln x)$ to $\ln x + 1$.
   $$f'(x) = \frac{1}{2\sqrt{\sin(3x^2-x)}} \cdot \cos(3x^2-x) \cdot (6x-1) + \left( \ln x + 1 \right) = \frac{(6x-1)\cos(3x^2-x)}{2\sqrt{\sin(3x^2-x)}} + \ln x + 1$$ 
   4. $f(x)=x^e \, \arcsin x - x^{\cos(2x)}$
   Dla drugiego składnika stosujemy tożsamość $x^g = e^{g \ln x}$, czyli $\left(x^{\cos(2x)}\right)' = \left(e^{\cos(2x) \ln x}\right)' = x^{\cos(2x)} \cdot \left( -2\sin(2x)\ln x + \frac{\cos(2x)}{x} \right)$.
   $$f'(x) = e x^{e-1} \arcsin x + x^e \cdot \frac{1}{\sqrt{1-x^2}} - x^{\cos(2x)} \left( \frac{\cos(2x)}{x} - 2\sin(2x)\ln x \right)$$ 
   5. $f(x)= (7x^2-2)^{13} + 2\log_x(\arctan x)$
   Zamieniamy podstawę logarytmu: $\log_x(\arctan x) = \frac{\ln(\arctan x)}{\ln x}$. Pochodna tego ułamka to: $\frac{\frac{1}{\arctan x \cdot (1+x^2)} \cdot \ln x - \ln(\arctan x) \cdot \frac{1}{x}}{\ln^2 x}$.
   $$f'(x) = 13(7x^2-2)^{12} \cdot 14x + 2 \cdot \frac{\frac{\ln x}{\arctan x \cdot (1+x^2)} - \frac{\ln(\arctan x)}{x}}{\ln^2 x}$$ 

------------------------------
## Zadanie 5 (Dokończenie treści i rozwiązanie)
Treść zadania została urwana, ale na podstawie standardowych przykładów akademickich i rozpoczętych zapisów, najprawdopodobniej brakujące fragmenty to:

   1. $\lim_{x \to 0} \frac{\sin{x} + 2x}{\cos{x} - 3x -1}$
   2. $\lim_{x \to +\infty} \frac{\sin{x}}{x}$ (częsty przykład-pułapka przy l'Hospitalu) lub $\lim_{x \to 0^+} x \ln x$. Rozwiążmy najbardziej standardowe interpretacje:


* Podpunkt 1:
$$\lim_{x \to 0} \frac{\sin{x} + 2x}{\cos{x} - 3x -1} \quad \left[\frac{0}{0}\right]$$ 
Stosujemy regułę de l'Hospitala (pochodna licznika i mianownika):
$$= \lim_{x \to 0} \frac{\cos x + 2}{-\sin x - 3} = \frac{1 + 2}{0 - 3} = \frac{3}{-3} = -1$$ 
* Podpunkt 2 (Zakładając standardowe uzupełnienie $\lim_{x \to +\infty} \frac{\ln x}{x}$ lub $\lim_{x \to 0^+} x \ln x$):
Wariant A: Jeśli symbolem była granica $\lim_{x \to +\infty} \frac{\ln x}{x}$ $\left[\frac{\infty}{\infty}\right]$:
$$= \lim_{x \to +\infty} \frac{\frac{1}{x}}{1} = 0$$ 
Wariant B: Jeśli w mianowniku był po prostu x (jak zaczęto pisać $\lim_{x \to +\infty} \frac{\sin x}{x}$):
Uwaga: Tutaj reguła de l'Hospitala nie działa, ponieważ granica pochodnej mianownika i licznika ($\lim \cos x$) nie istnieje. Granicę tę oblicza się z twierdzenia o trzech funkcjach: $-\frac{1}{x} \le \frac{\sin x}{x} \le \frac{1}{x}$, stąd wynik to 0.

Jeśli podpunkt 5.2 w Twoich materiałach wyglądał inaczej, podaj jego pełną treść, a chętnie go rozpiszę. Czy chciałbyś również wygenerować kod w SageMath, który automatycznie weryfikuje powyższe pochodne w komórce widżetu?
