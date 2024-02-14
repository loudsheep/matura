with open('../../dane/58/dane_systemy1.txt') as f:
    s1 = [i.strip().split() for i in f.readlines()]

with open('../../dane/58/dane_systemy2.txt') as f:
    s2 = [i.strip().split() for i in f.readlines()]

with open('../../dane/58/dane_systemy3.txt') as f:
    s3 = [i.strip().split() for i in f.readlines()]


idx = 0
count = 0
while idx < len(s1):
    expected = 12 + 24 * idx

    d1 = int(s1[idx][0], 2)
    d2 = int(s2[idx][0], 4)
    d3 = int(s3[idx][0], 8)

    if d1 != expected and d2 != expected and d3 != expected:
        count += 1

    idx += 1

print(count)