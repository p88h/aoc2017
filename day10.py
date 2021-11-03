import io
line = io.open("day10.in").readline()
len1 = list(map(int, line.split(',')))
len2 = list(map(ord, line))
len2.extend([17, 31, 73, 47, 23])

def knothash(lens, rounds):
    tab = list(range(256))
    p = 0
    s = 0
    for r in range(rounds):
        for l in lens: 
            for j in range(l//2):
                p1 = (p+j) % 256
                p2 = (p+l-1-j) % 256
                (tab[p1], tab[p2]) = (tab[p2], tab[p1])
            p += l + s
            s += 1
    return tab

t1 = knothash(len1, 1)
print(t1[0]*t1[1])
t2 = knothash(len2, 64)
d2 = ''
o = 0
for b in range(16):
    v = 0
    for c in range(16):
        v ^= t2[o+c]
    o += 16
    d2 += "{:02x}".format(v)
print(d2)   
