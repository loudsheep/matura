with open('../DANE/identyfikator.txt') as f:
    dokumenty = [i.strip() for i in f.readlines()]


def digit_sum(d):
    s = 0
    for c in d:
        s += int(c)
    return s

max_sum = 0

for dok in dokumenty:
    summ = digit_sum(dok[3:])
    max_sum = max(summ, max_sum)

result = []
for dok in dokumenty:
    summ = digit_sum(dok[3:])
    if summ == max_sum:
        result.append(dok)

with open('wyniki4_1.txt', 'w') as f:
    f.write("\n".join(result))
