first = None
count = 0

with open('../Dane_2205/liczby.txt', 'r') as f:
    line = f.readline().strip()
    while line:
        if line[0] == line[-1]:
            count += 1
            if first is None:
                first = line
        line = f.readline().strip()

print(count, first)
