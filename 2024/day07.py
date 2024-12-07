text = open('input_day07.txt').read()
lines = text.splitlines()
plines = [map(int, l.replace(':','').split()) for l in lines]

def valid_line_pt1(line):
    res = line[0]
    op = set([line[1]])
    for v in line[2:]:
        op = set([y  for x in op for y in [x+v, x*v]])
    return res in op

def solve_day07_pt1():
    return sum([l[0] for l in plines if valid_line_pt1(l)])

# runs in ~9.8s. Without "set" in ~8.9s.
def valid_line_pt2(line):
    res = line[0]
    op = set([line[1]])
    for v in line[2:]:
        op = set([y  for x in op for y in [x+v, x*v, int(str(x)+str(v))]])
    return res in op

# runs in ~4.7s.
def valid_line_pt2_better(line):
    res = line[0]
    op = ([line[1]])
    for v in line[2:]:
        op = ([y  for x in op for y in [x+v, x*v, int(str(x)+str(v))] if y <= res])
    return res in op

def deops(res, arg):
    ops = []
    if arg < res:
        ops.append(res - arg)
    if res % arg == 0:
        ops.append(res / arg)
    sarg, sres = str(arg), str(res)
    if sres.endswith(sarg) and sres != sarg:
        ops.append(int(sres[:-len(sarg)]))
    return ops

# runs in ~0.15s
def valid_line_pt2_best(line):
    goals = [line[0]]
    for v in line[2:][::-1]:
        goals = [y for x in goals for y in deops(x, v)]
    return line[1] in goals

def solve_day07_pt2(valid_func = valid_line_pt2_best):
    return sum([l[0] for l in plines if valid_func(l)])
