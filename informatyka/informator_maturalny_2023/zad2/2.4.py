with open('../DANE/dane2_4.txt') as f:
    dane = [i.strip() for i in f.readlines()]


def correct(wyr):
    current = 0
    for i in wyr:
        if i == "[":
            current += 1
        else:
            current -= 1
    return "tak" if current == 0 else "nie"



result = ""
for d in dane:
    result += correct(d) + "\n"


with open("zadanie2_4.txt", "w") as f:
    f.write(result)
