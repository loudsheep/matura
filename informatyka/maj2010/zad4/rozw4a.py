with open('../Dane/anagram.txt') as f:
    words = [i.strip().split() for i in f.readlines()]


result = []
for w in words:
    l = len(w[0])
    same = True
    for ww in w:
        if len(ww) != l:
            same = False
            break
    if same:
        result.append(" ".join(w))

with open('odp4a.txt', 'w') as f:
    f.write("\n".join(result))
