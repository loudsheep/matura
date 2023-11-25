with open('../../dane/69/dane_geny.txt') as f:
    genes = [i.strip() for i in f.readlines()]



def find_genes(genotype):
    res = []
    current = ""

    for i in range(1, len(genotype)):
        if genotype[i-1] + genotype[i] == "BB":
            if current != "":
                current += "B"
                res.append(current)
                current = ""
                continue
        if genotype[i-1] + genotype[i] == "AA":
            if current == "":
                current = "AA"
                continue

        if current != "":
            current += genotype[i]

    return res




max_genes = 0
max_len = 0
for g in genes:
    found = find_genes(g)

    if len(found) > max_genes:
        max_genes = len(found)

    for f in found:
        if len(f) > max_len:
            max_len = len(f)


print(max_genes)
print(max_len)
