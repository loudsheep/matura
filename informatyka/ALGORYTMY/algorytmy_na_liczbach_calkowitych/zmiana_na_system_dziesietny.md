# Zmiana podstawy podanej liczby na dziesiętny
Algorym konwertuje liczbę z systemu dowolnego na system dzisiętny

## Algorytm
**Wejście:**
* n - liczba w postaci tekstu
* base - podstawa systemu

**Wyjscie:**
* ciąg znaków zawierający nową liczbę w systemie dzisiętnym

**Zmienne pomocnicze**
* res - wyniki konwersji

**Lista kroków**
1. Krok 1

## Przykładowy program

```python
def to_dec(n, base):
    res = 0
    for i in range(len(n)):
        digit = int(n[len(n) - i - 1])
        res += digit * (base ** i)
    return res

```
