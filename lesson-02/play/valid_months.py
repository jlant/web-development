months = ["January",
          "Februrary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]

month_abbvs = {}
for m in months:
    month_abbvs[m[:3].lower()] = m

month_abbvs2 = dict((m[:3].lower(),m) for m in months)

print(month_abbvs2)

def valid_month(month):
    
    month = month.lower().capitalize()
    if month in months:
        result = month
    else:
        result = None
    
    return result

def valid_month2(month):
    
    month = month.lower().capitalize()
    short_month = month[:3].lower()
    
    return month_abbvs.get(short_month)

print(valid_month("January"))
print(valid_month("JaNuary"))
print(valid_month("hello"))
print(valid_month(""))

print(valid_month2("January"))
print(valid_month2("JaNuary"))
print(valid_month2("hello"))
print(valid_month2(""))