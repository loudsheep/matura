with open('../Dane_2305/pi.txt') as f:
    pi = [int(i) for i in f.readlines()]



c = 0
i = 0
while i < len(pi) - 1:
    if int(str(pi[i]) + str(pi[i+1])) > 90:
        c += 1
    i += 1

print(c)
