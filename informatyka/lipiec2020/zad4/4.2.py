with open('../DANE/identyfikator.txt') as f:
    dokumenty = [i.strip() for i in f.readlines()]


result = []
for dok in dokumenty:
    left, right = dok[:3], dok[3:]

    if left == left[::-1] or right == right[::-1]:
        result.append(dok)

with open('wyniki4_2.txt', 'w') as f:
    f.write("\n".join(result))
