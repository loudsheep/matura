def suma_cyfr(x):
    s = 0
    for c in str(x):
        s += int(c)
    return s

def osiagalna(n):
    for i in range(1, 36 + 1):
        k = n - i
        if suma_cyfr(k) == i:
            return k
    print("NIE")


print(osiagalna(505))
