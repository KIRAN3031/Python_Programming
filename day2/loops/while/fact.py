def fact(n):
    i,f=n,1
    while i>=1:
        f=f*i
        i-=1
    return f

x=int(input("Enter the number"))
print(f'The factorial of the given number is {x} is {fact(x)}')