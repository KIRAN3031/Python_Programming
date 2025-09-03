def div_by_5_and_11(n):
    if n % 5 == 0 and n % 11 == 0:
        return True
    else:
        return False

n = int(input("Enter a number: "))
if div_by_5_and_11(n):
    print(f"{n} is divisible by 5 and 11")
else:
    print(f"{n} is not divisible by 5 and 11")  