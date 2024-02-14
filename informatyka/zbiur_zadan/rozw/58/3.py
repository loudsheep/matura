with open('../../dane/58/dane_systemy1.txt') as f:
    s1 = [i.strip().split() for i in f.readlines()]

with open('../../dane/58/dane_systemy2.txt') as f:
    s2 = [i.strip().split() for i in f.readlines()]

with open('../../dane/58/dane_systemy3.txt') as f:
    s3 = [i.strip().split() for i in f.readlines()]


def check_diff(elem1, elem2, base):
    elem1 = int(elem1, base)
    elem2 = int(elem2, base)

    return elem2 - elem1

m1 = int(s1[0][1], 2)
m2 = int(s2[0][1], 4)
m3 = int(s3[0][1], 8)

idx = 0
count = 1
while idx < len(s1):
    r1 = False
    r2 = False
    r3 = False
    if int(s1[idx][1], 2) > m1:
        r1 = True
        m1 = int(s1[idx][1], 2)
    if int(s2[idx][1], 4) > m2:
        r2 = True
        m2 = int(s2[idx][1], 4)
    if int(s3[idx][1], 8) > m3:
        r3 = True
        m3 = int(s3[idx][1], 8)

    if r1 or r2 or r3:
        count += 1

    idx += 1

print(count)