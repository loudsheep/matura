def czynniki(liczba):
    czyn = []
    i = 2
    stop = liczba // 2
    while i <= stop:
        if liczba % i == 0:
            czyn.append(i)
            liczba //= i
        else:
            i += 1

    return czyn

def nie_parz_czynn(liczba):
    if liczba % 2 == 0:
        return False

    czyn = []
    for i in range(3, liczba//2, 2):
        if liczba % i == 0:
            czyn.append(i)

            if len(czyn) > 3:
                return False

    return len(czyn) == 3

def odwroc_liczbe(liczba):
    l_str = str(liczba)
    o_str = ""
    for i in l_str:
        o_str = i + o_str

    return int(o_str)

def w(n):
    l_str = str(n)
    res = 1
    for i in l_str:
        res *= int(i)

    return res


with open('../../dane/59/liczby.txt') as f:
    liczby = f.readlines()

'''
counter = 0
for l in liczby:
    nie_p = nie_parz_czynn(int(l))

    if nie_p:
        counter += 1

print(counter)
'''

print(nie_parz_czynn(1157625))

'''
couter = 0
progress = 0
for l in liczby:
    rozklad = set(czynniki(int(l)))
    progress += 1
    print(progress)

    if len(rozklad) != 3:
        continue

    br = False
    for r in rozklad:
        if r % 2 != 0:
            br = True

    if br:
        continue

    counter += 1

print(couter)
'''


#print(czynniki(985408507))
