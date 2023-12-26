with open('../../dane/73/tekst.txt') as f:
    words = [i for i in f.read().split()]


def double_letter(w):
    i = 0
    while i < len(w) - 1:
        if w[i] == w[i + 1]:
            return True
        i += 1
    return False

c = 0
for word in words:
    if double_letter(word):
        c += 1

print(c)
