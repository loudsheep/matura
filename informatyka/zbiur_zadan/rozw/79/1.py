with open('../../dane/79/okregi.txt') as f:
    okregi = [[float(j) for j in i.strip().split()] for i in f.readlines()]


def quater(x, y):
    if x >= 0 and y >= 0:
        return 1
    if x < 0 and y >= 0:
        return 2
    if x < 0 and y < 0:
        return 3
    return 4
    

def is_contained_in_quater(x, y, r):
    X = abs(x) - r
    Y = abs(y) - r
    
    return X > 0 and Y > 0

result = [0, 0, 0, 0, 0]
for x, y, r in okregi:
    q = quater(x, y)

    if is_contained_in_quater(x, y, r):
        result[q - 1] += 1
    else:
        result[4] += 1

print(" ".join([str(i) for i in result]))
