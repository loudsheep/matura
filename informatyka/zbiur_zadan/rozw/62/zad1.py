with open('../../dane/62/liczby1.txt') as f:
    liczby = [int(i.strip()) for i in f.readlines()]


print(min(liczby), max(liczby))
