with open('../Dane_2212/mecz.txt') as f:
    gra = f.readline().strip()


longest = 0
longest_team = ""
count = 0

current = ""

i = 0
while i < len(gra):
    if current == "":
        current += gra[i]
    elif gra[i] == current[-1]:
        current += gra[i]
    else:
        if len(current) >= 10:
            count += 1
            if len(current) > longest:
                longest = len(current)
                longest_team = current[-1]
            current = gra[i]
        else:
            current = gra[i]
    

    i += 1

print(count, longest_team, longest)
