with open("../../dane/74/hasla.txt") as f:
    hasla = [i.strip() for i in f.readlines()]




# zad 1
def is_only_numeric(h):
    numeric = "0123456789"
    for c in h:
        if c not in numeric:
            return False
    return True

count = 0
for h in hasla:
    if is_only_numeric(h):
        count += 1
print(count)
            
# zad 2
result = {}
multiple = []
for h in hasla:
    if h in result:
        multiple.append(h)
    else:
        result[h] = 1

multiple = sorted(multiple)
for r in multiple:
    print(r)


# zad 3
def is_frag_ascii(f):
    f = "".join(sorted(list(f)))

    for c in range(len(f) - 1):
        if ord(f[c + 1]) - ord(f[c]) != 1:
            return False
    
    return True

def check_ascii(h):
    if len(h) < 4:
        return False

    for i in range(len(h) - 4 + 1):
        frag = h[i:(i+4)]
        if is_frag_ascii(frag):
            return True

    return False

count = 0
for h in hasla:
    if check_ascii(h):
        count += 1

print(count)

# zad 4
def contains(h, seq):
    for c in h:
        if c in seq:
            return True
    return False

def complexity(h):
    lower = "qwertyuioplkjhgfdsazxcvbnm"
    upper = lower.upper()
    numeric = "1234567890"

    return contains(h, lower) and contains(h, upper) and contains(h, numeric)


count = 0
for h in hasla:
    if complexity(h):
        count += 1

print(count)
