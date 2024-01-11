with open('../DANE/identyfikator.txt') as f:
    dokumenty = [i.strip() for i in f.readlines()]


def letter_to_digit(letter):
    return ord(letter) - ord('A') + 10


weights = [7,3,1,7,3,1,7,3]
def doc_to_sum(doc):
    letters = doc[:3]
    digits = doc[4:]

    values = []
    for l in letters:
        values.append(letter_to_digit(l))

    for d in digits:
        values.append(int(d))

    sum_all = 0
    for i in range(len(values)):
        sum_all += values[i] * weights[i]

    return sum_all % 10


result = []
for dok in dokumenty:
    control_digit = int(dok[3])
    control_sum = doc_to_sum(dok)

    if control_digit != control_sum:
        result.append(dok)


with open('wyniki4_3.txt', 'w') as f:
    f.write("\n".join(result))
