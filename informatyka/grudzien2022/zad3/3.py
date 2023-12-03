with open('../Dane_2212/liczby.txt') as f:
    liczby = [int(i) for i in f.readlines()]



def sito(n):
    sito = [False, False] + [True for i in range(2, n + 1)]

    for i in range(2, n + 1):
        if sito[i]:
            j = i * i
            while j <= n:
                sito[j] = False
                j += i

    return sito


primes_sito = sito(1_000_000)
max_roz = 0
max_x = 0

min_roz = float('inf')
min_x = 0

for l in liczby:
    c = 0

    a = 2
    b = l - a
    while a <= b:
        if primes_sito[a] and primes_sito[b]:
            c += 1
        a += 1
        b = l - a

    if c > max_roz:
        max_roz = c
        max_x = l
    elif c < min_roz:
        min_roz = c
        min_x = l

print(max_x, max_roz)
print(min_x, min_roz)
            

    
