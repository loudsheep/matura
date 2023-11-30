with open('../../dane/62/liczby1.txt') as f:
    liczby1 = [int(i.strip()) for i in f.readlines()]

with open('../../dane/62/liczby2.txt') as f:
    liczby2 = [int(i.strip()) for i in f.readlines()]


a = 0
b = 0

i = 0
while i < len(liczby1):
    l1 = int(str(liczby1[i]), 8)
    l2 = liczby2[i]

    if l1 == l2:
        a += 1
    elif l1 > l2:
        b += 1
    
    i += 1


print(a, b)
