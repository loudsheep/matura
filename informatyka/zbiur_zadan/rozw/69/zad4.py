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



strong = 0
resistant = 0

for g in genes:
    if g == g[::-1]:
        strong += 1

    left = "".join(find_genes(g))
    right = "".join(find_genes(g[::-1]))

    if left == right:
        resistant += 1

print(resistant)
print(strong)
