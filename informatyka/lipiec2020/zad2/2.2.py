import math

def rozklad(p, q):
    if p > 0:
        x = math.ceil(q / p)
        p1 = p * x - q
        q1 = q * x
        return [x] + rozklad(p1, q1)
    return []
