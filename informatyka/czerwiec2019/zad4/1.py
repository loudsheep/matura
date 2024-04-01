with open("../DANE/liczby.txt") as f:
    liczby = [int(i.strip()) for i in f.readlines()]

def is_prime(n):
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            return False
    return True


for l in liczby:
    if not 100 <= l <= 5000:
        continue

    if is_prime(l):
        print(l)
