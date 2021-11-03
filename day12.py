import io
c = []
for l in io.open("day12.in").readlines():
    a = l.split(' <-> ')
    b = list(map(int, a[1].split(', ')))
    c.append(b)

v = {}
g = 0
for q in range(len(c)):
    if q in v:
        continue
    s = [ q ]
    v[q] = 0
    l = 0 
    while l < len(s): 
        n = s[l]
        for d in c[n]:
            if d not in v:
                v[d] = v[n] + 1
                s.append(d)
        l += 1
    g += 1
    print("Group {} from {} size {}".format(g, q, len(s)))
