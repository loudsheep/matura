with open('../../dane/73/tekst.txt') as f:
    words = [i for i in f.read().split()]



result = {}
all_sum = 0
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for l in letters:
    result[l] = 0

for word in words:
    for letter in word:
        result[letter] += 1
        all_sum += 1



for letter in result:
    print(letter + ":", result[letter], "(" + str(round(result[letter] / all_sum * 100, 2)) + "%)")
