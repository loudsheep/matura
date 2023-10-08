with open('../../dane/65/dane_ulamki.txt') as f:
    ulamki = [i.split() for i in f.readlines()]


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


min_idx = 0
min_value = float('inf')

b = 2*2*3*3*5*5*7*7*13

b_count = 0
c_sum = 0
d_sum = 0

# main loop
for u in range(len(ulamki)):
    up, down = ulamki[u]
    up = int(up)
    down = int(down)

    nd = nwd(up, down)

    value = up / down
    if value < min_value:
        min_value = value
        min_idx = u
    elif value == min_value:
        if int(ulamki[min_idx][1]) > down:
            min_value = value
            min_idx = u

    if nd == 1:
        b_count += 1

    c_sum += up // nd

    d_sum += up * (b // down)


print(ulamki[min_idx])
print(b_count)
print(c_sum)
print(d_sum)























