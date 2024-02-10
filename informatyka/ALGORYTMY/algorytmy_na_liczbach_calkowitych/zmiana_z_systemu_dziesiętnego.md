# Zmiana podstawy podanej liczby z dzisiętnego na dowolny
Algorym konwertuje liczbę z systemu dziesiętnego na dowolny inny system liczbowy

## Algorytm
**Wejście:**
* n - liczba w systemie dzisiętnym
* base - podstawa docelowego systemu

**Wyjscie:**
* ciąg znaków zawierający nową liczbę w podanym systemie liczbowym

**Zmienne pomocnicze**
* res - wyniki konwersji

## Przykładowy program

```python
def from_dec(n, base):
    res = ""
    while n > 0:
        res = str(n % base) + res
        n //= base
    return res
```
