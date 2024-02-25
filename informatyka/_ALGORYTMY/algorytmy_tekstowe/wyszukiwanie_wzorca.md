# Wyszukiwania Wzorca
Algorytm N – naiwny – ustawia okno o długości wzorca p na pierwszej pozycji w łańcuchu s. Następnie sprawdza, czy zawartość tego okna jest równa wzorcowi p. Jeśli tak, pozycja okna jest zwracana jako wynik, po czym okno przesuwa się o jedną pozycję w prawo i cała procedura powtarza się.

## Algorytm
**Wejście:**
* s - łańcuch znakowy
* p - łańcuch wzorca

**Wyjscie:**
* pierwsza pozycja łańcucha p w łańcuchu s, lub -1 gdy nie znaleziono

**Zmienne pomocnicze**
* i : pozycja okna, i  ∈ N.
* n : długość łańcucha s, n  ∈ N.
* m : długość wzorca p, m  ∈ N.

## Przykładowy program

```python
def sub_str(s, p):
    n = len(s)
    m = len(p)
    for i in range(n - m):
        if p == s[i:(i + m)]:
            return i
    return -1
```
