with open('../Dane_PR/dane.txt') as f:
    rows = [[int(j) for j in i.strip().split()] for i in f.readlines()]


print(min([min(i) for i in rows]))
print(max([max(i) for i in rows]))