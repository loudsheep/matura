with open("../../dane/97/stopa_bezrobocia.txt") as f:
    dane = [[float(j.replace(",", ".")) for j in i.strip().split()] for i in f.readlines()[1:]]

all_stopy = []
for d in dane:
    all_stopy += d[1:]



longest_start = 0
longest_len = 0

current_start = 0
for i in range(1, len(all_stopy)):
    if all_stopy[i - 1] >= all_stopy[i]:
        continue

    ll = i - current_start
    if ll > longest_len:
        longest_start = current_start
        longest_len = ll
    current_start = i

ll = len(all_stopy) - 1 - current_start
if ll > longest_len:
        longest_start = current_start
        longest_len = ll

print(longest_len)
print(1945 + longest_start // 12)
print(longest_start % 12 + 1)
