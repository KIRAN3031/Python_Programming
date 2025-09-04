def sum_natural(n):
    i,s=0,0
    while i<n:
        i+=1
        s+=i
    return s
n = int(input("Enter the range of the number"))
print(f"The sum of the numbers form 1 to {n} is {sum_natural(n)}")