import io

grid = {}
y = 0
x = 0
for l in io.open("day22.in").read().splitlines():
    for x in range(len(l)):
        grid[(y,x)] = l[x]
    y += 1
y = y // 2
x = x // 2
dx = 0
dy = -1
r = 0
for iter in range(10000000):
    if (y,x) not in grid or grid[(y,x)] == '.':
        (dy, dx) = (-dx, dy)
        grid[(y,x)] = 'W'
    elif grid[(y,x)] == 'W':
        grid[(y,x)] = '#'
        r += 1
    elif grid[(y,x)] == '#':
        (dy, dx) = (dx, -dy)
        grid[(y,x)] = 'F'
    elif grid[(y,x)] == 'F':
        (dy, dx) = (-dy, -dx)
        grid[(y,x)] = '.'
    y += dy
    x += dx
print(r)