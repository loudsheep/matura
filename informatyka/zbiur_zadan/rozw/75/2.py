with open('../../dane/75/tekst.txt') as f:
    text = f.read().strip().split()


def chr_to_number(c):
    return ord(c) - 97


def number_to_chr(n):
    return chr(n % 26 + 97)


def encode(word, A, B):
    nums = [chr_to_number(i) * A + B for i in word]
    chars = [number_to_chr(n) for n in nums]

    return "".join(chars)

print(encode('dwa', 1, 3))


for w in text:
    if len(w) >= 10:
        print(encode(w, 5, 2))
