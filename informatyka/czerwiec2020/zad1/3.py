def tablice_takie_same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True


# zakładamy że pierwszy element tablicy ma indeks 1
def wycinek_tablicy(arr, od, do):
    if do == 0 or od > len(arr):
        return []

    result = []
    for i in range(1, len(arr) + 1):
        if od <= i <= do:
            result.append(arr[i-1])

    return result

def czy_k_podobne(n, A, B, k):
    a1 = wycinek_tablicy(A, 1, k)
    b1 = wycinek_tablicy(B, n - k + 1, n)

    a2 = wycinek_tablicy(A, k + 1, n)
    b2 = wycinek_tablicy(B, 1, n - k)

    return tablice_takie_same(a1,b1) and tablice_takie_same(a2, b2)


def czy_podobne(n, A, B):
    for k in range(0, n):
        if czy_k_podobne(n, A, B, k):
            return True
    return False
