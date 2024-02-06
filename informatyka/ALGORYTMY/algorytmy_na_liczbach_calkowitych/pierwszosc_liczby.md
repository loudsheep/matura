# Algorytm sprawdzania pierwszości liczby naturalnej

Liczba jest pierwsza, jeśli nie posiada dzielników innych poza 1 i sobą samą. Pierwsze rozwiązanie testu na pierwszość (ang. primality test) polega na próbnym dzieleniu liczby p przez liczby z przedziału od 2 do [√p ] (do części całkowitej z pierwiastka z p) i badaniu reszty z dzielenia. Powód takiego postępowania jest prosty – jeśli liczba p posiada czynnik większy od pierwiastka z p, to drugi czynnik musi być mniejszy od pierwiastka, aby ich iloczyn był równy p. W przeciwnym razie iloczyn dwóch liczb większych od √p dawałby liczbę większą od p. Zatem wystarczy przebadać podzielność p przez liczby z przedziału [2, [√p ]], aby wykluczyć liczby złożone.


## Algorytm

**Wejście:**
* p - liczba badana na pierwszość, p ∈ N, p > 1.

**Wyjscie:**
* TAK, jeśli p jest pierwsze lub NIE w przypadku przeciwnym.

**Zmienne pomocnicze**
* g	 – 	granica sprawdzania podzielności p. g ∈ N.
* i	 – 	kolejne podzielniki liczby p, i ∈ N.

**Lista kroków**
1. przebiegamy przez przedział [2, [ √p]]
1. jeśli liczba z przedziału [2, [√p ]] dzieli p, to p nie jest pierwsze
1. jeśli żadna liczba z [2, [√p]] nie dzieli p, p jest pierwsze


## Przykładowy program

```python
def is_prime(p):
    for d in range(2, p // 2 + 1): # dla ułatwienia jest p/2 a nie √p
        if p % d == 0:
            return False
    return True
```
