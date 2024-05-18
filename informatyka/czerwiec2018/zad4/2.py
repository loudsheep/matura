with open('../NM_DANE_PR/dane1.txt') as f:
    dane1 = [[int(j) for j in i.strip().split()] for i in f.readlines()]

with open('../NM_DANE_PR/dane2.txt') as f:
    dane2 = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def count_even(ciag):
    c = 0
    for i in ciag:
        if i % 2 == 0:
            c += 1
    return c

def count_odd(ciag):
    c = 0
    for i in ciag:
        if i % 2 != 0:
            c += 1
    return c



count = 0
for r in range(len(dane1)):
    if count_even(dane1[r]) != count_odd(dane1[r]):
        continue

    if count_even(dane2[r]) != count_odd(dane2[r]):
        continue

    count += 1

print(count)
