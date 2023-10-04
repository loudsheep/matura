with open('../DANE/DANE_M/przyklad.txt') as f:
    liczby = [i.strip() for i in f.readlines()]


def count_in_string(s, c):
    count = 0
    for char in s:
        if c == char:
            count += 1
    return count

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def angram(n):
    l = len(n)
    c0 = count_in_string(n, '0')
    c1 = count_in_string(n, '1')

    komb_1 = 
    
    return (c1 - 1)


