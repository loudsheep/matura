with open('../../dane/86/dane_wybory.txt') as f:
    dane = [i.strip().split() for i in f.readlines()]

# wiersz: 
# A1 26573 13009 19177 26574 9656

newD = []
regions = "ABCD"

for r in regions:
    new = [r, 0, 0, 0, 0, 0]
    for d in dane:
        if d[0][0] == r:
            new = [r] + [new[i] + int(d[i]) for i in range(1, 5 + 1)]
    newD.append(new)

print(newD)


mandaty = 100

def przydziel(row, do_przy):
    okr = row[0]
    glosy = [int(i) for i in row[1:]]

    m = [0 for _ in row[1:]]
    w = []

    while do_przy > 0:
        w = [glosy[i]/(2 * m[i] + 1) for i in range(5)]
        wMax = max(w)

        for i in range(5):
            if w[i] >= wMax:
                m[i] += 1
                break
        do_przy -= 1

    return m



sumK = [0 for _ in range(5)]

for d in newD:
    res = przydziel(d, mandaty)

    sumK = [sumK[i] + res[i] for i in range(5)]

print(sumK)
