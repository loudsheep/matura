with open('../DANE_2105/instrukcje.txt', 'r') as file:
    instrukcje = [i.strip() for i in file.readlines()]

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shift(char):
    idx = chars.index(char)
    return chars[(idx + 1) % len(chars)]


ciag = []
for i in instrukcje:
    typ, litera = i.split(' ')

    if typ == "DOPISZ":
        ciag.append(litera)
    elif typ == "ZMIEN":
        ciag[-1] = litera
    elif typ == "USUN":
        del ciag[-1]
    elif typ == "PRZESUN":
        for j in range(len(ciag)):
            if ciag[j] == litera:
                ciag[j] = shift(ciag[j])
                break

print("".join(ciag))
