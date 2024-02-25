with open("../../dane/91/pesele.txt") as f:
    dane = [i.strip().split(";") for i in f.readlines()[1:]]


def ident(row):
    return row[2][0] + row[1][:3] + row[0][-1]

ids = [ident(i) for i in dane]

import collections
res = [item for item, count in collections.Counter(ids).items() if count > 1]

res = sorted(res)
print("\n".join(res))
