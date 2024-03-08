def skrot(wiadomosc):
    S = [ord(i) for i in "ALGORYTM"]
    while len(wiadomosc) % 8 != 0:
        wiadomosc += "."
    print(len(wiadomosc))

    for i in range(0, len(wiadomosc), 8):
        partition = wiadomosc[i:i+8]
        for j in range(8):
            S[j] = (S[j] + ord(partition[j])) % 128
    print(S)

    wynik = ""
    for j in range(8):
        wynik = wynik + chr(65 + S[j] % 26)

    return wynik




with open("../../dane/78/wiadomosci.txt") as f:
    wiadomosci = [i.strip() for i in f.readlines()]


print(skrot(wiadomosci[0]))
