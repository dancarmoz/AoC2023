text = open('input_day13.txt').read()
blines = [x.splitlines() for x in text.split('\n\n')]
blines_t = [map(''.join, zip(*bl)) for bl in blines]

def get_refl_rows(b):
    m = len(b)
    return [i for i in xrange(1,m) if all(b[j]==b[2*i-1-j] for j in xrange(max(0,2*i-m),i))]

def solve(blines, blines_t, get_rows):
    return sum(sum(get_rows(b))*100 + sum(get_rows(bt)) for b,bt in zip(blines,blines_t))

assert solve(blines, blines_t, get_refl_rows) == 31877

def get_refl_rows_smudge(b):
    m, n = len(b), len(b[0])
    res = []
    for i in xrange(1,m):
        fixes = 0
        for j in xrange(max(0,2*i-m),i):
            if b[j] == b[2*i-1-j]: continue
            if fixes >= 1: break
            if sum(x!=y for x,y in zip(b[j], b[2*i-1-j])) > 1: break
            fixes = 1
        else:
            if fixes: res.append(i)
    return res

assert solve(blines, blines_t, get_refl_rows_smudge) == 42996
