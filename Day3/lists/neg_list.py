def neg(l):
    for num in l:
        if num<0:
            print(num, end= ' ')
l = list(map(int,input("Enter the numbers by giving a tab space").split()))
neg(l)