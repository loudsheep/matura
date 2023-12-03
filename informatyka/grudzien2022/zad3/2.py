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


primes = sito(1_000_000)


c = 0
for l in liczby:
    if primes[l - 1]:
        c += 1

print(c)
