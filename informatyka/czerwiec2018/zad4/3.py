import collections

with open('../NM_DANE_PR/dane1.txt') as f:
    dane1 = [[int(j) for j in i.strip().split()] for i in f.readlines()]

with open('../NM_DANE_PR/dane2.txt') as f:
    dane2 = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def compare(a1, a2):
    if len(a1) != len(a2):
        return False
    a1.sort()
    a2.sort()
    for i in range(len(a1)):
        if a1[i] != a2[i]:
            return False
    return True


count = 0
for r in range(len(dane1)):
    c1 = [item for item, c in collections.Counter(dane1[r]).items()]
    c2 = [item for item, c in collections.Counter(dane2[r]).items()]

    if compare(c1, c2):
        count += 1
        print(r + 1)


print("Count:", count)
