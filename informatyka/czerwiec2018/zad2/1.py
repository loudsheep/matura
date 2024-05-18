def F(n):
    n1 = 1
    n2 = 1
    for i in range(n - 2):
        n = n1 + n2
        n1 = n2
        n2 = n
    return n2
