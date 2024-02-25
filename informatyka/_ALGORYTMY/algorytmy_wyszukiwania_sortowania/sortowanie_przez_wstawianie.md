# Sortowanie przez wstawianie (insertion sort)
Algorytm sortowania przez wstawianie można porównać do sposobu układania kart pobieranych z talii. Najpierw bierzemy pierwszą kartę. Następnie pobieramy kolejne, aż do wyczerpania talii. Każdą pobraną kartę porównujemy z kartami, które już trzymamy w ręce i szukamy dla niej miejsca przed pierwszą kartą starszą (młodszą w przypadku porządku malejącego). Gdy znajdziemy takie miejsce, rozsuwamy karty i nową wstawiamy na przygotowane w ten sposób miejsce. Jeśli nasza karta jest najstarsza (najmłodsza), to umieszczamy ją na samym końcu.

## Algorytm
**Wejście:**
* d[ ]	- zbiór, który będzie sortowany. Elementy zbioru mają indeksy od 0.

**Wyjscie:**
* d[ ]	- posortowany zbiór

**Zmienne pomocnicze**
* i, j	- zmienne sterujące pętli, i, j ∈ N
* x	- zawiera wybrany ze zbioru element.

## Przykładowy program

```python
def insertion(d):
    i = len(d) - 2
    while i >= 0:
        x = d[i]
        j = i + 1
        while j < len(d) and x > d[j]:
            d[j - 1] = d[j]
            j += 1
        d[j - 1] = x
        i -= 1
    return d
```
