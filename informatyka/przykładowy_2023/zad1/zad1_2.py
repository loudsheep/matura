with open('../Dane_2203/szachy.txt') as f:
    lines = [i.strip() for i in f.readlines()]


boards = []

tmp = []
for i in lines:
    if i == '' and len(tmp) >= 8:
        boards.append(tmp)
        tmp = []
    else:
        tmp.append(i)

if len(tmp) >= 8:
    boards.append(tmp)


def count_chars_in_str(s, c):
    count = 0
    for ss in s:
        if ss in c:
            count += 1
    return count

def pieces_dict(board):
    white = {}
    black = {}
    for row in board:
        for sq in row:
            if sq != '.' and sq.islower():
                if sq in black:
                    black[sq] += 1
                else:
                    black[sq] = 1
            elif sq != '.' and sq.isupper():
                if sq in white:
                    white[sq] += 1
                else:
                    white[sq] = 1
    return white, black


def dict_sum(d):
    s = 0
    for i in d:
        s += d[i]
    return s


def count_pieces_color(board):
    white, black = pieces_dict(board)

    if len(white) != len(black):
        return False

    for w in white:
        if w.lower() not in black or black[w.lower()] != white[w]:
            return False

    for b in black:
        if b.upper() not in white or white[b.upper()] != black[b]:
            return False

    return dict_sum(white) + dict_sum(black)


min_ = 64
count_ = 0
for board in boards:
    res = count_pieces_color(board)

    if res == False:
        continue

    count_ += 1
    if res < min_:
        min_ = res

print(count_, min_)
    
