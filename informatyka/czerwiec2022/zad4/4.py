with open('../DANE/liczby.txt') as f:
    liczby = [int(i.strip()) for i in f.readlines()]


rep = list(set(liczby))
print(len(rep))

counter = 0
for li in rep:
    if liczby.count(li) == 2:
        counter += 1

print(counter)


counter = 0
for li in rep:
    if liczby.count(li) == 3:
        counter += 1

print(counter)
