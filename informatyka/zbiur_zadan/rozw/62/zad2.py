with open('../../dane/62/liczby2.txt') as f:
    liczby = [int(i.strip()) for i in f.readlines()]


sequences = []
current_sequence = []
for i in liczby:
    if len(current_sequence) > 0:
        if i >= current_sequence[-1]:
            current_sequence.append(i)
        else:
            sequences.append(current_sequence)
            current_sequence = [i]
    else:
        current_sequence.append(i)

print(max(sequences, key= lambda x: len(x)))
