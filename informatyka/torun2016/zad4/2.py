with open("../Dane_2016/dane.txt") as f:
    okregi = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def inside(o1, o2):
    distSq = (o2[1] - o1[1])**2 + (o2[0] - o1[0])**2
    return distSq <= o2[2]**2


max_o = []
max_c = 0
for o in okregi:
    c = 0
    for o2 in okregi:
        if o == o2:
            continue
        if inside(o2, o):
            c += 1
    if c > max_c:
        max_c = c
        max_o = o

res = " ".join([str(x) for x in max_o])
res += "\n" + str(max_c)

with open("wyniki2.txt", "w") as f:
    f.write(res)
