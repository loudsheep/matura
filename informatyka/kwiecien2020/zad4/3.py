import collections

with open('../DANE/dane4.txt') as f:
    dane = [int(i.strip()) for i in f.readlines()]


luki = [abs(dane[i] - dane[i + 1]) for i in range(len(dane) - 1)]

wyst = [(item, count) for item, count in collections.Counter(luki).items()]

wyst = sorted(wyst, key=lambda x: -x[1])
max_wyst = wyst[0][1]

print("Max k:", max_wyst)
for i in wyst:
    if i[1] == max_wyst:
        print(i[0])


