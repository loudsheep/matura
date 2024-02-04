def odbicie(n):
    return int(str(n)[::-1])

with open('../DANE/liczby.txt') as f:
    liczby = [int(i.strip()) for i in f.readlines()]


def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True



for li in liczby:
    if not is_prime(li):
        continue
    
    odb = odbicie(li)

    if is_prime(odb):
        print(li)
