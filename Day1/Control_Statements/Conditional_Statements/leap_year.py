def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return True
    else:
        return False
    
year = int(input("Enter a year: "))
if leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")