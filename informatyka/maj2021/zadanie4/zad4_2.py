with open('../DANE_2105/instrukcje.txt', 'r') as file:
    instrukcje = [i.strip() for i in file.readlines()]

longest = 0
longest_typ = ""

last_typ = ""
last_typ_count = 0
for i in instrukcje:
    typ, litera = i.split(' ')

    if typ == last_typ:
        last_typ_count += 1
    else:
        if last_typ_count > longest:
            longest = last_typ_count
            longest_typ = last_typ

            last_typ = typ
            last_typ_count = 1
        else:
            last_typ = typ
            last_typ_count = 1

print(longest_typ, longest)
