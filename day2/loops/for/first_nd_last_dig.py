import math
def first_nd_last(n):
    no= int(math.log(n,10))
    return n%10,n//10**no
last,first=first_nd_last(123)
print(f"The first and the last digits of the given number are {first} and {last}")