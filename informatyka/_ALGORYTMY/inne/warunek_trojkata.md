# Nierówność trójkąta
Czy z trzech podanych liczb reprezentujących długości odcinków można zbudować trójkąt?

## Algorytm
**Wejście:**
* a, b, c - długości odcinków z których konstruujemy trójkąt


**Rozwiązanie**
- suma dwóch krótszych odcinków musi być większa niż najdłuższy odcinek
- lub ogólnie:
```
a + b > c
a + c > b
b + c > a
```

