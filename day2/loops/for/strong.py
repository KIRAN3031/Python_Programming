def fact(n):
    if n==0 or n==1: return n
    else : return n*fact(n-1)
def Strong(n):
    s=0
    temp=n
    while n>0:
        s+=fact(n%10)
        n//=10
    return s==temp
x=int(input("Enter a number to check whether the number is Strong or not"))
print(f'The number {x} is the strong number ?? {Strong(x)}')

