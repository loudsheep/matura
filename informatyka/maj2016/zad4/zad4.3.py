with open('../Dane_NOWA/punkty.txt') as f:
    points = [[int(j) for j in i.strip().split()] for i in f.readlines()]


S = [200, 200]
r = 200

def pi_approx(S, r, pts):
    count_sq = len(pts)
    count_ci = 0

    for p in pts:
        dist = (p[0] - S[0])**2 + (p[1] - S[1])**2

        if dist <= r * r:
            count_ci += 1

    return round((4 * count_ci) / count_sq, 4)


import math

result = []
for i in range(1, 1700 + 1):
    pi = pi_approx(S, r, points[:i])
    e = abs(math.pi - pi)

    result.append(str(i) + ";" + str(e) + "\n")

print(result[1000 - 1], result[1700 - 1])

with open('zad4.3csv.csv', 'w') as f:
    f.writelines(result)
