def bloki(liczba):
    binarna = liczba

    current = binarna[0]
    bloki = []

    for i in binarna[1:]:
        if i == current[-1]:
            current += i
        else:
            bloki.append(current)
            current = i

    bloki.append(current)

    return len(bloki)


with open('../Dane_2305/bin.txt') as f:
    liczby = [i.strip() for i in f.readlines()]


c = 0
for i in liczby:
    if bloki(i) <= 2:
        c += 1

print(c)
