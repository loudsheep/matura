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

print(decrypt(word, key))
