with open('../../dane/61/bledne.txt') as f:
    ciagi = [[int(j) for j in i.split()] for i in f.readlines()[1::2]]

def count_elem(arr, elem):
    count = 0
    for e in arr:
        if e == elem:
            count += 1
    return count

def majority(arr):
    max_no = 0
    max_count = 0

    for i in arr:
        cou = count_elem(arr, i)
        if cou > max_count:
            max_count = cou
            max_no = i
    
    return max_no, max_count


roznice = []
for c in ciagi:
    r = []

    for w in range(len(c) - 1):
        r.append(c[w + 1] - c[w])

    roznice.append(r)

    s = set(r)
    max_no, max_max_count = majority(r)
    # piwerszy badz ostatni jest bledem
    if len(s) == 2:
        if r[0] == max_no:
            print(c[-1])
        else:
            print(c[0])
    else:
        for rr in range(len(r)):
            if r[rr] != max_no:
                print(c[rr+1])
                break
                




































        
