import io
lines = io.open("day25.in").read().splitlines()
state = lines[0][15]
steps = int(lines[1].split()[5])
program = {}
curs = 0
tape = {}

def parse_op(stmt):
    val = int(stmt[0][22])
    dir = 1 if 'right' in stmt[1] else -1
    nxt = stmt[2][26]
    return (val, dir, nxt)

for blk in range(len(lines) // 10):
    label = lines[blk*10+3][9]
    program[label] = [ parse_op(lines[blk*10+5:blk*10+8]), parse_op(lines[blk*10+9:blk*10+12]) ]

for s in range(steps):
    value = tape[curs] if curs in tape else 0
    (value, dir, state) = program[state][value]
    tape[curs] = value
    curs += dir

print(list(tape.values()).count(1))