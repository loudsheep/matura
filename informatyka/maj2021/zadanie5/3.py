with open('../DANE_2105/wodociagi.txt') as f:
    wodociagi = [i.strip().split(";") for i in f.readlines()][1:]



def zurzycie_roczne(row):
    s = 0
    for i in range(1, len(row)):
        s += int(row[i])
    return s

def zuz_mies(row):
    zuz = []
    for i in range(1, len(row)):
        zuz.append(int(row[i]))
    return zuz

def add_to_dziel(zuz, dziel):
    for i in range(min(len(zuz), len(dziel))):
        dziel[i] += zuz[i]


obj = {}
for w in wodociagi:
    dziel = w[0][-3:]

    z = zuz_mies(w)

    if dziel in obj:
        add_to_dziel(z, obj[dziel])
    else:
        obj[dziel] = z

for k in obj:
    v = obj[k]

    print(k, max(v))

