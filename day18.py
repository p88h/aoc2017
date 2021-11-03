import io

class duet:
    def __init__(self, prog, id):
        self.reg = {}
        for c in range(25):
            self.reg[chr(c+ord('a'))] = 0
        self.reg['p'] = id
        self.pc = 0
        self.prog = prog
        self.snd = []
        self.rcv = 0
        self.block = False
    
    def val(self, tgt):
        if tgt.isalpha():
            return self.reg[tgt]
        else:
            return int(tgt)

    def step(self, other):
        op = self.prog[self.pc]
        if op[0] == 'set':
            self.reg[op[1]]=self.val(op[2])
        if op[0] == 'add':
            self.reg[op[1]]+=self.val(op[2])
        if op[0] == 'mul':
            self.reg[op[1]]*=self.val(op[2])
        if op[0] == 'mod':
            self.reg[op[1]]%=self.val(op[2])
        if op[0] == 'snd':
            self.snd.append(self.val(op[1]))
        if op[0] == 'rcv':
            if self.rcv < len(other.snd):
                self.reg[op[1]] = other.snd[self.rcv]
                self.rcv += 1
                self.block = False
            else:
                self.block = True
                return
        if op[0] == 'jgz' and self.val(op[1]) > 0:
            self.pc += self.val(op[2])
        else:
            self.pc += 1

prog = []
for l in io.open("day18.in").readlines():
    op = l.split()
    prog.append(op)

mach0 = duet(prog, 0)
mach1 = duet(prog, 1)

while not (mach0.block and mach1.block):
    mach0.step(mach1)
    mach1.step(mach0)

print(len(mach1.snd))
