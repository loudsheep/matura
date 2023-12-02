def f(x):
    return (x**4 / 500) - (x**2 / 200) - (3 / 250)

def g(x):
    return -(x**3 / 30) + (x / 20) + (1 / 6)

import math
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


top = 19 + (61 / 125)
bottom = -32 - (2 / 3)
left = 2
max_right = 10

precision = 1 / 4


result = 0


i = max_right - precision
while i > left:
    diff = f(i) - g(i)
    if diff < 1:
        break

    result += math.floor(diff)

    i -= precision


print(result)
