with open("../../dane/68/dane_napisy.txt") as f:
    angramy = [i.split() for i in f.readlines()]

def letter_count(ang):
    res = {}
    for l in ang:
        if l in res:
            res[l] += 1
        else:
            res[l] = 1
    return res


def compare_counts(c1, c2):
    if len(c1) != len(c2):
        return False

    for k in c1:
        if (k not in c2) or (c2[k] != c1[k]):
            return False

    for k in c2:
        if (k not in c1) or (c2[k] != c1[k]):
            return False

    return True


a_count = 0
b_count = 0

# main loop
for i in angramy:
    first, second = i

    if len(first) == len(second):
        if len(letter_count(first)) == len(letter_count(second)) == 1:
            a_count += 1

    if len(first) == len(second):
        fc = letter_count(first)
        sc = letter_count(second)

        if compare_counts(fc, sc):
            b_count += 1


print("1-", a_count)
print("2-", b_count)


all_angram = []
for i in angramy:
    all_angram.append(i[0])
    all_angram.append(i[1])


max_count = 0
for i in range(len(all_angram)):
    c = 1
    for j in range(len(all_angram)):
        if i == j:
            continue

        fc = letter_count(all_angram[i])
        sc = letter_count(all_angram[j])

        if compare_counts(fc, sc):
            c += 1
    if c > max_count:
        max_count = c


print("3-", max_count)
