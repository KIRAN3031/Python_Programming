def del_ele(l,idx):
    print("The original list is ",l)
    for i in range(len(l)):
        if i == idx:
            l.pop(i)
    print(l)



l = list(map(int,input("Enter the elements ").split()))
de = int(input("Enter the index for deleting the element"))
del_ele(l,de)