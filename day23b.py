b=65
c=b
h=0
b*=100
b+=100000
c=b
c+=17000
while True:
    f=1
    d=2
    while True:
        e = b // d
        while True:
            if d * e == b:
                f = 0
                break
            e += 1 
            if d * e > b:
                break
        d += 1
        if d * d > b or f == 0:
            break
    if f == 0:
        h += 1
    if b == c:
        break
    b+=17
    print("b={} c={} h={}".format(b,c,h))
print(h)