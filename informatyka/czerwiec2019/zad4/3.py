with open("../DANE/pierwsze.txt") as f:
    liczby = [int(i.strip()) for i in f.readlines()]

def d_sum(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s

res = []
for l in liczby:
    weight = d_sum(l)
    while weight >= 10:
        weight = d_sum(weight)
    if weight == 1:
        res.append(l)
        print(l)

with open("wyniki4_3.txt", "w") as f:
    f.write(str(len(res)))
