# Algorytm generacji liczb Fibonacciego metodą iteracyjną
rozwiązanie wykorzystuje zasadę programowania dynamicznego (ang. dynamic programming). Polega ona na tym, iż rozwiązanie wyższego poziomu obliczamy z rozwiązań otrzymanych na poziomie niższym, które odpowiednio zapamiętujemy. Dzięki temu podejściu program nie musi liczyć wszystkich składników od początku, wykorzystuje wyniki poprzednich obliczeń.

## Algorytm
**Wejście:**
* n – numer liczby ciągu Fibonacciego do wyliczenia, n ∈  N.

**Wyjscie:**
* n-ta liczba ciągu Fibonacciego.

**Zmienne pomocnicze**
* f 0, f 1, f 	 :  	kolejne trzy liczby Fibonacciego, f 0, f 1, f ∈ C.

## Przykładowy program

```python
def fibo_iter(n):
    f0 = 0
    f1 = 1
    f = 1
    for i in range(n + 1):
        if i <= 1:
            f = i
            continue
        f = f0 + f1
        f0 = f1
        f1 = f
    return f
```
