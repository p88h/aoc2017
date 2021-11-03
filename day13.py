from curses import wrapper
import io
import time

pos = []
dir = []
rng = []
ofs = []
cyc = []
las = 0
for l in io.open("day13.in").readlines():
    a = l.split(': ')
    pos.append(0)
    dir.append(1)
    r = int(a[1])
    rng.append(r)
    o = int(a[0])
    ofs.append(o)
    cyc.append((r-1)*2)
    if o > las:
        las = o

delay = 0

def simm(delay):
    for f in range(len(ofs)):
        if (ofs[f] + delay) % cyc[f] == 0:
            return True
    return False

while simm(delay):
    delay += 1
    pass

def main(scr):
    scr.clear()
    pkt = -1
    tot = 0
    for f in range(len(ofs)):
        p = delay % cyc[f]
        if p >= rng[f] - 1:
            dir[f]=-1
            p -= rng[f]-1
            p = rng[f]-1-p
        else:
            dir[f]=1
        pos[f]=p
    for s in range(las+1):
        if pkt >= 0:
            scr.addstr(0, pkt, " ")
        pkt += 1
        hit = -1
        for f in range(len(ofs)):
            if ofs[f] == pkt and pos[f] == 0:
                hit = ofs[f] * rng[f]
                tot += hit
            for i in range(rng[f]):
                if i != pos[f]:
                    scr.addstr(i, ofs[f], 'O')
                else:
                    scr.addstr(i, ofs[f], 'X')
            pos[f] += dir[f]
            if pos[f] == rng[f]-1 or pos[f] == 0:
                dir[f] = -dir[f]
        if pkt >= 0:
            scr.addstr(0, pkt, "P")
        scr.addstr(20, 0, "{:04d}".format(tot))
        scr.addstr(21, 0, "+{}".format(delay))
        scr.refresh()
        time.sleep(0.25)
    time.sleep(3)

wrapper(main)