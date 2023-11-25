with open('../../dane/69/dane_geny.txt') as f:
    genes = [i.strip() for i in f.readlines()]

    
result = {}
for g in genes:
    l = len(g)

    if l in result:
        result[l] += 1
    else:
        result[l] = 1

print(len(result))

max_idx = list(result.keys())[0]
for r in result:
    if result[r] > result[max_idx]:
        max_idx = r

print(max_idx, result[max_idx])
