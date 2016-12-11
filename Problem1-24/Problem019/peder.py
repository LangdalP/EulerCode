
MONTH_NAMES = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
NORMAL_YEAR_WEEKDAY_ADVANCE = 1
LEAP_YEAR_WEEKDAY_ADVANCE = 2
# Weekdays are 1 - 7 (monday - sunday)

def is_leap_year(year):
    is_century = year % 100 == 0
    return year % 400 == 0 if is_century else year % 4 == 0

def count_sundays_on_first(from_date, to_date, starting_weekday):
    current_year = from_date[0]
    current_month = from_date[1]
    current_day = from_date[2]
    current_weekday = starting_weekday
    sunday_count = 0
    while (current_year, current_month, current_day) != to_date:
        # print("{yr}-{mn}-{da} // {wda}".format(yr=current_year, mn=current_month, da=current_day, wda=current_weekday))
        if current_weekday == 7 and current_day == 1:
            sunday_count += 1
        # Change day
        current_weekday = current_weekday % 7 + 1
        days_in_month = MONTH_DAYS[current_month - 1]
        if is_leap_year(current_year) and current_month == 2:
            days_in_month = 29
        current_day += 1
        if current_day > days_in_month:
            current_day = 1
            current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1
    
    return sunday_count

if __name__ == "__main__":
    start = (1901, 1, 1)
    end = (2001, 1, 1)
    num_sundays = count_sundays_on_first(start, end, 2)
    print(num_sundays)

