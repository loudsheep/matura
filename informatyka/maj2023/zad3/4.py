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



def longest_ros(idx):
    for r in range(idx, len(pi) - 1):
        if pi[r] >= pi[r + 1]:
            return r
    return len(pi) - 1

def longest_mal(idx):
    for r in range(idx, len(pi) - 1):
        if pi[r] <= pi[r + 1]:
            return r
    return len(pi) - 1


longest = ""
longest_start = 0

for i in range(len(pi) - 1):
    ros = longest_ros(i)
    if ros > i:
        mal = longest_mal(ros + 1)
        ciag = pi[i:mal+1]
        if len(ciag) > len(longest):
            longest = "".join([str(x) for x in ciag])
            longest_start = i + 1

print(longest, longest_start)



