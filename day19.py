import io
m = io.open("day19.in").readlines()
px = m[0].index('|')
py = 0
dx = 0
dy = 1
p = ''
s = 0
while px >= 0 and py >= 0 and py < len(m) and px < len(m[py]) and m[py][px]!=' ':
    s+=1
    px+=dx
    py+=dy
    if m[py][px].isalpha():
        p += m[py][px]
    if m[py][px] == '+':
        # go left
        if dx == 0 and px > 0 and m[py][px-1] != ' ':
            dy = 0
            dx = -1
        # go right
        elif dx == 0 and px + 1 < len(m[py]) and m[py][px+1] != ' ':
            dy = 0
            dx = 1
        # go down
        elif dy == 0 and py > 0 and m[py-1][px] != ' ':
            dy = -1
            dx = 0
        # go up
        elif dy == 0 and py + 1 < len(m) and m[py+1][px] != ' ':
            dy = 1
            dx = 0
print(p)
print(s)
    
    
        