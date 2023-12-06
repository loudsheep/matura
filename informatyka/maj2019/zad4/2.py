with open('../Dane_PR/liczby.txt') as f:
    liczby = [int(i) for i in f.readlines()]



factorial = [1, 1]
for i in range(2, 10):
    factorial.append(i * factorial[i-1])



for i in liczby:
    x = 0
    for c in str(i):
        x += factorial[int(c)]

    if x == i:
        print(i)


