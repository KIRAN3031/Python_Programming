def digit_word(n):
    d = ['zero','one','two','three','four','five','six','seven','eight','nine']
    l = []
    while n > 0:
        l.append(d[n % 10])
        n = n // 10
    return l[::-1]

s = digit_word(123)
print(*s)
