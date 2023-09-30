with open('../../dane/60/liczby.txt') as f:
    liczby = [i.strip() for i in f.readlines()]


zad1 = [i for i in liczby if len(i) <= 3]


print(len(zad1))
print(zad1[-2], zad1[-1])

import math
def find_dividers(n):
    res = []
    for d in range(1, n):
        if n % d == 0:
            res.append(d)
    res.append(n)
    return res


zad2 = [find_dividers(int(i)) for i in liczby]
print('=====================')
for i in zad2:
    if len(i) == 18:
        print(i[-1], end=' ')
        for j in i:
            print(j, end=' ')
        print()

print('=====================')


for i in range(2, 1_000_000):
    count = 0
    j = len(zad2) - 1
    while j >= 0:
        x = zad2[j]

        for y in x[1:]:
            if y == i:
                count += 1

                if count > 1:
                    zad2.remove(x)
                break
        j -= 1
    if count > 1:
        print('eliminated ', i)
    if len(zad2) == 1:
        break

print(zad2)


'''
for i in range(len(zad2) - 1, -1, -1):
    n = zad2[i]

    for j in range(len(zad2)):
        if i == j: continue
'''
        
