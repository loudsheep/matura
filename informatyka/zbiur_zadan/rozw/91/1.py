with open("../../dane/91/pesele.txt") as f:
    dane = [i.strip().split(";") for i in f.readlines()[1:]]

# dane => [PESEL, Nazwisko, Imie]

for d in dane:
    if int(d[0][-2]) % 2 == 0:
        if d[2][-1] != "a":
            print(d[2])

