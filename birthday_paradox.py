# created on 16th july , 2020

import random
import datetime

birth_days = []

i = 0
while i < 50:
    year = random.randint(1895, 2020)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # to know if the year is leap year
        leap = 1
    else:
        leap = 0

    month = random.randint(1, 12)
    if leap == 1 and month == 2:
        day = random.randint(1, 29)
    elif month == 2:
        day = random.randint(1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)
    dd = datetime.date(year, month, day)
    day_of_year = dd.timetuple().tm_yday
    birth_days.append(day_of_year)
    i += 1

birth_days.sort()

previous_i = 0
for i in birth_days:
    if i == previous_i:
        print('*', i)  # this will help us to find the same dates ie if any 2 dates are same the 2nd of those will have a star
    else:
        print(i)
    previous_i = i
