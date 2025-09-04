def perfect(n):
    s=0
    for i in range(1,n):
        if (n%i==0): s+=i
    return s==n

x = int(input("Enter the number to check whether it is a perfect or not"))
print(f'The number {x} is a perfect number??? {perfect(x)}')