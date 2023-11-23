with open('../Dane_NOWA/dane_6_2.txt') as f:
    szyfry = [[j for j in i.strip().split()] for i in f.readlines()]


s2 = []
for i in szyfry:
    if len(i) == 2:
        s2.append(i)

szyfry = s2

def find_in_str(string, find):
    for c in range(len(string)):
        if string[c] == find:
            return c
    return -1

def encode(word, key):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    new = ""
    for w in word:
        idx = find_in_str(letters, w)
        new += letters[(idx + key) % len(letters)]

    return new

def decode(word, key):
    return encode(word, -key)


res = [decode(i[0], int(i[1])) + "\n" for i in szyfry]

with open('wyniki_6_2.txt', 'w') as f:
    f.writelines(res)
