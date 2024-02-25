with open("../../dane/91/pesele.txt") as f:
    dane = [i.strip().split(";") for i in f.readlines()[1:]]

im_naz = [d[1] + d[2] for d in dane]

import collections
# find only duplicates
duplicates = [row for row, count in collections.Counter(im_naz).items() if count > 1]

for d in dane:
    if d[1] + d[2] in duplicates:
        print(" ".join(d))
