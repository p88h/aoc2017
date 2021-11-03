import io
d = io.open("day16.in").readline().split(',')
# d = [ 's1', 'x3/4', 'pe/b']
M = 16
# order permutation (x swaps and shifts)
pos = list(range(M))
seq = list(range(M))
# label permutation (p swaps)
lab = list(range(M))
bal = list(range(M))
# do the dance now
for m in d:
    if m[0] == 's':
        o = int(m[1:])
        # shift right
        for c in range(M-o):
            pos[seq[c]] += o
        # shift left
        for c in range(o):
            pos[seq[M-o+c]] = c
        # reconstruct
        for c in range(M):
            seq[pos[c]]=c
    else:
        ab = m[1:].split('/')
        if m[0] == 'x':
            a = int(ab[0])
            b = int(ab[1])
            (seq[a], seq[b]) = (seq[b], seq[a])
            pos[seq[a]] = a
            pos[seq[b]] = b
        else:
            a = int(ord(ab[0])-ord('a'))
            b = int(ord(ab[1])-ord('a'))
            (bal[a], bal[b]) = (bal[b], bal[a])
            lab[bal[a]] = a
            lab[bal[b]] = b

# helper function to multiply permutations
def mulp(perma, permb):
    permc = []
    for i in range(len(perma)):
        permc.append(perma[permb[i]])
    return permc

# build our permutation exponents
perms = [ seq ]
perml = [ lab ]
for e in range(1,30):
    perms.append(mulp(perms[e-1], perms[e-1]))
    perml.append(mulp(perml[e-1], perml[e-1]))

# just do it, binary style
num = 999999999
lvl = 0 
while num > 0:
    if num % 2 == 1:
        seq = mulp(seq, perms[lvl])
        lab = mulp(lab, perml[lvl])
    num = num // 2
    lvl += 1

t = ''
for c in seq:
    t += chr(ord('a') + lab[c])
print(t)