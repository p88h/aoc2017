import io, re
pat = re.compile('^(\w+) (\w+) (\-?\d+) if (\w+) (\!?=?>?<?=?) (\-?\d+)$')
reg = {}
rmax = 0
for l in io.open("day8.in").readlines():
    m = pat.match(l)
    r1 = m.group(1)
    op = m.group(2)
    ov = int(m.group(3))
    r2 = m.group(4)
    co = m.group(5)
    cv = int(m.group(6))
    if r1 not in reg:
        reg[r1] = 0
    if r2 not in reg:
        reg[r2] = 0
    if (co == '<' and reg[r2] < cv) or (co == '>' and reg[r2] > cv) or \
       (co == '>=' and reg[r2] >= cv) or (co == '<=' and reg[r2] <= cv) or \
       (co == '==' and reg[r2] == cv) or (co == '!=' and reg[r2] != cv):
        if op == 'inc':
            reg[r1] += ov
        if op == 'dec':
            reg[r1] -= ov
    if reg[r1] > rmax:
        rmax = reg[r1]
print(reg)
print(max(list(reg.values())))
print(rmax)
