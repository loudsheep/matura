with open('../DANE_2105/wodociagi.txt') as f:
    wodociagi = [i.strip().split(";") for i in f.readlines()][1:]



def zurzycie_roczne(row):
    s = 0
    for i in range(1, len(row)):
        s += int(row[i])
    return s

obj = {}
for w in wodociagi:
    dziel = w[0][-3:]
    if dziel in obj:
        obj[dziel] += zurzycie_roczne(w)
    else:
        obj[dziel] = zurzycie_roczne(w)


for k in obj:
    print(k, obj[k])
