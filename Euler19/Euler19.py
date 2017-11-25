import time
import math

num_days_dict = {
	1: 31,
	3: 31,
	4: 30,
	5: 31,
	6: 30,
	7: 31,
	8: 31,
	9: 30,
	10:31,
	11:30,
	12:31
}

def determine_num_days(month_num, year_num):
	try:
		return num_days_dict[month_num]
	except:
		if year_num % 4 == 0 and not year_num % 400 == 0:
			return 29
		else:
			return 28

def determine_year_num(index):
	i = 1900
	while i < 2001 and index > 0:
		if i % 4 == 0 and not i % 400 == 0:
			index -= 366
		else:
			index -= 365
		i += 1
	return i


def determine_month_num(index):
	i = 0
	current_month = 1
	current_day = 1
	while i < index:
		print(determine_year_num(i), determine_num_days(current_month, determine_year_num(i)), current_month, i, current_day)
		if current_day > determine_num_days(current_month, determine_year_num(i)):
			current_day = 1
			if current_month == 12:
				current_month = 1
			else:
				current_month += 1
		else:
			current_day += 1
		i += 1
	return current_month

print(determine_month_num(376))