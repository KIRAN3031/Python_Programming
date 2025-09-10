def freq_dup(l):
    li = []
    f=0
    for i in l:
        if i not in li:
            li.append(i)
        else: f+=1
    return f

l=[1,2,3,4,1,2,5,6,7,1,2]
print("The count of the duplicates in the given list is ",freq_dup(l))