text = open('input_day17.txt').read()
lines = text.splitlines()
# m, n = len(lines), len(lines[0])

init_a = int(lines[0].split()[-1])
prog = map(int,lines[-1].split()[-1].split(','))

def act(regs, output):
    ip = regs[-1]
    if ip >= len(prog): return False
    c = prog[ip]
    op = prog[ip+1]
    ip += 2
    comb_op = (op if op < 4 else regs[op-4])
    if op == 7 and c in [0,2,5,6,7]: return False
    if c == 0: 
        regs[0] >>= comb_op
    if c == 1:
        regs[1] ^= op
    if c == 2:
        regs[1] = comb_op % 8
    if c == 3:
        if regs[0] != 0: ip = op
    if c == 4:
        regs[1] ^= regs[2]
    if c == 5:
        output.append(comb_op % 8)
    if c == 6:
        regs[1] = regs[0] >> comb_op
    if c == 7:
        regs[2] = regs[0] >> comb_op
    regs[3] = ip
    return True

def output_a(a):
    regs = [a, 0, 0, 0]
    output = []
    while act(regs, output): pass
    return output

def solve_day17_pt1():
    return ','.join(map(str,output_a(init_a)))

'''
My input program was 2,4,1,1,7,5,0,3,1,4,4,5,5,5,3,0.
This decompiles to
0: b = a % 8
2: b ^= 1
4: c = a >> b
6: a >>= 3
8: b ^= 4
10: b ^= c
12: out b % 8
14: jnz 0

Which is equivalent to the simple loop:
  while a:
    output (a ^ (a >> (a % 8 ^ 1)) ^ 5) % 8
    a >>= 3
Therefore a can be reconstructed 3 bits at a time by reading the outputs in reverse
and seeing which previous values for a%8 worked. This may branch a little and at least one branch
is guaranteed to work.
'''
def prev_a(a, outval):
    a <<= 3
    res = []
    for x in range(a, a+8):
        if (x ^ (x >> ((x%8)^1)) ^ 5) % 8 == outval:
            res.append(x)
    return res

def solve_day17_pt2():
    aa = [0]
    for v in prog[::-1]:
        aa = sum([next_a(a, v) for a in aa],[])
    return min(aa)
