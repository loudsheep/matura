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


most = 0
poprawne = 0
naprawialne = 0
nieprawidlowy = 0

n = 20

for obr in obrazki:
    rows = count_incorrect_rows(obr)
    cols = count_incorrect_cols(obr)

    if rows == 0 and cols == 0:
        poprawne += 1
    elif rows <= 1 and cols <= 1:
        naprawialne += 1
    else:
        nieprawidlowy += 1

    most = max(most, rows + cols)

print(poprawne)
print(naprawialne)
print(nieprawidlowy)
print(most)


