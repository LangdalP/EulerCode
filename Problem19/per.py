

"""
You are given the following information, but you may prefer to do some research for yourself.

    1. Jan 1900 was a Monday.
    Thirty days has September, April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1. Jan 1901 to 31. Dec 2000)?
"""
daysInMonthNormal = [31,28,31,30,31,30,31,31,30,31,30,31]
daysInMonthLeap = [31,29,31,30,31,30,31,31,30,31,30,31]

def getNumDaysEachMonth(n):
	global daysInMonthLeap, daysInMonthNormal
	if (n % 100 == 0 and n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
		return daysInMonthLeap
	return daysInMonthNormal

def findStartDay(year):
	year0 = 1900
	days = 0
	daysInMonth = getNumDaysEachMonth(year0)
	for i in range(0, 12):
		for j in range(daysInMonth[i]):
			days += 1
	return days

def findDaysInYear(year, days):
	global sundaysFirst
	daysInMonth = getNumDaysEachMonth(year)
	#print(daysInMonth)
	for i in range(0, 12):
		for j in range(daysInMonth[i]):
			days += 1
			if j == 0 and days % 7 == 0:
				#print(year, i, days-365, j)
				sundaysFirst += 1
	return days



sundaysFirst = 0
startYear = 1901
endYear = 2000
days = findStartDay(startYear)
for i in range(startYear, endYear+1):
	days = findDaysInYear(i, days)
	print(i, days, sundaysFirst)
