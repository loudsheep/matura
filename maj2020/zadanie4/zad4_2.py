def prime_factors(num):
    arr = []
    i = 2
    while i <= num and num > 1:
        if num % i == 0:
            arr.append(i)
            num //= i
        else:
            i += 1
    return arr


# length of factors array
most_factors = 0
# number that has those factors
most_factors_number = 0

most_different = 0
most_different_number = 0

with open('../Dane_2205/liczby.txt', 'r') as file:
    line = file.readline().strip()
    while line:
        n = int(line)
        p = prime_factors(n)
        f = len(p)
        d = len(set(p))

        if f > most_factors:
            most_factors = f
            most_factors_number = n

        if d > most_different:
            most_different = d
            most_different_number = n

        line = file.readline().strip()

print(most_factors_number, most_factors, most_different_number, most_different)
