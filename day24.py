import io
conn = [[] for i in range(50)]
for l in io.open("day24.in").read().splitlines():
    ab = l.split('/')
    a = int(ab[0])
    b = int(ab[1])
    conn[a].append(b)
    if a != b:
        conn[b].append(a)

def explore(graph, used, cur, idx, sum, path):
    # eat short loops first, always
    lmax = len(path)
    smax = sum
    loop = False
    leaf = True
    if cur in graph[cur] and (cur,cur) not in used:
        used[(cur,cur)] = idx
        idx += 1
        sum += cur + cur
        loop = True
        path.append((cur,cur))
    for dst in graph[cur]:
        if (cur,dst) not in used:
            leaf = False
            used[(cur,dst)] = idx
            used[(dst,cur)] = idx
            sum += cur + dst
            path.append((cur,dst))
            (ltmp, stmp) = explore(graph, used, dst, idx + 1, sum, path)
            path.pop()
            sum -= cur + dst
            del used[(cur,dst)]
            del used[(dst,cur)]
            if ltmp > lmax or (ltmp == lmax and stmp > smax):
                smax = stmp
                lmax = ltmp
    if loop:
        path.pop()
        del used[(cur,cur)]
    #if leaf:   
    return (lmax, smax)

res = explore(conn, {}, 0, 1, 0, [])
print(res)
