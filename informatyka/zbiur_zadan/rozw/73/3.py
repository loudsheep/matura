with open('../../dane/73/tekst.txt') as f:
    words = [i for i in f.read().split()]


samo = "AEIOUY"
def sub_word(w):
    for s in samo:
        w = w.replace(s, " ")
    return w.split()


def max_len(subs):
    m = 0
    x = ""
    for s in subs:
        if len(s) > m:
            m = len(s)
            x = s
    return x


result = []
max_sub = ""

for word in words:
    sub = max_len(sub_word(word))

    result.append([word, sub])

    if len(sub) > len(max_sub):
        max_sub = sub


c = 0
for r in result:
    if len(r[1]) == len(max_sub):
        c += 1

print(len(max_sub))
print(c)

for r in result:
    if len(r[1]) == len(max_sub):
        print(r[0])
        break
