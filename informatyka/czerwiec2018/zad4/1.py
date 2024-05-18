with open('../NM_DANE_PR/dane1.txt') as f:
    dane1 = [[int(j) for j in i.strip().split()] for i in f.readlines()]

with open('../NM_DANE_PR/dane2.txt') as f:
    dane2 = [[int(j) for j in i.strip().split()] for i in f.readlines()]


r = 0

count = 0
while r < len(dane1):
    if dane1[r][-1] == dane2[r][-1]:
        count += 1
    r += 1

print(count)
