with open('../Dane_2212/liczby.txt') as f:
    liczby = [int(i) for i in f.readlines()]



counts = {}
for i in range(10):
    counts[str(i)] = 0

counts["A"] = 0
counts["B"] = 0
counts["C"] = 0
counts["D"] = 0
counts["E"] = 0
counts["F"] = 0

def count_chars(s):
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1


for l in liczby:
    h = str(hex(l)[2:])
    count_chars(h.upper())
    


for k in counts:
    print(k,":", counts[k])
