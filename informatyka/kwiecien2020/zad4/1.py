with open('../DANE/dane4.txt') as f:
    dane = [int(i.strip()) for i in f.readlines()]


min_luka = float('inf')
max_luka = 0

for i in range(len(dane) - 1):
    luka = abs(dane[i] - dane[i + 1])
    min_luka = min(min_luka, luka)
    max_luka = max(max_luka, luka)


print("Max:", max_luka)
print("Min:", min_luka)
