with open('../Dane_2305/pi.txt') as f:
    pi = [int(i) for i in f.readlines()]


pary = {}
for i in "0123456789":
    for j in "0123456789":
        pary[int(i + j)] = 0

i = 0
while i < len(pi) - 1:
    para = int(str(pi[i]) + str(pi[i+1]))
    pary[para] += 1
    
    i += 1

max_c, max_p = 0, float('inf')
min_c, min_p = float('inf'), float('inf')

for k in pary:
    if pary[k] > max_c:
        max_c = pary[k]
        max_p = k
    elif pary[k] == max_c:
        max_p = min(max_p, k)
        
    if pary[k] < min_c:
        min_c = pary[k]
        min_p = k
    elif pary[k] == min_c:
        min_p = min(min_p, k)

print(max_p, max_c)
print(min_p, min_c)
        
        
