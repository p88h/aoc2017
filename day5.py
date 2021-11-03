import io
l = list(map(int, io.open("day5.in").readlines()))
p = 0
s = 0
while p >= 0 and p < len(l):
    o = l[p]
    if o < 3:
        l[p] += 1
    else:
        l[p] -= 1
    p += o
    s += 1
print(s)
