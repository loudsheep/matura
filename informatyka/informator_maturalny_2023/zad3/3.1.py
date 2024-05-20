with open('../DANE/dane3.txt') as f:
    ranges = [[int(j) for j in i.strip().split()] for i in f.readlines()]



lengths = []
for r in ranges:
    lengths.append(r[1] - r[0] + 1)

lengths = sorted(list(set(lengths)))

print(lengths[:2])
