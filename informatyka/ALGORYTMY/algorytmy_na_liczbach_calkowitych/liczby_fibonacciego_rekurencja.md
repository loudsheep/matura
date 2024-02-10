# Algorytm generacji liczb Fibonacciego metodą rekurencyjną
Rozwiązanie opieramy bezpośrednio na definicji wykorzystując wywołania rekurencyjne. Jest to bardzo złe rozwiązanie (podajemy je tylko ze względów dydaktycznych), ponieważ algorytm wielokrotnie oblicza wyrazy ciągu, co w efekcie prowadzi do wykładniczej klasy złożoności obliczeniowej O (2 n).

## Algorytm
**Wejście:**
* n – numer liczby ciągu Fibonacciego do wyliczenia, n ∈  N.

**Wyjscie:**
* n-ta liczba ciągu Fibonacciego.


## Przykładowy program

```python
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 2) + fibo(n - 1)
```
