def second_largest_num(l):
    lar = l[0]
    for i in l:
        if i>lar:
            lar=i
    l.remove(lar)
    lar=0
    for i in l:
        if i>lar:
            lar=i
    return lar
l=list(map(int,input("Enter the numbers").split()))
print("The second largest number of list is ",second_largest_num(l))
