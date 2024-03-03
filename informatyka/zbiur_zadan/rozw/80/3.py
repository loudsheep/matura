with open("../../dane/80/dane_trojkaty.txt") as f:
    boki = [int(i.strip()) for i in f.readlines()]

def is_triangle(b1, b2, b3):
    # b1 ma być najmniejszy, b3 - największy
    b1, b2, b3 = sorted([b1, b2, b3])

    return b1 + b2 > b3


count = 0
for i in range(len(boki) - 2):
    for j in range(i + 1, len(boki) - 1):
        for k in range(j + 1, len(boki)):
            b1 = boki[i]
            b2 = boki[j]
            b3 = boki[k]

            if is_triangle(b1, b2, b3):
                count += 1

print(count)
