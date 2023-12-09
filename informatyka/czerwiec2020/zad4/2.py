with open('../Dane_PR2/pary.txt') as f:
    pary = [i.strip().split() for i in f.readlines()]


def longest(w):
    longest = w[0]
    current = w[0]

    w += "1"

    i = 1
    while i < len(w):
        if w[i] == current[-1]:
            current += w[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = w[i]
        i += 1

    return longest


for para in pary:
    l = longest(para[1])

    print(l, len(l))
