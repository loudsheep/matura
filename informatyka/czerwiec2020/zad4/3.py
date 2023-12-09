with open('../Dane_PR2/pary.txt') as f:
    pary = [i.strip().split() for i in f.readlines()]


def pair_is_smaller(p1, p2):
    if int(p1[0]) < int(p2[0]):
        return True

    if int(p1[0]) == int(p2[0]):
        return False

    r = [p1[1], p2[1]]
    r = sorted(r)

    return p1[1] == r[0]
        


eq = []
for p in pary:
    if int(p[0]) == len(p[1]):
        eq.append(p)


i = 0
while i < len(eq) - 1:
    j = i + 1
    while j < len(eq):
        if not pair_is_smaller(eq[i], eq[j]):
            i = j
            break
        
        j += 1

print(eq[i])
