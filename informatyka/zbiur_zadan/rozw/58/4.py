import math

with open('../../dane/58/dane_systemy1.txt') as f:
    s1 = [i.strip().split() for i in f.readlines()]


def skok(arr, ii, jj):
    e1 = int(arr[ii][1], 2)
    e2 = int(arr[jj][1], 2)
    return math.ceil(((e1 - e2) ** 2) / abs(i - j))


max_skok = 0

for i in range(len(s1)):
    for j in range(i + 1, len(s1)):
        max_skok = max(max_skok, skok(s1, i, j))

print(max_skok)