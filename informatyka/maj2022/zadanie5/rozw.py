from datetime import datetime

class Day:
    def __init__(self, row: str) -> None:
        row = row.split()

        self.id = int(row[0])
        self.date = datetime.strptime(row[1], '%d.%m.%Y')
        self.magazine = row[2]
        self.amount = int(row[3])


with open('../Dane_2205/soki.txt') as f:
    rows = [i.strip() for i in f.readlines()]

days = [Day(r) for r in rows[1:]]


# zad. 1
result = {}
for i in days:
    m = i.magazine
    if m in result:
        result[m] += 1
    else:
        result[m] = 1

print(result)

# zad. 2

streak = 0
streak_start = None
current_streak = 0
current_streak_start = None

for i in days:
    if i.magazine == "Ogrodzieniec":
        if current_streak == 0:
            current_streak_start = i.date
        current_streak += 1
    else:
        if current_streak > streak:
            streak = current_streak
            streak_start = current_streak_start
        
        current_streak = 0

print(streak, streak_start)

