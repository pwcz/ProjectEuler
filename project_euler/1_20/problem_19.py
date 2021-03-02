def get_number_of_days(year: int):
    return 31, (29 if year % 4 == 0 and year % 400 != 0 else 28), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31


first_day = (0 + sum(get_number_of_days(1900))) % 7

result = 0

for year in range(1901, 2001):
    for days in get_number_of_days(year):
        if first_day == 0:
            result += 1
        first_day = (first_day + days) % 7

print(result)
