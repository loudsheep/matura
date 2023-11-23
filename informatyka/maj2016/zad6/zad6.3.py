with open('../Dane_NOWA/dane_6_3.txt') as f:
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

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = []
for s in szyfry:
    w1, w2 = s

    diff = find_in_str(letters, w2[0]) - find_in_str(letters, w1[0])
    if encode(w1, diff) != w2:
        res.append(w1 + "\n")

with open('wyniki_6_3.txt', 'w') as f:
    f.writelines(res)
