with open('../../dane/75/tekst.txt') as f:
    text = f.read().strip().split()


for w in text:
    if w[0] == w[-1] == "d":
        print(w)
