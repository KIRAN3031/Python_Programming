def factors(n):
    for i in range(1,n+1):
        if (n%i==0):
            print(i,end=' ')
x = int(input("Enter the number to get the factors of those numbers"))
print(f'The Factors of the given number {x} are : ')
factors(x)