def dec2bin(n):
    res = ""
    while n > 0:
        if n % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
        n //= 2
    return res

def dl(arr):
    c = 0
    for _ in arr:
        c += 1
    return c


def bloki(liczba):
    binarna = dec2bin(liczba)

    current = binarna[0]
    bloki = []

    for i in binarna[1:]:
        if i == current[-1]:
            current += i
        else:
            bloki.append(current)
            current = i

    bloki.append(current)

    return dl(bloki)
