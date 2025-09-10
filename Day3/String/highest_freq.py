def high_freq(s):
    s= s.lower()
    si=''
    val=s[0]
    ma = s.count(s[0])
    for i in s:
        if i not in si:
            j = s.count(i)
            si+=i
            if j>ma:
                ma=j
                val=i

    return val,ma

print(high_freq("aaaabbbccca"))