from itertools import product
text = open('input_day12.txt').read()
lines = text.splitlines()
rows, conts = [l.split()[0] for l in lines], [map(int, l.split()[1].split(',')) for l in lines]

# Original solution to easy part - deprecated by hard part
def row_to_cont(r):
    return map(len, r.replace('.',' ').split())

MAX_LEN = max(map(len,rows))
assert MAX_LEN <= 20
row_to_conts = [row_to_cont(''.join(r)) for r in list(product(*[['.','#'] for j in xrange(MAX_LEN)]))]

def solve_row_easy(p, c):
    mask = int(p.replace('?','0').replace('#','1').replace('.','1'),2)
    num = int(p.replace('#','1').replace('?','0').replace('.','0'),2)
    return sum(cc == c and (n&mask) == num for n, cc in enumerate(row_to_conts[:2**len(p)]))

def solve_easy(rows, conts):
    return sum(solve_row(r, c) for r, c in zip(rows, conts))
assert solve_easy(rows, conts) == 7771

# Solution to both parts
def solve_row(part, con):
    part = part + '.'
    m, n = len(part), len(con)
    solves = [[None]*(n+1) for i in xrange(m)] + [[0]*n+[1]]
    for i in xrange(m-1,-1,-1):
        solves[i] = solves[i+1][:] if part[i] != '#' else [0]*(n+1)
        if part[i] == '.': continue
        for j in xrange(n):
            cc = con[j]
            if i+cc <= m and all(part[ii] != '.' for ii in xrange(i, i+cc)) and part[i+cc] != '#':
                solves[i][j] += solves[i+cc+1][j+1]
    return solves[0][0]

rows_hard, conts_hard = ['?'.join([r]*5) for r in rows], [c*5 for c in conts]

def solve_hard(rows, conts):
    return sum(solve_row(r, c) for r, c in zip(rows, conts))

solve_hard(rows, conts) == 7771
solve_hard(rows_hard, conts_hard) == 10861030975833
