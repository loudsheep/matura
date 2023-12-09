with open('../Dane_PR2/pary.txt') as f:
    pary = [i.strip().split() for i in f.readlines()]


def is_prime(x):
    if x < 2: return False
    if x == 2: return True

    for i in range(2, (x//2) + 1):
        if x % i == 0:
            return False
    return True


primes = []
for p in range(100):
    if is_prime(p):
        primes.append(p)


def find_diff(num):
    max_diff = 0
    max_pair = []
    for p in primes:
        i = num - p
        if i in primes:
            if abs(i - p) >= max_diff:
                max_diff = abs(i - p)
                max_pair = [p, i]
        if i < 0:
            break
    return max_pair


for para in pary:
    if int(para[0]) % 2 == 0:
        r = find_diff(int(para[0]))
        print(int(para[0]), r[0], r[1])
