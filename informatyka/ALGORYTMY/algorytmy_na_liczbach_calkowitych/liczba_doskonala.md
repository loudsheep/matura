# Sprawdzanie czy liczba jest liczbą doskonałą
Liczba doskonała (definicja) to taka liczba naturalna, której suma jej dzielników właściwych (bez niej samej) jest jej równa.

## Algorytm
**Wejście:**
* n - liczba do sprawdzenia

**Wyjscie:**
* True, jeśli liczba jest doskonała, False jak nie

**Zmienne pomocnicze**
* s - suma zwiększana dzielnikami n

**Lista kroków**
1. Przechodnimy przez przedział od 1 do √n
1. Sprawdzamy czy n jest podzielne przez daną liczbę
1. Jak jest, to dodajemy tą liczbę do s
1. Sprawdzamy czy s jest równe n

## Przykładowy program

```python
import math
def czy_doskonala(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s == n
```
