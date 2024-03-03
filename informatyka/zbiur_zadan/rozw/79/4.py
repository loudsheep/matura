import math

with open('../../dane/79/okregi.txt') as f:
    okregi = [[float(j) for j in i.strip().split()] for i in f.readlines()]

def dst_sq(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def common_points(o1, o2):
    x1,y1,r1 = o1
    x2,y2,r2 = o2

    dst = dst_sq(x1,y1,x2,y2)
    maxR = max(r1,r2)
    minR = min(r1, r2)
    # jeden okrag jest w środku innego
    if dst < maxR * maxR:
        if math.sqrt(dst) + minR < maxR:
            return 0
        elif math.sqrt(dst) + minR == maxR:
            return 1
        else:
            return 2

    R = (r1 + r2) ** 2
    return dst <= R


chains = []
current_len = 1
last_o = okregi[0]
for i in range(1, 1000):

    is_chain = common_points(okregi[i], last_o) > 0
    if is_chain:
        current_len += 1
        last_o = okregi[i]
    else:
        chains.append(current_len)
        current_len = 1
    last_o = okregi[i]

chains.append(current_len)


print(chains)
print(max(chains))
        

        

