def f(n):
    i = 0
    s = 0
    while True:
        l = -2 * (i + 1)
        r = None if i == 0 else -2 * i
        part = str(n)[l:r]

        if part == "":
            break

        s += int(part)
        if len(part) < 2:
            break
        
        i += 1
    return s % 7

