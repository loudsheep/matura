with open('../DANE/napisy.txt') as f:
    napisy = [i.strip() for i in f.readlines()]



a_count = 0

def count_digits(string):
    c = 0
    for char in string:
        if char in "0123456789":
            c += 1
    return c

def check_for_palindrome(string):
    chars = "QWERTYUIOPLKJHGFDSAZXCVBNM1234567890"

    for c in chars:
        tmp = string + c
        if tmp[::-1] == tmp:
            return tmp

    for c in chars:
        tmp = c + string
        if tmp[::-1] == tmp:
            return tmp
        
    return None

def digits_ascii(string):
    digits = "0123456789"
    dd = ""

    for c in string:
        if c in digits:
            dd += c

    if len(dd) % 2 != 0:
        dd = dd[:-1]

    d = []

    for c in range(0, len(dd) - 1, 2):
        d.append(dd[c] + dd[c + 1])

    res = ""
    for r in d:
        if 65 <= int(r) <= 90:
            res += chr(int(r))

    return res
    
    

b_word = ""
n_idx = 1

c_word = ""
d_word = ""
d_x_count = 0

for i in napisy:
    a_count += count_digits(i)

    if n_idx % 20 == 0 and n_idx > 0:
        b_word += i[(n_idx // 20) - 1]

    n_idx += 1

    pal = check_for_palindrome(i)

    if pal is not None:
        c_word += pal[len(pal) // 2]

    if d_x_count >= 3:
        continue
    
    asc = digits_ascii(i)
    if asc == "X":
        d_x_count += 1
    elif asc != "":
        d_x_count = 0

    d_word += asc

        



print(a_count)
print(b_word)
print(c_word)
print(d_word)
