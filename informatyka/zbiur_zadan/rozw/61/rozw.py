with open('../../dane/61/ciagi.txt') as f:
    ciagi = [[int(j) for j in i.split()] for i in f.readlines()[1::2]]


count = 0
max_r = 0
for c in ciagi:
    r = c[1] - c[0]

    correct = True
    for i in range(len(c) - 1):
        if c[i + 1] - c[i] != r:
            correct = False
            break
    if correct:
        count += 1
        if r > max_r:
            max_r = r

print(count, max_r)

cubes = [i**3 for i in range(1, 101) if i**3 <= 1_000_000]
print(cubes)

for c in ciagi:
    for w in c[::-1]:
        if w in cubes:
            print(w)
            break

