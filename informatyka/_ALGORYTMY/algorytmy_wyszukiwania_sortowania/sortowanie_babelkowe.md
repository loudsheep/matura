# Sortowanie bąbelkowe (bubble sort)
Algorytm sortowania bąbelkowego jest jednym z najstarszych algorytmów sortujących. Zasada działania opiera się na cyklicznym porównywaniu par sąsiadujących elementów i zamianie ich kolejności w przypadku niespełnienia kryterium porządkowego zbioru. Operację tę wykonujemy dotąd, aż cały zbiór zostanie posortowany.

## Algorytm
**Wejście:**
* d[ ]	- zbiór, który będzie sortowany. Elementy zbioru mają indeksy od 0.


**Wyjscie:**
* d[ ]	- posortowany zbiór

**Zmienne pomocnicze**
* i, j	- zmienne sterujące pętli, i, j ∈ N


## Przykładowy program

```python
def bubble(d):
    for i in range(len(d) - 1):
        for j in range(len(d) - 1):
            if d[j] > d[j + 1]:
                d[j], d[j + 1] = d[j + 1], d[j]
    return d
```
