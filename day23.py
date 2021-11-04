import io

class coproc:
    def __init__(self, prog, id):
        self.reg = {}
        for c in range(8):
            self.reg[chr(c+ord('a'))] = 0
        self.pc = 0
        self.cnt = 0
        self.prog = prog
        self.snd = []
        self.rcv = 0
        self.block = False
        self.mulcnt = 0
    
    def val(self, tgt):
        if tgt.isalpha():
            return self.reg[tgt]
        else:
            return int(tgt)

    def step(self, other):
        op = self.prog[self.pc]
        self.cnt += 1
        if self.cnt % 1000 == 0:
            print("{}: regs={}".format(self.pc, self.reg))
        if op[0] == 'set':
            self.reg[op[1]]=self.val(op[2])
        if op[0] == 'add':
            self.reg[op[1]]+=self.val(op[2])
        if op[0] == 'sub':
            self.reg[op[1]]-=self.val(op[2])
        if op[0] == 'mul':
            self.reg[op[1]]*=self.val(op[2])
            self.mulcnt += 1
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
        elif op[0] == 'jnz' and self.val(op[1]) != 0:
            self.pc += self.val(op[2])
        else:
            self.pc += 1

prog = []
for l in io.open("day23.in").readlines():
    op = l.split()
    prog.append(op)

mach = coproc(prog, 0)
mach.reg['a']=1
while mach.pc < len(prog):
    mach.step(None)

print(mach.mulcnt)
print(mach.reg['h'])
