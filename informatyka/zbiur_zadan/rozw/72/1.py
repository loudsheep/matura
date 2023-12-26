with open('../../dane/72/napisy.txt') as f:
    napisy = [[j for j in i.strip().split()] for i in f.readlines()]


def minmax(n):
    n1, n2 = len(n[0]), len(n[1])

    return min(n1, n2), max(n1, n2)


count = 0
for i in napisy:
    minN, maxN = minmax(i)

    if maxN / minN >= 3:
        if count == 0:
            print(" ".join(i))
        count += 1

print(count)
