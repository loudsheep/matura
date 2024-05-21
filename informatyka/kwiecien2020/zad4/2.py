with open('../DANE/dane4.txt') as f:
    dane = [int(i.strip()) for i in f.readlines()]



max_len = 0
first = 0
last = 0

current_first_idx = 0
current_luka = abs(dane[1] - dane[0])

for i in range(1, len(dane) - 1):
    luka = abs(dane[i] - dane[i + 1])

    if luka == current_luka:
        continue

    current_len = i - current_first_idx
    if max_len < current_len:
        max_len = current_len
        first = dane[current_first_idx]
        last = dane[i]

    current_first_idx = i
    current_luka = luka

print(max_len, first, last)
