with open('../Dane_NOWA/dane_6_1.txt') as f:
    szyfry = [i.strip() for i in f.readlines()]

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


res = [encode(i, 107) + "\n" for i in szyfry]

with open('wyniki_6_1.txt', 'w') as f:
    f.writelines(res)
    
