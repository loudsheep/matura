with open('../Dane_NOWA/punkty.txt') as f:
    points = [[int(j) for j in i.strip().split()] for i in f.readlines()]


S = [200, 200]
r = 200

n_points = len(points) + 1

count_sq = len(points[:n_points])
count_ci = 0

for p in points[:n_points]:
    dist = (p[0] - S[0])**2 + (p[1] - S[1])**2

    if dist <= r * r:
        count_ci += 1



print(round((4 * count_ci) / count_sq, 4))
