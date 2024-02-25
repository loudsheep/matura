# Algorytm Euklidesa (NWD)
Liczba c o powyższej własności nosi nazwę NWD – największego wspólnego dzielnika a i b. NWD znajdujemy za pomocą znanego algorytmu Euklides

## Algorytm
**Wejście:**
* a, b – liczby naturalne, których NWD poszukujemy, a, b ∈ N.

**Wyjscie:**
* NWD liczb a i b

**Lista kroków**
1. pętla dopóki a jest różne od b
1. od większej liczby odejmujemy mniejszą aż się zrównają wtedy dowolna z nich jest NWD

## Przykładowy program

```python
def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
```
