def letter2idx(letter):
    return ord(letter) - 65

def idx2letter(idx):
    return chr(idx + 65)

def decrypt(text, key):
    skip = " .,"
    result = ""

    key_idx = 0
    for T in text:
        if T in skip:
            result += T
            continue
        key_letter = letter2idx(key[key_idx % len(key)])
        text_letter = letter2idx(T)
        result += idx2letter((text_letter - key_letter) % 26)
        key_idx += 1

    return result


with open("../../dane/77/szyfr.txt") as f:
    word, key = [i.strip() for i in f.readlines()]

skip = " .,"

import collections
result = [(item, count) for item, count in collections.Counter(word).items() if item not in skip]
result = {key:value for key, value in result}

print(result)


n = sum(result[k] for k in result)
k0 = 0

for k in result:
    k0 += result[k] * (result[k] - 1)

k0 /= n * (n - 1)

d = 0.0285 / (k0 - 0.0385)

print(round(d, 2), len(key))


