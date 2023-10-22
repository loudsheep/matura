#a = [int(i) for i in input().split(", ")]
a = [i for i in range(5, 100 + 1, 5)]

n = len(a)
s = int(input())

b = [False for i in range(s + 1)]

def tura(k):
    for i in range(s, a[k - 1] - 1, -1):
        if b[i - a[k - 1]] and not b[i]:
            b[i] = True



b[0] = True
for i in range(1, n + 1):
    tura(i)


print(b)

count = 0
for i in b:
    if i:
        count += 1
print(count)
