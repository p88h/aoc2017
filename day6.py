import io
b=list(map(int, io.open("day6.in").readline().split()))
s={}
l=len(b)
c=0
key=''
while True:
    key = ' '.join(map(str,b))
    if key in s:
        break
    # print(key)
    s[key]=c
    m = b[0]
    p = 0
    for i in range(l):
        if b[i] > m :
            m = b[i]
            p = i
    b[p] = 0
    # redistribute
    while m > 0:
        p = (p + 1) % l
        b[p] += 1
        m -= 1
    c += 1
print(c)
print(c-s[key])

