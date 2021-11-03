import io
x = 0
y = 0

def distance(cx, cy):
    b = min(abs(cx), abs(cy))
    return b+(abs(cx)-b)+(abs(cy)-b)//2

f = 0

for m in io.open("day11.in").readline().split(','):
    if m == "nw":
        x -= 1
        y -= 1
    if m == "n":
        y -= 2
    if m == "ne":
        x += 1
        y -= 1
    if m == "sw":
        x -= 1
        y += 1
    if m == "s":
        y += 2
    if m == "se":
        x += 1
        y += 1
    d = distance(x,y)
    if d > f:
        f = d

print(distance(x,y))
print(f)