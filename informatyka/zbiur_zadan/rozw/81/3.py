with open('../../dane/81/wspolrzedneTR.txt') as f:
    punkty = [[int(j) for j in i.strip().split('\t')] for i in f.readlines()]
    
# y = ax + b
# a = (y2 - y1) / (x2 - x1)

# b = y - ax
import math

def dist(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

largest_l = 0
largest_w = []
for row in punkty:
    xa, ya, xb, yb, xc, yc = row

    l = dist(xa, ya, xb, yb) + dist(xc, yc, xb, yb) + dist(xa, ya, xc, yc)

    if l > largest_l:
        largest_l = l
        largest_w = row

print(largest_w)
print(round(largest_l, 2))
