# Wyszukiwanie duplikatów w liscie (Pyton)
Wyszukiwanie z użyciem biblioteki `collections`

## Przykład

```python
a = [1,2,3,2,1,5,6,5,5,5]

import collections
print([(item, count) for item, count in collections.Counter(a).items()])
# [(1, 2), (2, 2), (3, 1), (5, 4), (6, 1)]
# wypisuje tablicę tuple (wartosc, liczba_wystapien)
```
