def odbicie(n):
    return int(str(n)[::-1])

with open('../DANE/liczby.txt') as f:
    liczby = [int(i.strip()) for i in f.readlines()]



for li in liczby:
    odw = odbicie(li)

    if odw % 17 == 0:
        print(odw)
