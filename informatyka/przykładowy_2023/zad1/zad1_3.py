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


def get_board_column(board, column_idx):
    res = ""
    for i in board:
        res += i[column_idx]
    return res

def get_board_row(board, row_idx):
    return board[row_idx]

# find pieces that can 'see' each other
# in line '.w...s..'
# the result is 'w...s', then check if first and last pieces are kings and rooks
def seeing_pairs(line):
    res = []
    current = ""
    for i in line:
        if i == ".":
            if current == "":
                continue
            current += "."
        else:
            if current == "":
                current = i
            else:
                current += i
                res.append(current)
                current = i
    return res

def count_checks(pairs):
    white, black = 0, 0
    
    for p in pairs:
        if p[0] == "k" and p[-1] == "W":
            white += 1
        elif p[0] == "W" and p[-1] == "k":
            white += 1
        elif p[0] == "K" and p[-1] == "w":
            black += 1
        elif p[0] == "w" and p[-1] == "K":
            black += 1
    return white, black


white_rook = 0
black_rook = 0
for b in boards:
    for r in range(8):
        row = get_board_row(b, r)

        ww, bb = count_checks(seeing_pairs(row))
        white_rook += ww
        black_rook += bb

    for c in range(8):
        col = get_board_column(b, c)
        
        ww, bb = count_checks(seeing_pairs(col))
        white_rook += ww
        black_rook += bb

print(white_rook, black_rook)

        

        
