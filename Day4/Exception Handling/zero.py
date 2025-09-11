def division(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result

print(division(10, 2))  
print(division(10, 0))  