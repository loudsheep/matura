with open("../../dane/66/trojki.txt") as f:
    trojki = [[j for j in i.strip().split()] for i in f.readlines()]

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


for t in trojki:
    a = is_prime(int(t[0]))
    b = is_prime(int(t[1]))
    c = int(t[0])

    if not a or not b:
        continue

    if int(t[0]) * int(t[1]) == int(t[2]):
        print(" ".join(t))
