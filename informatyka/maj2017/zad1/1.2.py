def area(n, A, p):
    A.sort(reverse=True)
    i = n - 1
    while i >= 0:
        if A[i] % p == 0:
            del A[i]
        i -= 1

    if len(A) >= 2:
        return A[0] * A[1]
    return 0

