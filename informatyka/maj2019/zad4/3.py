with open('../Dane_PR/liczby.txt') as f:
    liczby = [int(i) for i in f.readlines()]


def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a



def ultra_giga_nwd(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return nwd(arr[0], arr[1])

    return nwd(arr[0], ultra_giga_nwd(arr[1:]))




i = 0
result = (0, 0, 0)
while i < len(liczby) - 1:

    for j in range(i + 1, len(liczby)):
        x = ultra_giga_nwd(liczby[i:j])

        if x > 1:
            if j - i > result[1]:
                result = (liczby[i], j - i, x)
        else:
            break

    i += 1


print(result)
