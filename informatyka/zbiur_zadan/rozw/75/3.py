with open('../../dane/75/probka.txt') as f:
    data = [i.strip().split() for i in f.readlines()]

print(data)
def chr_to_number(c):
    return ord(c) - 97


def number_to_chr(n):
    return chr(n % 26 + 97)


def encode(word, A, B):
    nums = [chr_to_number(i) * A + B for i in word]
    chars = [number_to_chr(n) for n in nums]

    return "".join(chars)


# A -> 
# B -> <0, 25>
def find_key(normal, encoded):
    result = ""
    for B in range(25 + 1):
        for A in range(100):
            if encode(normal, A, B) == encoded:
                result += "klucz szyfrujący: " + str(A) + " " + str(B)
                break
        for A in range(100):
            if encode(encoded, A, B) == normal:
                result += " klucz deszyfrujący: " + str(A) + " " + str(B)
                break
    print(result)


for d in data:
    find_key(d[0], d[1])
