import calendar
import datetime
def leap_year(year):
    year = int(year)
    if (not year % 4 and year % 100) or not year % 400:
        return True
    else:
        return False


def get_day_counts(month, year):
    if leap_year(year):
        if month == 2:
            return 29
        else:
            return calendar.mdays[month]
    else:
        return calendar.mdays[month]


def get_days_list(month,year):
    counts_day = get_day_counts(month,year)
    days_list = []
    for day in range(1,counts_day+1):
        if datetime.date(year,month,day).isoweekday() in [6,7]:
            days_list.append('В')
        else:
            days_list.append(8)
    return days_list



