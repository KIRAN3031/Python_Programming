def char_count(s):
    si=''
    freq={}
    for i in s:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    freq = dict(sorted(freq.items()))
    for key,value in freq.items():
        si+=key+str(value)
    return si

print(char_count("kiran"))
    
