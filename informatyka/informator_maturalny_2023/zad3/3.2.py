with open('../DANE/dane3.txt') as f:
    ranges = [[int(j) for j in i.strip().split()] for i in f.readlines()]

import collections

lengths = []
for r in ranges:
    lengths.append(r[1] - r[0] + 1)


lengths = [(item, count) for item, count in collections.Counter(lengths).items()]

lengths = sorted(lengths, key= lambda x: -x[1])

print(lengths[:10])
