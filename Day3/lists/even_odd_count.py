def even_odd_count(l):
    even_count,odd_count=0,0
    for i in l:
        if i%2==0:
            even_count+=1
        else : 
            odd_count+=1
    return even_count,odd_count

l = list(map(int,input("Enter the numbers").split()))
even,odd=even_odd_count(l)
print(f"The even count is {even} and the odd count is {odd}")