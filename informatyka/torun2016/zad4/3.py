with open("../Dane_2016/dane.txt") as f:
    okregi = [[int(j) for j in i.strip().split()] for i in f.readlines()]

def outside(o1, o2):
    RR = o1[2] + o2[2]
    distSq = (o1[1] - o2[1])**2 + (o1[0] - o2[0])**2
    return distSq == RR * RR

def inside(o1, o2):
    RR = abs(o1[2] - o2[2])
    distSq = (o1[1] - o2[1])**2 + (o1[0] - o2[0])**2
    return distSq == RR * RR


result = ""
for o1 in okregi:
    for o2 in okregi:
        if o1 == o2:
            continue
        if outside(o1, o2) or inside(o1, o2):
            result += " ".join([str(x) for x in o1]) + " " + " ".join([str(x) for x in o2])
            result += "\n"

print(result)

with open("wyniki3.txt", "w") as f:
    f.write(result)
