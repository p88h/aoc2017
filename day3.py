v = 361527
x = 50
y = 50
grid = {}
grid[100*y+x] = 1 

def sumup(sx, sy):
    t = 0 
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            k = 100*(sy+dy)+sx+dx
            if k in grid:
                t += grid[k]
    return t

def process(sx, sy, z):
    z = sumup(sx,sy)
    grid[100*sy + sx] = z
    if z >= v:
        print("{}x{}=>{}".format(sx-50,sy-50,z))
    return z

def run(sx, sy, l, z):
    for i in range(l-1):
        z = process(sx, sy, z)
        sy -= 1
    for i in range(l):
        z = process(sx, sy, z)
        sx -= 1
    for i in range(l):
        z = process(sx, sy, z)
        sy += 1
    for i in range(l):
        z = process(sx, sy, z)
        sx += 1
    z = process(sx, sy, z)
    sx += 1
    return (sx, sy, z)

s = 0
t = 1
while v > t:
    (x, y, t) = run(x, y, s // 4, t)
    s += 8
