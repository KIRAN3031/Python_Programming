def freq(l):
    li = []
    for i in l:
        if i not in li:
            print(f'{i} -> {l.count(i)}')
            li.append(i)

l=[1,2,3,4,1,2,5,6,7,1,2]
freq(l)