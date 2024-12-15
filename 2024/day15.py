text = open('input_day15.txt').read()
texts = text.split('\n\n')
lines = texts[0].splitlines()
m, n = len(lines), len(lines[0])
lines2 = texts[1].splitlines()

ll = [l for l in lines if '@' in l][0]
si, sj = lines.index(ll), ll.index('@')


def move_pt1(c, state, ci, cj):
    di, dj = {'^': (-1, 0), 'v':(1,0), '<':(0,-1), '>':(0,1)}[c]
    ni, nj = ci+di, cj+dj
    nni, nnj = ni, nj
    while state[ni][nj] == 1:
        ni, nj = ni+di, nj+dj
    if state[ni][nj] == 2:
        return ci, cj
    state[ni][nj] = state[nni][nnj]
    state[nni][nnj] = 0
    return nni, nnj

def solve_day15_pt1():
    state = [[{'#':2, '.':0, '@':0, 'O': 1}[c] for c in line] for line in lines]
    ci, cj = si, sj
    for c in ''.join(lines2):
        ci, cj = move_pt1(c, state, ci, cj)
    return sum([100*i + j for i in xrange(m) for j in xrange(n) if state[i][j] == 1])
    
def move_pt2(c, state, ci, cj):
    di, dj = {'^': (-1, 0), 'v':(1,0), '<':(0,-1), '>':(0,1)}[c]
    if di == 0:
        nj = cj+dj
        while state[ci][nj] in '[]':
            nj = nj+dj
        if state[ci][nj] == '#':
            return ci, cj
        for pj in xrange(nj, cj, -dj):
            state[ci][pj] = state[ci][pj-dj]
        return ci, cj+dj
    assert dj == 0
    ni = ci+di
    moves = {ni: {cj}}
    while moves[ni]:
        nni = ni + di
        if any([state[ni][nj] == '#' for nj in moves[ni]]): return ci, cj
        moves[nni] = reduce(lambda x,y: x|y,
                            [{']': {nj-1, nj}, '[': {nj,nj+1}, '.': set()}[state[ni][nj]]
                             for nj in moves[ni]])
        ni = nni
    for ni in xrange(nni, ci, -di):
            for nj in moves[ni]:
                state[ni][nj] = state[ni-di][nj]
                state[ni-di][nj] = '.'
    return ci+di, cj

def solve_day15_pt2():
    state = [[x for c in line for x in {'#':'##', '.':'..', '@':'..', 'O': '[]'}[c]] for line in lines]
    ci, cj = si, 2*sj
    for c in ''.join(lines2):
        ci, cj = move_pt2(c, state, ci, cj)
    return sum([100*i + j for i in xrange(m) for j in xrange(2*n) if state[i][j] == '['])
