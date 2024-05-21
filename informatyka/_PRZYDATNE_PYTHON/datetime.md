# Data i czas w Pythonie

## Get current date and time
```python
import datetime
now = datetime.datetime.now()

print(now)
# 2024-05-21 08:26:49.219717
```

## Get current date
```python
import datetime
now = datetime.date.today()

print(now)
# 2024-05-21
```

## Create date object to represent date
```python
import datetime
d = datetime.date(2024, 5, 21)

print(d)
# 2024-05-21
```

## Print date's year, month, etc.
```python
import datetime
today = datetime.date.today()

print(today.year)
print(today.month)
print(today.day)
# 2024
# 5
# 21
```

# Time object to represent time
```python
from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)


# a = 00:00:00
# b = 11:34:56
# c = 11:34:56
# d = 11:34:56.234566
```


## Datetime object
```python
from datetime import datetime

# datetime(year, month, day)
a = datetime(2022, 12, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)


# 2022-12-28 00:00:00
# 2022-12-28 23:55:59.342380
```

## Timedelta - represents difference between dates
```python
from datetime import datetime, date

# using date()
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)

t3 = t1 - t2

print("t3 =", t3)

# using datetime()
t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("Type of t3 =", type(t3)) 
print("Type of t6 =", type(t6))  

# t3 = 201 days, 0:00:00
# t6 = -333 days, 1:14:20
# Type of t3 = <class 'datetime.timedelta'>
# Type of t6 = <class 'datetime.timedelta'>
```

## Difference between 2 timedelta objects
```python
from datetime import timedelta

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)

t3 = t1 - t2

print("t3 =", t3)

# t3 = 14 days, 13:55:39
```

## Time duration in seconds
```python
from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())

# Total seconds = 435633.233423
```

## strftime() method - creates string from date, datetime and time object
```python
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# time: 04:34:52
# s1: 12/26/2018, 04:34:52
# s2: 26/12/2018, 04:34:52
```

## strptime() method - creates datetime object from string
```python
from datetime import datetime

date_string = "25 December, 2022"
print("date_string =", date_string)

# use strptime() to create date object
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)

# date_string = 25 december, 2022
# date_object = 2018-06-21 00:00:00
```

Directive | Meaning | Example
--- | --- | ---
`%a`  |  Abbreviated weekday name.    |   Sun, Mon, ...
`%A`  |  Full weekday name.   |   Sunday, Monday, ...
`%w`  |  Weekday as a decimal number. |   0, 1, ..., 6
`%d`  |  Day of the month as a zero-padded decimal.   |   01, 02, ..., 31
`%-d` |  Day of the month as a decimal number.    |   1, 2, ..., 30
`%b`  |  Abbreviated month name.  |   Jan, Feb, ..., Dec
`%B`  |  Full month name. |   January, February, ...
`%m`  |  Month as a zero-padded decimal number.   |   01, 02, ..., 12
`%-m` |  Month as a decimal number.   |   1, 2, ..., 12
`%y`  |  Year without century as a zero-padded decimal number.    |   00, 01, ..., 99
`%-y` |  Year without century as a decimal number.    |   0, 1, ..., 99
`%Y`  |  Year with century as a decimal number.   |   2013, 2019 etc.
`%H`  |  Hour (24-hour clock) as a zero-padded decimal number.    |   00, 01, ..., 23
`%-H` |  Hour (24-hour clock) as a decimal number.    |   0, 1, ..., 23
`%I`  |  Hour (12-hour clock) as a zero-padded decimal number.    |   01, 02, ..., 12
`%-I` |  Hour (12-hour clock) as a decimal number.    |   1, 2, ... 12
`%p`  |  Locale’s AM or PM.   |   AM, PM
`%M`  |  Minute as a zero-padded decimal number.  |   00, 01, ..., 59
`%-M` |  Minute as a decimal number.  |   0, 1, ..., 59
`%S`  |  Second as a zero-padded decimal number.  |   00, 01, ..., 59
`%-S` |  Second as a decimal number.  |   0, 1, ..., 59
`%f`  |  Microsecond as a decimal number, zero-padded on the left.    |   000000 - 999999
`%z`  | UTC offset in the form +HHMM or -HHMM.	 
`%Z`  | Time zone name.	 
`%j`  | Day of the year as a zero-padded decimal number.  |   001, 002, ..., 366
`%-j` | Day of the year as a decimal number.  |   1, 2, ..., 366
`%U`  | Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.  |   00, 01, ..., 53
`%W`  |   Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.    |   00, 01, ..., 53
`%c`  |   Locale’s appropriate date and time representation.  |   Mon Sep 30 07:06:05 2013
`%x`  |   Locale’s appropriate date representation.   |   09/30/13
`%X`  |   Locale’s appropriate time representation.   |   07:06:05
`%%`  |   A literal '%' character.    |   %