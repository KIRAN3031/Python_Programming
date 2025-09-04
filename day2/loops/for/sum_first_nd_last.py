import math
def first_nd_last(n):
    no= int(math.log(n,10))
    return n%10+n//10**no
su_of_first_nd_last=first_nd_last(123)
print(f"The sum of  first and the last digits of the given number are {su_of_first_nd_last}")