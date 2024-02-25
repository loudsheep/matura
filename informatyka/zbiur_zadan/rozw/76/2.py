def cifer(A, P):
    A = list(A)
    idx = 0
    while idx < len(A):
        pos = P[idx % len(P)]

        A[idx], A[pos - 1] = A[pos - 1], A[idx]
        
        idx += 1
    return "".join(A)


with open("../../dane/76/szyfr2.txt") as f:
    dane = [i.strip() for i in f.readlines()]

key = [int(i) for i in dane[-1].split()]

for d in dane[:-1]:
    print(cifer(d, key))
