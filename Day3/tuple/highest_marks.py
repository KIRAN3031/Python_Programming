def five_students(t):
    l=[]
    l.append(t)
    return l

l=[]
for i in range(5):
    t = tuple(map(str,input("Enter the roll_no, name , marks").split()))
    l+= five_students(t)
higher = max(l,key=lambda x : int(x[2]))
print("The highest mark student is ",higher[1],higher[2])
