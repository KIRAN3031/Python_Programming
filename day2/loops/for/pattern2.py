def pattern(r):
    for i in range(1,r+1):
        for j in range(1,r+1):
            if(i==j):
                print('$ ',end=' ')
            else:
                print('* ',end=' ')
        print()
pattern(5) 