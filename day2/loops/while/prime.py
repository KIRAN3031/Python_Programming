import math
def prime(n):
    i=3
    if(n==1 or n<0) : return False
    while i<=int(math.sqrt(n)):
        if (n%i==0):
            return False
    return True
x = int(input("Enter a number"))
print(f'Is the entered number {x} is prime??  {prime(x)}')

