def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and not year % 100 == 0:
        return 1
    else:
        return 0