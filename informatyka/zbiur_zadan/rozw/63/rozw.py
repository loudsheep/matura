with open('../../dane/63/ciagi.txt') as f:
    ciagi = [i.strip() for i in f.readlines()]

def ones(ciag):
    for i in range(len(ciag) - 1):
        if ciag[i] == ciag[i + 1] == "1":
            return False
    return True



import math
def half_prime(n):
    div = []
    nn = n / 2 + 1
    i = 2
    while i <= nn and n > 1:
        if n % i == 0:
            n //= i
            div.append(i)
            continue
        i += 1
    return len(div) == 2

print(half_prime(6))

a = []
b_count = 0
cc = []

# main loop
for c in ciagi:
    if len(c) % 2 == 0:
        l = len(c) // 2
        if c[:l] == c[l:]:
            a.append(c)


    if ones(c):
        b_count += 1

    if half_prime(int(c, 2)):
        cc.append(int(c, 2))



# print("\n".join(a))
print(b_count)
print(len(cc), min(cc), max(cc))

































