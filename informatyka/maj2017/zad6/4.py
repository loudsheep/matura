with open('../Dane_PR/dane.txt') as f:
    rows = [[int(j) for j in i.strip().split()] for i in f.readlines()]


longest = 0
current = 0
for x in range(len(rows[0])):
    current = rows[0][x]
    current_start = 0
    for y in range(1, len(rows)):
        if rows[y][x] != current:
            if y - current_start > longest:
                longest = y - current_start
                current = rows[y][x]
                current_start = y
            else:
                current = rows[y][x]
                current_start = y

print(longest)
