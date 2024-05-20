with open('../DANE/dane3.txt') as f:
    ranges = [[int(j) for j in i.strip().split()] for i in f.readlines()]


def contains(A, B):
    # check if A contains B (B is inside A)
    # (a0,a1) , (b0, b1)
    return B[0] >= A[0] and B[1] <= A[1]



import collections

lengths = []
for r in ranges:
    lengths.append((r[0], r[1], r[1] - r[0] + 1))

lengths = sorted(lengths, key= lambda x: x[2])



max_len = 0
for r1 in range(len(lengths) - 1):
    current_len = 0
    last_ciag = lengths[r1]
    for r2 in range(r1 + 1, len(lengths)):
        if contains(lengths[r2], last_ciag):
            current_len += 1
            last_ciag = lengths[r2]
    max_len = max(max_len, current_len)

print(max_len)
        

