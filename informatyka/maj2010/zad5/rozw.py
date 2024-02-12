with open('../Dane/pesel.txt') as f:
    pesel = [i.strip() for i in f.readlines()]



def kontr(p):
    weights = [1,3,7,9]

    idx = 0
    s = 0
    while idx < 10:
        s += int(p[idx]) * weights[idx % len(weights)]
        idx += 1

    s %= 10
    return str((10 - s) % 10)


result = []
for pes in pesel:
    if kontr(pes) != pes[-1]:
        result.append(pes)

result.sort()

print("\n".join(result))
