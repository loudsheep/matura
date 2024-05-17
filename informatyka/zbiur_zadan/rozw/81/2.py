with open('../../dane/81/wspolrzedne.txt') as f:
    punkty = [[int(j) for j in i.strip().split()] for i in f.readlines()]
    
# y = ax + b
# a = (y2 - y1) / (x2 - x1)

# b = y - ax

def is_on_slope(x, y, a, b):
    return y == a * x + b

def get_a(x1,y1,x2,y2):
    if x2 == x1:
        return float('inf')
    return (y2 - y1) / (x2 - x1)

def get_b(x, y, a):
    return y - a * x

count = 0
for row in punkty:
    xa, ya, xb, yb, xc, yc = row

    a = get_a(xa,ya,xb,yb)
    b = get_b(xa,ya,a)

    if a == float('inf'):
        if xa == xc:
            count += 1
        continue

    if is_on_slope(xc, yc, a, b):
        count += 1

print(count)
