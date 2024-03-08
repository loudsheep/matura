with open("../../dane/94/wzrost.txt") as f:
    dane = [i.strip().split(";") for i in f.readlines()[1:]]

def groth(row):
    gr = []
    for i in range(3, len(row)):
        gr.append(int(row[i]) - int(row[i - 1]))
    return gr

d = [0 for _ in range(19)]
ch = [0 for _ in range(19)]

d_count = 0
ch_count = 0

for row in dane:
    gr = groth(row)
    if row[1] == "d":
        d_count += 1
        for i in range(19):
            d[i] += gr[i]
    else:
        ch_count += 1
        for i in range(19):
            ch[i] += gr[i]

for i in range(len(d)):
    d[i] = round(d[i] / d_count, 2)

for i in range(len(ch)):
    ch[i] = round(ch[i] / ch_count, 2)

print(d)
print(ch)
    
