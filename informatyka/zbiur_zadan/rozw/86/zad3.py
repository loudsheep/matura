with open('../../dane/86/dane_wybory.txt') as f:
    dane = [i.strip().split() for i in f.readlines()]

# wiersz: 
# A1 26573 13009 19177 26574 9656

mandaty = 20

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



maxK = [0 for _ in range(5)]

for d in dane:
    res = przydziel(d, mandaty)

    maxK = [max(maxK[i], res[i]) for i in range(5)]

print(maxK)
