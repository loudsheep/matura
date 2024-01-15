with open('../Dane/tj.txt') as f:
    words = [i.strip() for i in f.readlines()]

with open('../Dane/klucze1.txt') as f:
    keys = [i.strip() for i in f.readlines()]


def letter_ascii(l):
    return ord(l)

def ascii_letter(a):
    return chr(a)

def letter_code(l):
    return letter_ascii(l) - 64

def code_letter(c):
    return ascii_letter(c + 64)


def encode(word, key):
    k = key
    while len(k) < len(word):
        k += key

    j = 0
    res = ""
    while j < len(word):
        new = letter_ascii(word[j]) + letter_code(k[j])
        if new > 90: new -= 26
        res += ascii_letter(new)
        j += 1

    return res
    

result = []

i = 0
while i < len(words):
    result.append(encode(words[i], keys[i]))
    i += 1

with open('wynik4a.txt', 'w') as f:
    f.write("\n".join(result))
