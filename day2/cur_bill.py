cur_bill=0
def current_bill(units):
    if units>=300:
        return 50*3.80+50*4.20+100*5.10+100*6.30+(units-300)*7.50
    elif units>=200 and units<300:
        return 50*3.80+50*4.20+100*5.10+(units-200)*6.30
    elif units>=100 and units<200:
        return 50*3.80+50*4.20+(units-100)*5.10
    elif units>=50 and units<100:
        return 50*3.80+(units-50)*4.20
    else:
        return units*3.80
x = int(input("Enter the units used by the customer"))
print(f"The exact current bill for the customer is {current_bill(x)}")
