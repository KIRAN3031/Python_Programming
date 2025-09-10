def five_students(t):
    l=[]
    l.append(t)
    return l

l=[]
for i in range(5):
    t = tuple(map(str,input("Enter the roll_no, name , marks").split()))
    l+= five_students(t)
print("The list of tuples is ",l)
