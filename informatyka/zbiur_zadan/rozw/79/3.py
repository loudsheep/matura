with open('../../dane/79/okregi.txt') as f:
    okregi = [[float(j) for j in i.strip().split()] for i in f.readlines()]


count = 0
for i in range(len(okregi) - 1):
    for j in range(i + 1, len(okregi)):
        # skip different radii
        if okregi[i][2] != okregi[j][2]:
            continue

        x1, y1, r1 = okregi[i]
        x2, y2, r2 = okregi[j]

        if x1 == -x2 and y1 == -y2:
            continue
        if x1 == x2 or y1 == y2:
            continue

        if abs(x1) == abs(y2) and abs(y1) == abs(x2):
            count += 1
        

print(count)
        

        

