with open('../DANE/DANE_M/anagram.txt') as f:
    liczby = [i.strip() for i in f.readlines()]



def count_in_string(s, c):
    count = 0
    for char in s:
        if c == char:
            count += 1
    return count

zr = 0
nie_zr = 0
for i in liczby:
    c1 = count_in_string(i, '1')
    c2 = count_in_string(i, '0')

    if c1 == c2:
        zr += 1
    elif c1 - c2 == 1 or c2 - c1 == 1:
        nie_zr += 1

print(zr)
print(nie_zr)
