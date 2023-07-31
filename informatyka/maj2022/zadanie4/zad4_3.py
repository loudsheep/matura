def numbers_are_different(nums):
    for n1 in range(len(nums) - 1):
        for n2 in range(n1 + 1, len(nums)):
            if nums[n1] == nums[n2]:
                return False

    return True


def numbers_are_ascending(nums):
    for n in range(1, len(nums)):
        if nums[n - 1] > nums[n]:
            return False

    return True


with open('../Dane_2205/liczby.txt', 'r') as file:
    lines = [int(i.strip()) for i in file.readlines()]

len_lines = len(lines)
count = 0

trojki = []
for i in range(len_lines):
    for j in range(len_lines):
        for k in range(len_lines):
            x = lines[i]
            y = lines[j]
            z = lines[k]

            if not numbers_are_different([x, y, z]):
                continue

            if not numbers_are_ascending([x, y, z]):
                continue

            if y % x == 0 and z % y == 0:
                print(x, y, z)
                trojki.append([x, y, z])
                count += 1

print("Trojki:", count)

with open("trojki.txt", "w") as file:
    file.writelines([' '.join(map(str, i)) + "\n" for i in trojki])

count = 0

for t in trojki:
    for i in range(len_lines):
        for j in range(len_lines):
            x = t[0]
            y = t[1]
            z = t[2]
            w = lines[i]
            v = lines[j]

            if not numbers_are_different([x, y, z, w, v]):
                continue

            if not numbers_are_ascending([x, y, z, w, v]):
                continue

            if y % x == 0 and z % y == 0 and w % z == 0 and v % w == 0:
                print(x, y, z, w, v)
                count += 1

print("Piatki:", count)
