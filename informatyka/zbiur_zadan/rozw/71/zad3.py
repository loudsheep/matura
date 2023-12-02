with open('../../dane/71/funkcja.txt') as f:
    funkcje = [[float(j) for j in i.strip().split()] for i in f.readlines()]


def createF(a, x):
    return a[0] + a[1] * x + a[2] * x * x + a[3] * x * x * x


def f(x):
    if x < 1:
        return createF(funkcje[0], x)
    if x < 2:
        return createF(funkcje[1], x)
    if x < 3:
        return createF(funkcje[2], x)
    if x < 4:
        return createF(funkcje[3], x)
    if x < 5:
        return createF(funkcje[4], x)



i = 0
res = []
while i < 5:
    if round(f(i), 4) == 0:
        res.append(round(i, 5))

    i += 0.00001


print(res)
