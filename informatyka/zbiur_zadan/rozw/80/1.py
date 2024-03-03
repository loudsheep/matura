with open("../../dane/80/dane_trojkaty.txt") as f:
    boki = [int(i.strip()) for i in f.readlines()]

def right_triangle(b1, b2, b3):
    # b1 ma być najmniejszy, b3 - największy
    b1, b2, b3 = sorted([b1, b2, b3])

    return b1 * b1 + b2 * b2 == b3 * b3


for i in range(len(boki) - 3):
    b1, b2, b3 = boki[i:i+3]
    if right_triangle(b1, b2, b3):
        print(b1, b2, b3)
