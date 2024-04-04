with open('../Dane_2016/imiennicy.txt') as f:
    nazwiska = [i.strip().split("\t") for i in f.readlines()][1:]


for n in nazwiska:
    if int(n[1]) > int(n[2]):
        print(n[0])


print()

s = sorted(nazwiska, key=lambda x: x[1] + x[2], reverse=True)
print("\n".join([x[0] for x in s[:12]]))
