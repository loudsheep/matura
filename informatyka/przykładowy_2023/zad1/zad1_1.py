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
        if ss == c:
            count += 1
    return count


def compare_rows(board):
    first_line = list(board[0])
    for line in board[1:]:
        idx = 0
        while idx < 8:
            if first_line[idx] == line[idx] == ".":
                pass
            else:
                first_line[idx] = "1"
            idx += 1
    return "".join(first_line)


max_col = 0
count_col = 0
for b in boards:
    x = compare_rows(b)
    if count_chars_in_str(x, ".") > 0:
        count_col += 1
        if count_chars_in_str(x, ".") > max_col:
            max_col = count_chars_in_str(x, ".")

print(count_col, max_col)
    
