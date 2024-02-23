with open("../../dane/66/trojki.txt") as f:
    trojki = [[j for j in i.strip().split()] for i in f.readlines()]


def check_tri(row):
    a = int(row[0])
    b = int(row[1])
    c = int(row[2])

    # liczby nie musza byc posortowane
    # c musi byc najwieksze
    a, b, c = sorted([a, b, c])

    return a + b > c


longest = 0
current = 0
count = 0
for t in trojki:
    if check_tri(t):
        current += 1
        count += 1
    else:
        longest = max(longest, current)
        current = 0

longest = max(longest, current)

print(count, longest)
        
