
def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False
def days_in_month(year, month):
	if  month < 1 or month > 12:
		return None
	dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	aux  = dias[month - 1]
	if month == 2 and is_year_leap(year):
		aux = 29
	return aux

def day_of_year(year, month, day):
    if day > 31 or day < 1 and month <1 or month > 12:
        return None
    else:
        dias = days_in_month(year, month)
        return dias - day

print(day_of_year(2000, 11, 20))