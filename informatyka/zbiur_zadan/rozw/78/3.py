def skrot(wiadomosc):
    S = [ord(i) for i in "ALGORYTM"]
    while len(wiadomosc) % 8 != 0:
        wiadomosc += "."

    for i in range(0, len(wiadomosc), 8):
        partition = wiadomosc[i:i+8]
        for j in range(8):
            S[j] = (S[j] + ord(partition[j])) % 128

    wynik = ""
    for j in range(8):
        wynik = wynik + chr(65 + S[j] % 26)

    return wynik

def decrypt(d, n, message):
    for i in range(len(message)):
        message[i] = chr((message[i] * d) % n)
    return "".join(message)


with open("../../dane/78/wiadomosci.txt") as f:
    wiadomosci = [i.strip() for i in f.readlines()]
    
with open("../../dane/78/podpisy.txt") as f:
    podpisy = [[int(j) for j in i.strip().split()] for i in f.readlines()]


for i in range(11):
    wiad = wiadomosci[i]
    pod = podpisy[i]

    skr = skrot(wiad)
    dec = decrypt(3, 200, pod)

    if skr == dec:
        print(i + 1)
