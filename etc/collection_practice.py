import datetime

day31 = [0, 2, 4, 6, 7, 9, 11]
today = datetime.date.today()
year = today.year
month = today.month


def get_days(month):
    if month in day31:
        days = 31
    elif month == 1:
        if(year % 4 == 0) and (year % 100 != 0) or (year % 400) == 0:
            days = 29
        else:
            days = 28
    else:
        days = 30
    print('{} days for {}-{}'.format(days, year, month+1))
    return days


get_days(month)

