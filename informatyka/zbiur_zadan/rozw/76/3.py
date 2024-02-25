def decifer(A, P):
    A = list(A)
    idx = len(A) - 1
    while idx >= 0:
        pos = P[idx % len(P)]
        A[idx], A[pos - 1] = A[pos - 1], A[idx]
        
        idx -= 1
    return "".join(A)


with open("../../dane/76/szyfr3.txt") as f:
    dane = [i.strip() for i in f.readlines()]

key = [6,2,4,1,5,3]

for d in dane:
    print(decifer(d, key))
