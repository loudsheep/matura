with open('../../dane/72/napisy.txt') as f:
    napisy = [[j for j in i.strip().split()] for i in f.readlines()]


def maxend(n):
    l = min(len(n[0]), len(n[1]))

    c = 0
    for x in range(1, l + 1):
        if n[0][-x] == n[1][-x]:
            c += 1
        else:
            return c
    return c


same = []
max_e = 0
for i in napisy:
    end = maxend(i)

    if end > 0:
        if end > max_e:
            max_e = end
        same.append([i[0], i[1], end])

print(max_e)

for s in same:
    if s[2] == max_e:
        print(s[0], s[1])
        
