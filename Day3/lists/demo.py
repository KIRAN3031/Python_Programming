def list1():
    l = list(map(int,input("Enter the elements separeted by space").split()))
    for num in l : print(num , end=' ')
    print()
    print(type(l))
list1()