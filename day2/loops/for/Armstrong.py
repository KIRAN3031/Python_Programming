def Armstrong(n):
    temp=n
    s=0
    while n>0:
        s+=(n%10)**3
        n//=10
    return temp==s
print(f'The number 153 is palindrome {Armstrong(153)}')