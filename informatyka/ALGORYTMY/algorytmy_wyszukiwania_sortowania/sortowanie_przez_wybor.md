# Sortowanie przez wybór (selection sort)
Idea algorytmu sortowania przez wybór jest bardzo prosta. Załóżmy, iż chcemy posortować zbiór liczbowy rosnąco. Zatem element najmniejszy powinien znaleźć się na pierwszej pozycji. Szukamy w zbiorze elementu najmniejszego i wymieniamy go z elementem na pierwszej pozycji. W ten sposób element najmniejszy znajdzie się na swojej docelowej pozycji.

## Algorytm
**Wejście:**
* d[ ]	- zbiór, który będzie sortowany. Elementy zbioru mają indeksy od 0.

**Wyjscie:**
* d[ ]	- posortowany zbiór

**Zmienne pomocnicze**
* i, j	- zmienne sterujące pętli, i, j ∈ N
* pmin	- pozycja elementu minimalnego w zbiorze d[ ],  pmin ∈ N


## Przykładowy program

```python
def selection(d):
    for i in range(len(d) - 1):
        pmin = i
        for j in range(i + 1, len(d)):
            if d[j] < d[pmin]:
                pmin = j
        d[i], d[pmin] = d[pmin], d[i]
    return d
```
