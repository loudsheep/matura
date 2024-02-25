# Algorytm wyznaczania najmniejszej wspólnej wielokrotności

Dla danych dwóch liczb naturalnych a i b znaleźć najmniejszą liczbę naturalną c, która jest podzielna bez reszty przez a i przez b.

Liczba naturalna c o takich własnościach nosi nazwę NWW – najmniejszej wspólnej wielokrotności liczb a i b

## Algorytm
**Wejście:**
* a, b	 – 	liczby, których NWW poszukujemy, a, b ∈ N.


**Wyjscie:**
* NWW – najmniejsza wspólna wielokrotność liczb a i b.

**Zmienne pomocnicze**
* ab	 – 	zapamiętuje iloczyn a i b. ab ∈ N.
* t	 –  	tymczasowo przechowuje dzielnik w algorytmie Euklidesa, t ∈ N.


## Przykładowy program

```python
def nww(a, b):
    ab = a * b
    while b != 0:
        t = b
        b = a % b
        a = t
    ab = ab // a
    return ab
```
