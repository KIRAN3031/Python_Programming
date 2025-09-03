#2) The Function with parameters and without return type
def add(a,b):
    c=a+b
    print(c)

add(10,20)

def km_to_miles(km):
    miles=km*0.621371
    print("The distance in miles is:",miles)
    
km_to_miles(10)

def months_and_years(days):
    months=days//30
    years=days/365
    print("The months:",months)
    print("The years:",years)

months_and_years(1000)