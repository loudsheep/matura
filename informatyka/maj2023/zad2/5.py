with open('../Dane_2305/bin.txt') as f:
    liczby = [i.strip() for i in f.readlines()]



result = []
for i in liczby:
    print(i)
    dec = int(i, 2)
    dec2 = 0 if i == "1" else int(i[:-1], 2)

    res = dec ^ dec2
    res = bin(res)[2:]

    result.append(res)


with open('wyniki2_5.txt', 'w') as f:
    f.write("\n".join(result))
