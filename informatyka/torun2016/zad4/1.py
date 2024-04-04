with open("../Dane_2016/dane.txt") as f:
    okregi = [[int(j) for j in i.strip().split()] for i in f.readlines()]


min_r = float('inf')
for o in okregi:
    min_r = min(min_r, o[2])


result = ""
count = 0
for o in okregi:
    if o[2] != min_r:
        continue
    count += 1
    result += " ".join([str(x) for x in o]) + "\n"

result += str(count)

with open("wyniki1.txt", "w") as f:
    f.write(result)
    
