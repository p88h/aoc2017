import io
pos = []
vel = []
acc = []
liv = []

def parse(it):
    s = it[3:-1]
    return s.split(',')
    
for l in io.open("day20.in").read().splitlines():
    pva = l.split(', ')
    pos.append(list(map(int, parse(pva[0]))))
    vel.append(list(map(int, parse(pva[1]))))
    acc.append(list(map(int, parse(pva[2]))))
    liv.append(True)

last = 0
for iter in range(1000000):
    first = True
    min = 0
    idx = 0
    kill = 0
    coll = {}
    for p in range(len(pos)):
        if not liv[p]:
            continue
        vel[p][0] += acc[p][0]
        vel[p][1] += acc[p][1]
        vel[p][2] += acc[p][2]
        pos[p][0] += vel[p][0]
        pos[p][1] += vel[p][1]
        pos[p][2] += vel[p][2]
        dst = abs(pos[p][0]) + abs(pos[p][1]) + abs(pos[p][2])
        if first or dst < min:
            min = dst
            idx = p
            first = False
        pkey = '{},{},{}'.format(pos[p][0],pos[p][1],pos[p][2])
        if pkey in coll:
            liv[p] = False
            liv[coll[pkey]] = False
            kill += 1
        else:
            coll[pkey] = p
    if idx != last or kill > 0:
        print("iter: {} min: {} live: {}".format(iter, idx, liv.count(True)))
        last = idx
