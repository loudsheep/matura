with open('../Dane_PR/dane.txt') as f:
    rows = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def pixel(x, y, default = -1):
    if 0 <= y < len(rows):
        if 0 <= x < len(rows[y]):
            return rows[y][x]
    return default

def has_contrast(x1, y1, x2, y2):
    p1 = pixel(x1, y1)
    p2 = pixel(x2, y2, p1)

    return abs(p1 - p2) > 128

def contrast(x, y):
    c = 0

    if has_contrast(x, y, x + 1, y):
        c += 1
    if has_contrast(x, y, x - 1, y):
        c += 1
    if has_contrast(x, y, x, y - 1):
        c += 1
    if has_contrast(x, y, x, y + 1):
        c += 1

    return c
    

count = 0
for yy in range(len(rows)):
    for xx in range(len(rows[yy])):
        if contrast(xx, yy) > 0:
            count += 1

print(count)