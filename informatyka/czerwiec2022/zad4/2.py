def odbicie(n):
    return int(str(n)[::-1])

with open('../DANE/liczby.txt') as f:
    liczby = [int(i.strip()) for i in f.readlines()]


result = [0, 0, 0]
for li in liczby:
    odb = odbicie(li)

    diff = abs(li - odb)
    if diff > result[0]:
        result = [diff, li, odb]

print(result)
