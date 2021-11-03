import io
rot2 = [[0,1,2,3],[2,0,3,1],[3,2,1,0],[1,3,0,2],[2,3,0,1],[0,2,1,3],[1,0,3,2],[3,1,2,0]]
rot3 = [[0,1,2,3,4,5,6,7,8],[6,3,0,7,4,1,8,5,2],[8,7,6,5,4,3,2,1,0],[2,5,8,1,4,7,0,3,6]] + \
       [[6,7,8,3,4,5,0,1,2],[0,3,6,1,4,7,2,5,8],[2,1,0,5,4,3,8,7,6],[8,5,2,7,4,1,6,3,0]]

repl = {}
for l in io.open("day21.in").read().splitlines():
    pt = l.split(' => ')
    p = ''.join(pt[0].split('/'))
    t = pt[1].split('/')
    if len(p) == 4:
        rot = rot2
    else:
        rot = rot3
    for r in rot:
        q = ''
        for b in r:
            q += p[b]
        repl[q] = t
        print(q)
    print('=>')
    print(t)

sc = ['.#.', '..#', '###']

for iter in range(18):
    sc2 = []
    if len(sc) % 2 == 0:
        for by in range(len(sc)//2):
            sc2.extend(['','',''])
            for bx in range(len(sc)//2):
                str = sc[by*2][bx*2:bx*2+2] + sc[by*2+1][bx*2:bx*2+2]
                rep = repl[str]
                sc2[by*3] += rep[0]
                sc2[by*3+1] += rep[1]
                sc2[by*3+2] += rep[2]
    else:
        for by in range(len(sc)//3):
            sc2.extend(['','','',''])
            for bx in range(len(sc)//3):
                str = sc[by*3][bx*3:bx*3+3] + sc[by*3+1][bx*3:bx*3+3] + sc[by*3+2][bx*3:bx*3+3]
                rep = repl[str]
                sc2[by*4] += rep[0]
                sc2[by*4+1] += rep[1]
                sc2[by*4+2] += rep[2]
                sc2[by*4+3] += rep[3]
    sc = sc2
    t = 0
    for l in sc:
        t += l.count('#')
        print(l)
    print('='*len(sc)+' {}'.format(t))

            

