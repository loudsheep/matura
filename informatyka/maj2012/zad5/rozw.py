def next_row(row):
    res = [1]
    for i in range(1, len(row)):
        res.append(row[i - 1] + row[i])
    res.append(1)
    return res

def digit_sum(n):
    return len(str(n))

def div5(n):
    if n % 5 == 0:
        return 1
    return 0


pascal = [
    [0],
    [1],
    [1, 1]
]

for i in range(2, 30 + 1):
    pascal.append(next_row(pascal[-1]))

'''
print(max(pascal[10]))
print(max(pascal[20]))
print(max(pascal[30]))
'''

for i in range(1, 30 + 1):
    ss = sum([digit_sum(x) for x in pascal[i]])
    #print(i, "-", ss)

    d5 = sum([div5(x) for x in pascal[i]])
    if d5 == 0:
        print(i)
