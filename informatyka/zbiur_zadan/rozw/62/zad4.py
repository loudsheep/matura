with open('../../dane/62/liczby2.txt') as f:
    liczby2 = [int(i.strip()) for i in f.readlines()]


def dec2oct(n):
    res = ""

    while n >= 1:
        res = str(n % 8) + res
        n //= 8

    return res


a = 0
b = 0
for i in liczby2:
    for x in str(i):
        if x == "6":
            a += 1

    for x in str(dec2oct(i)):
        if x == "6":
            b += 1

print(a, b)
