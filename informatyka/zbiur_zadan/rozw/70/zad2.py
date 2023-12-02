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

precision = 1 / 1000


result = (max_right - left) * 2 + (top - bottom)


i = left + precision
while i <= max_right:
    prevF = (i - precision, f(i - precision))
    prevG = (i - precision, g(i - precision))

    currentF = (i, f(i))
    currentG = (i, g(i))

    distF = dist(prevF[0], prevF[1], currentF[0], currentF[1])
    distG = dist(prevG[0], prevG[1], currentG[0], currentG[1])

    result += distF + distG

    i += precision


print(result)
