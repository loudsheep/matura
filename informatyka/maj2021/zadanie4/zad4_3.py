with open('../DANE_2105/instrukcje.txt', 'r') as file:
    instrukcje = [i.strip() for i in file.readlines()]


litery = []
for i in instrukcje:
    typ, litera = i.split(' ')

    litery.append(litera)


max = 0
max_litera = ""

for i in set(litery):
    c = litery.count(i)
    if c > max:
        max = c
        max_litera = i


print(max_litera, max)