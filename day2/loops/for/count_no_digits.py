import math
def count(n):
    return int(math.log(n,10)+1)
x=int(input("Enter the number"))
print(f'The count of the digits of the number is {count(x)}')