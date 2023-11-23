def dzielniki(x):
    d = []
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            d.append(i)
    return d


def suma_tablicy(tab):
    s = 0
    for i in tab:
        s += i
    return s

# a = 75
x = suma_tablicy(dzielniki(a))
y = suma_tablicy(dzielniki(x - 1))

if y == a + 1:
    print(x - 1)
else:
    print("NIE")
