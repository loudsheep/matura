with open('../Dane_2212/mecz.txt') as f:
    gra = f.readline().strip()


a_pts = 0
b_pts = 0

for i in gra:
    if i == "A":
        a_pts += 1
    elif i == "B":
        b_pts += 1

    if a_pts >= 1000 or b_pts >= 1000:
        if abs(a_pts - b_pts) >= 3:
            break

print(a_pts, b_pts)
