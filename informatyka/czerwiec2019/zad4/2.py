with open("../DANE/pierwsze.txt") as f:
    liczby = [int(i.strip()) for i in f.readlines()]

def is_prime(n):
    for d in range(2, n // 2 + 1):
        if n % d == 0:
            return False
    return True

res = []
for l in liczby:
    l_rev = int(str(l)[::-1])

    if is_prime(l_rev):
        res.append(str(l))
        print(l)

with open("wyniki4_2.txt", "w") as f:
    f.write("\n".join(res))
