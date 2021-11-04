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
        if b % d == 0:
            f = 0
            break
        d += 1
        if d * d > b:
            break
    if f == 0:
        h += 1
    if b == c:
        break
    b+=17
    print("b={} c={} h={}".format(b,c,h))
print(h)