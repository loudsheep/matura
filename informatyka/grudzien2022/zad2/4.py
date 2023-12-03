with open('../Dane_2212/pary.txt') as f:
    pary = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def check_pair(x, y):
    if x > y:
        return False

    left = x * 2
    right = x * 2 + 1
    while left < 100_000 and right < 100_000:
        if left <= y <= right:
            return True

        if right > y:
            break

        left *= 2
        right = 2 * right + 1
    return False


for p in pary:
    if check_pair(p[0], p[1]):
        print(p[0], p[1])

    
