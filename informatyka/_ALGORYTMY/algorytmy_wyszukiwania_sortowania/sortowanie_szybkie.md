# Sortowanie szybkie (quick sort)
Algorytm sortowania szybkiego opiera się na strategii "dziel i zwyciężaj". Do utworzenia partycji musimy ze zbioru wybrać jeden z elementów, który nazwiemy piwotem. W lewej partycji znajdą się wszystkie elementy niewiększe od piwotu, a w prawej partycji umieścimy wszystkie elementy niemniejsze od piwotu. Położenie elementów równych nie wpływa na proces sortowania, zatem mogą one występować w obu partycjach. Również porządek elementów w każdej z partycji nie jest ustalony.

## Algorytm
**Wejście:**
* d[ ]	- zbiór, który będzie sortowany. Elementy zbioru mają indeksy od 0.
* lewy	- indeks pierwszego elementu w zbiorze, lewy ∈ C
* prawy	- indeks ostatniego elementu w zbiorze, prawy ∈ C

**Wyjscie:**
* d[ ]	- posortowany zbiór

**Zmienne pomocnicze**
* pivot	-	element podziałowy
* i, j	-	indeksy, i, j ∈ C


## Przykładowy program

```python
def quick(d, lewy, prawy):
    # ustaw pivot na najbardziej prawy element
    pivot = d[prawy]
    j = lewy
    for i in range(lewy, prawy - 1):
        # jeżeli aktualny element jest większy lub równy pivot to go pomiń
        if d[i] >= pivot:
            continue
        # w przeciwnym razie zamień elementy i, j ze sobą
        d[i], d[j] = d[j], d[i]
        j += 1
    # trzeba zamienić pivot z j
    d[prawy], d[j] = d[j], d[prawy]
    # posortuj pozostałe 2 tablice
    if lewy < j - 1:
        quick(d, lewy, j - 1)
    if j + 1 < prawy:
        quick(d, j + 1, prawy)
    return d
```
