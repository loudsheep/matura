def letter2idx(letter):
    return ord(letter) - 65

def idx2letter(idx):
    return chr(idx + 65)


def encrypt(text, key):
    skip = " .,"
    result = ""

    key_idx = 0
    for T in text:
        if T in skip:
            result += T
            continue
        key_letter = letter2idx(key[key_idx % len(key)])
        text_letter = letter2idx(T)
        result += idx2letter((key_letter + text_letter) % 26)
        key_idx += 1

    return result, key_idx // len(key) + 1


with open("../../dane/77/dokad.txt") as f:
    word = f.readline().strip()

key = "LUBIMYCZYTAC"

new, iterations = encrypt(word, key)

print(new, iterations)
