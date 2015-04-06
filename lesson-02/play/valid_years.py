import datetime

now = datetime.datetime.now()

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year <= now.year:
            return year

def valid_year2(year):
    """ """

    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year <= 2020:
            return year

print(valid_year("0")) # None
print(valid_year("-11")) # None
print(valid_year("1950")) # 1950
print(valid_year("2000")) # 2000
print(valid_year("")) # None
print(valid_year("foo")) # None
print(valid_year("1900,")) # None