
with open('../NM_DANE_PR/dane1.txt') as f:
    dane1 = [[int(j) for j in i.strip().split()] for i in f.readlines()]

with open('../NM_DANE_PR/dane2.txt') as f:
    dane2 = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def scalanie(A, B):
    # wskaźniki z pozycją
    a = 0
    b = 0

    result = []
    while a < len(A) and b < len(B):
        if A[a] <= B[b]:
            result.append(A[a])
            a += 1
        else:
            result.append(B[b])
            b += 1
    if a < len(A):
        while a < len(A):
            result.append(A[a])
            a += 1
    if b < len(B):
        while b < len(B):
            result.append(B[b])
            b += 1
            
    return result
    


to_save = ""
for r in range(len(dane1)):
    res = scalanie(dane1[r], dane2[r])
    to_save += " ".join([str(i) for i in res]) + "\n"


with open('wynik4_4.txt', 'w') as f:
    f.write(to_save)


