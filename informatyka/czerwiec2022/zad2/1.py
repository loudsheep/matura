def Koduj(n):
    if n == 1:
        return ""
    k = n // 2
    if k % 2 == 0:
        return Koduj(k) + "A"
    return "B" + Koduj(k)
