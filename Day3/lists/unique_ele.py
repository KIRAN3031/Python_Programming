def unique(l):
    print(f'One of the method using set is {list(set(l))}')
    print("The other method ")
    l1=[]
    for i in l:
        if i not in l1:
            l1.append(i)
    print("the other method using list is ",l1)
l = [1,2,3,4,1,3,2,6,7]
unique(l)
