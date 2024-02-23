with open("../../dane/66/trojki.txt") as f:
    trojki = [[j for j in i.strip().split()] for i in f.readlines()]

def digit_sum(n):
    s = 0
    for c in str(n):
        s += int(c)
    return s


for t in trojki:
    if digit_sum(t[0]) + digit_sum(t[1]) == int(t[2]):
        print(" ".join(t))
