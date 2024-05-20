with open('../DANE/dane2_3.txt') as f:
    dane = [i.strip() for i in f.readlines()]


def depth(wyr):
    max_d = 0
    current = 0
    for i in wyr:
        if i == "[":
            current += 1
        else:
            current -= 1
        max_d = max(max_d, current)
    return max_d



result = ""
for d in dane:
    result += str(depth(d)) + "\n"


with open("zadanie2_3.txt", "w") as f:
    f.write(result)
