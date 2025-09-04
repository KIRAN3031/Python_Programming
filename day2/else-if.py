def get_week(n):
    if n==1:
        return 'Sunday'
    elif n==2:
        return 'Monday'
    elif n==3:
        return 'Tuesday'
    elif n==4:
        return 'Wednesday'
    elif n==5:
        return 'Thrusday'
    elif n==6:
        return 'Friday'
    elif n==7:
        return 'Saturday'
    else:
        return 'Invalid Input'
day = int(input("Enter the week number"))
print(f"The day the user Entered is the {get_week(day)}")