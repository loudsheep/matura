with open("../../dane/66/trojki.txt") as f:
    trojki = [[j for j in i.strip().split()] for i in f.readlines()]


def check_pit(row):
    a = int(row[0])
    b = int(row[1])
    c = int(row[2])

    # liczby nie musza byc posortowane
    # c musi byc najwieksze
    a, b, c = sorted([a, b, c])

    return a * a + b * b == c * c


idx = 0
while idx < len(trojki) - 1:
    t1 = trojki[idx]
    t2 = trojki[idx + 1]

    if check_pit(t1) and check_pit(t2):
        print(" ".join(t1))
        print(" ".join(t2))

    idx += 1
