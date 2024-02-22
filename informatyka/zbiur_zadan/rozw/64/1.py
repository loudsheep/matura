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


rewers_count = 0
max_black = 0


def count_pixel_color(obrazek):
    bl, wh = 0, 0
    # przejdź po wszystkich wierszach oprócz ostatniego
    for row in obrazek[:-1]:
        for pixel in row[:-1]:
            if pixel == "0":
                wh += 1
            else:
                bl += 1
    return bl, wh

for obr in obrazki:
    black, white = count_pixel_color(obr)

    if black > white:
        rewers_count += 1

    max_black = max(max_black, black)

print(rewers_count)
print(max_black)
