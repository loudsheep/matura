with open('../Dane_NOWA/punkty.txt') as f:
    points = [[int(j) for j in i.strip().split()] for i in f.readlines()]


S = [200, 200]
r = 200

count_edge = 0
count_inside = 0

for p in points:
    dist = (p[0] - S[0])**2 + (p[1] - S[1])**2

    if dist == r * r:
        count_edge += 1
        print(p)
    elif dist < r * r:
        count_inside += 1


print(count_edge)
print(count_inside)
