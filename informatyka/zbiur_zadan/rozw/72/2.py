with open('../../dane/72/napisy.txt') as f:
    napisy = [[j for j in i.strip().split()] for i in f.readlines()]



for i in napisy:
    if len(i[0]) > len(i[1]):
        continue

    if i[1].startswith(i[0]):
        print(i[0], i[1], i[1][len(i[0]):])
