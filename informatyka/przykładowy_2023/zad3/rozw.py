with open('../Dane_2203/liczby.txt') as f:
    liczby = [[int(j) for j in i.split()] for i in f.readlines()]


def prime(n):
    if n < 2: return False
    if n < 4: return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def potega(a, x, M = None):
    if x == 0:
    	return 1
    if x % 2 == 0:
    	tmp = potega(a, x // 2, M)
    	return (tmp * tmp) % M
    if x % 2 == 1:
    	tmp = potega(a, (x - 1) // 2, M)
    	return (a * tmp * tmp) % M


count = 0
for l in liczby:
    M = l[0]
    if prime(M):
        count += 1

print(count)


count = 0
for l in liczby:
    M = l[0]
    a = l[1]
    if nwd(M, a) == 1:
        count += 1

print(count)


count = 0
for l in liczby:
    M, a, b = l

    for x in range(0, M):
        if potega(a, x, M) == b:
            count += 1
            break

print(count)
