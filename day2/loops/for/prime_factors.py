def isPrime(x):
    if x==1 and x<0 : return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
def factors(x):
    for i in range(2,x+1):
        if x%i==0 and isPrime(i):
            print(i,end=' ')
x = int(input("Enter the number"))
print("The prime factors are :")
factors(x)