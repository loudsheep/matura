with open('../../dane/64/dane_obrazki.txt') as file:
    data = file.readlines()


obrazki = []

current = []

# zamienić obrazki na tablice
for row in data:
    if row.strip() == "":
        obrazki.append(current)
        current = []
    else:
        current.append(row.strip())

# dodać ostatni obrazek do tablicy
obrazki.append(current)


def count_incorrect_rows(obrazek):
    count = 0
    for row in obrazek[:-1]:
        true_count = 0
        for pixel in row[:-1]:
            if pixel == "1":
                true_count += 1
        true_count = "0" if true_count % 2 == 0 else "1"
        if true_count != row[-1]:
            count += 1
    return count

def count_incorrect_cols(obrazek):
    count = 0
    for col in range(len(obrazek) - 1):
        true_count = 0
        for row in range(len(obrazek) - 1):
            if obrazek[row][col] == "1":
                true_count += 1
        true_count = "0" if true_count % 2 == 0 else "1"
        if true_count != obrazek[len(obrazek) - 1][col]:
            count += 1
    return count

def incorrect_row(obrazek):
    rr = 0
    for row in obrazek[:-1]:
        rr += 1
        true_count = 0
        for pixel in row[:-1]:
            if pixel == "1":
                true_count += 1
        true_count = "0" if true_count % 2 == 0 else "1"
        if true_count != row[-1]:
            return rr
    return -1

def incorrect_col(obrazek):
    cc = 0
    for col in range(len(obrazek) - 1):
        cc += 1
        true_count = 0
        for row in range(len(obrazek) - 1):
            if obrazek[row][col] == "1":
                true_count += 1
        true_count = "0" if true_count % 2 == 0 else "1"
        if true_count != obrazek[len(obrazek) - 1][col]:
            return cc
    return -1


n = 20

idx = 0
for obr in obrazki:
    idx += 1
    rows = count_incorrect_rows(obr)
    cols = count_incorrect_cols(obr)

    if rows == 0 and cols == 0:
        continue

    if rows <= 1 and cols <= 1:
        rr = incorrect_row(obr)
        cc = incorrect_col(obr)
        if rows == cols:
            print(idx, "-", rr, cc)
        elif rr >= 0:
            print(idx, "-", rr, n + 1)
        else:
            print(idx, "-", n + 1, cc)



