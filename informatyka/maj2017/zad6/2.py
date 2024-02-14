with open('../Dane_PR/dane.txt') as f:
    rows = [[int(j) for j in i.strip().split()] for i in f.readlines()]

count = 0
for r in rows:
    for i in range(len(r)):
        if r[i] != r[-i - 1]:
            count += 1
            break

print(count)