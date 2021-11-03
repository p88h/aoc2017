import io
from day10 import knothash
t = 0
p = 'vbqugkhl'
m = []
for i in range(128):
    l = "{}-{}".format(p, i)
    h = knothash(l)
    s = []
    for c in h:
        v = int(c, base=16)
        s.extend('{:04b}'.format(v))
    t += s.count('1')
    m.append(s)
print(t)

cnt=0
for i in range(128):
    for j in range(128):
        if m[i][j]=='1':
            cnt += 1
            m[i][j]='*'
            s = [(i,j)]
            k = 0
            while k < len(s):
                (y,x) = s[k]
                k += 1
                if y > 0 and m[y-1][x]=='1':
                    m[y-1][x]='#'
                    s.append((y-1,x))
                if x > 0 and m[y][x-1]=='1':
                    m[y][x-1]='#'
                    s.append((y,x-1))
                if x < 127 and m[y][x+1]=='1':
                    m[y][x+1]='#'
                    s.append((y,x+1))
                if y < 127 and m[y+1][x]=='1':
                    m[y+1][x]='#'
                    s.append((y+1,x))
print(cnt)