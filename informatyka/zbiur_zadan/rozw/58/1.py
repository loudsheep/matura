with open('../../dane/58/dane_systemy1.txt') as f:
    s1 = [i.strip().split() for i in f.readlines()]

with open('../../dane/58/dane_systemy2.txt') as f:
    s2 = [i.strip().split() for i in f.readlines()]

with open('../../dane/58/dane_systemy3.txt') as f:
    s3 = [i.strip().split() for i in f.readlines()]


s1min = min([int(i[1], 2) for i in s1])
s2min = min([int(i[1], 4) for i in s2])
s3min = min([int(i[1], 8) for i in s3])

print(bin(s1min), bin(s2min), bin(s3min))