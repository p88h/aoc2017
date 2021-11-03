import io
u = 0
u2 = 0
for line in io.open("day4.in").readlines():
    a = line.split()
    d = {}
    d2 = {}
    v = 1
    v2 = 1
    for w in a:
        if w not in d:
            d[w] = 1
        else:
            v = 0
        w2 = ''.join(sorted(w))
        if w2 not in d2:
            d2[w2] = 1
        else:
            v2 = 0
    u += v
    u2 += v2
print(u)
print(u2)

