with open("../../dane/91/pesele.txt") as f:
    dane = [i.strip().split(";") for i in f.readlines()[1:]]


def porz(pesel):
    # cyfry od pozycji 7 do 9
    return int(pesel[6:9])


min_porz = "99999999999"
max_porz = "00000000000"

for d in dane:
    if porz(d[0]) > porz(max_porz):
        max_porz = d[0]

    if porz(d[0]) < porz(min_porz):
        min_porz = d[0]


for d in dane:
    if d[0] == max_porz:
        print("MAX", d[2], d[1])
    if d[0] == min_porz:
        print("MIN", d[2], d[1])
