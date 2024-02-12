with open('../Dane/anagram.txt') as f:
    words = [i.strip().split() for i in f.readlines()]


def is_angram(row):
    letters = {}
    for l in row[0]:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    for w in row[1:]:
        let = {}
        for l in w:
            if l in let:
                let[l] += 1
            else:
                let[l] = 1
        if len(let) != len(letters):
            return False

        for l in letters:
            if not l in let or let[l] != letters[l]:
                return False
    return True


result = []
for w in words:
    l = len(w[0])
    same = True
    for ww in w:
        if len(ww) != l:
            same = False
            break
    if same and is_angram(w):
        result.append(" ".join(w))



with open('odp4b.txt', 'w') as f:
    f.write("\n".join(result))
