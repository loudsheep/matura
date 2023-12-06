with open('../Dane_PR/liczby.txt') as f:
    liczby = [int(i) for i in f.readlines()]


def check_if_power_of(n, p):
    if p == 1:
        return True

    while n > 1:
        x = n / p
        if int(x) != x:
            return False
        n //= p

    return True



count = 0
for i in liczby:
    if check_if_power_of(i, 3):
        count += 1

print(count)
