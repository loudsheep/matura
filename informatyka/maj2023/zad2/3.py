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
    liczby = [int(i.strip(), 2) for i in f.readlines()]


s = sorted(liczby)

print(s[-1], bin(s[-1]))
