with open('../Dane_2212/mecz.txt') as f:
    gra = f.readline().strip()


i = 1
counter = 0
while i < len(gra):
    if gra[i] != gra[i-1]:
        counter += 1
    i += 1

print(counter)
