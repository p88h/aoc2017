import io,re
pat = re.compile('^(\w+) \((\d+)\)( -> )?(\w[a-z, ]*)?$')
r = {}
g = {}

class Node:
    def __init__(self, label, weight):
        self.label = label
        self.children = []
        self.weight = weight

    def add(self, child):
        self.children.append(child)


def visit(graph, label):
    n = graph[label]
    w = n.weight
    f = 0
    for l in n.children:
        t = visit(graph, l)
        if f == 0:
            f = t
        elif t != f:
            print("{}->{} {}!={}".format(n.label,l,f,t))
        w += t
    return w

for l in io.open("day7.in").readlines():
    m = pat.match(l)
    n = Node(m.group(1), int(m.group(2)))
    # print("p: {} w: {} d: {}".format(m.group(1),m.group(2),m.group(4)))
    if m.group(4):
        for c in m.group(4).split(', '):
            r[c] = n
            n.add(c)
    g[n.label] = n

s = ''
for l in g.keys():
    if l not in r:
        s = l
print(s)
visit(g, s)
