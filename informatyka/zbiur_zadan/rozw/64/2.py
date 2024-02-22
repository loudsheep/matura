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


recuring_count = 0
first = []

def compare(obr1, obr2):
    for i in range(len(obr1)):
        for j in range(len(obr1[i])):
            if obr1[i][j] != obr2[i][j]:
                return False
    return True

def sub_picture(obrazek, rangeCol, rangeRow):
    result = []
    for i in rangeRow:
        tmp = ""
        for j in rangeCol:
            tmp += obrazek[i][j]
        result.append(tmp)
    return result

def is_recuring(obrazek):
    o1 = sub_picture(obrazek, range(0, 10), range(0, 10))
    o2 = sub_picture(obrazek, range(0, 10), range(10, 20))
    o3 = sub_picture(obrazek, range(10, 20), range(0, 10))
    o4 = sub_picture(obrazek, range(10, 20), range(10, 20))

    c1 = compare(o1, o2)
    c2 = compare(o1, o3)
    c3 = compare(o1, o4)

    return c1 and c2 and c3

for obr in obrazki:
    rec = is_recuring(obr)

    if rec:
        recuring_count += 1
        if len(first) == 0:
            first = obr

print(recuring_count)
print("\n".join(first))


