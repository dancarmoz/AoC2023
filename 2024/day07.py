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

def valid_line_pt2(line):
    res = line[0]
    op = set([line[1]])
    for v in line[2:]:
        op = set([y  for x in op for y in [x+v, x*v, int(str(x)+str(v))]])
    return res in op

# runs in ~9s
def solve_day07_pt2():
    return sum([l[0] for l in plines if valid_line_pt2(l)])

