import io
gid = 0
tot = 0
line = io.open("day9.in").readline()
pos = 0
gc = 0
garbage = False
while pos < len(line): 
    if not garbage:
        if line[pos] == '{':
            gid += 1
        if line[pos] == '}':
            tot += gid
            gid -= 1
        if line[pos] == '<':
            garbage = True
    else:
        if line[pos] == '!':
            pos += 1
        elif line[pos] == '>':
            garbage = False
        else:
            gc += 1
    pos += 1
print(tot)
print(gc)