# Rozkład liczby naturalnej na czynniki pierwsze
Będziemy sprawdzać podzielność liczby p przez kolejne liczby naturalne od 2 do pierwiastka z p. Jeśli liczba p będzie podzielna przez daną liczbę, to liczbę wyprowadzimy na wyjście, a za nowe p przyjmiemy wynik dzielenia i próbę dzielenia będziemy powtarzać dotąd, aż nie będzie to już możliwe. Wtedy przejdziemy do następnego dzielnika.

## Algorytm
**Wejście:**
* p - liczba rozkładana na czynniki pierwsze, p  ∈ N, p > 1.

**Wyjscie:**
* Czynniki pierwsze liczby p.

**Zmienne pomocnicze**
* g - granica sprawdzania podzielności liczby p, g ∈ N.
* i - kolejne podzielniki, i ∈ N.
* result - tablica podzielników

**Lista kroków**
1. w pętli sprawdzamy podzielność liczby p przez kolejne liczby
1. dopóki dzielnik dzieli p
1. wyprowadzamy go i
1. dzielimy przez niego p
1. pętlę przerywamy, gdy stwierdzimy brak dalszych dzielników
1. p może posiadać ostatni czynnik większy od pierwiastka z p

## Przykładowy program

```python
def czynniki(p):
    q = p // 2 + 1
    result = []
    i = 2
    while i <= q:
        if p % i == 0:
            result.append(i)
            p //= i
        else:
            i += 1
    return result
```
