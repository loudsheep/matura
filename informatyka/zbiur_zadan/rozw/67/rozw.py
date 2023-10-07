def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def to_bin(n):
    res = ""
    while n >= 1:
        if n % 2 == 0:
            res = "0" + res
        else:
            res = "1" + res
        n //= 2
    return res
        


fib_arr = [0, 1, 1]
def better_fib(n):
    if len(fib_arr) >= n + 1:
        return fib_arr[n]
    elif len(fib_arr) == n:
        res = fib_arr[n - 1] + fib_arr[n - 2]
        fib_arr.append(res)
        return res
    res = better_fib(n - 2) + better_fib(n - 1)
    fib_arr.append(res)
    return res

'''
print("10 -", better_fib(10))
print("20 -", better_fib(20))
print("30 -", better_fib(30))
print("40 -", better_fib(40))
'''


'''
for i in range(1, 41):
    f = better_fib(i)
    if is_prime(f):
        print(i, "-", f)
'''


bin_fib = []
for i in range(1, 41):
    bin_fib.append(to_bin(better_fib(i)))
    
longest = len(bin_fib[-1])
print(longest)

for i in bin_fib:
    r = "0" * (longest - len(i)) + i
    #r = i
    print(r.replace("0", ".").replace("1", "+"))

def count_char(s, c):
    co = 0
    for ss in s:
        if ss == c:
            co += 1
    return co

for i in bin_fib:
    if count_char(i, "1") == 6:
        print(i)


