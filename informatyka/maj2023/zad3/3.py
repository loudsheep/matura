with open('../Dane_2305/pi.txt') as f:
    pi = [int(i) for i in f.readlines()]


def ros(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] >= arr[i + 1]:
            return False
        i += 1
    return True


def mal(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] <= arr[i + 1]:
            return False
        i += 1
    return True



def ros_mal(arr):
    for k in range(2, len(arr) - 1):
        if ros(arr[:k]) and mal(arr[k:]):
            return True
    return False


c = 0
j = 0
while j < len(pi) - 6:
    if ros_mal(pi[j:j+6]):
        c += 1
    j += 1


print(c)
