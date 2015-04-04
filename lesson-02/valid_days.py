def valid_day(day):
    """ """

    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day

print(valid_day("0")) # None
print(valid_day("1")) # 1
print(valid_day("15")) # 15
print(valid_day("500")) # None
print(valid_day("")) # None
print(valid_day("foo")) # None
print(valid_day("31,")) # None
print(valid_day("-1")) # None