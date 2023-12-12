text = open('input_day10.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])

def get_pipes(lines):
    pipes = {}
    m, n = len(lines), len(lines[0])
    for i in range(m):
        for j in xrange(n):
            sym = lines[i][j]
            if sym == '.': continue
            elif sym == 'S':
                start = (i,j)
                pipes[i,j] = [(i-1,j), (i,j-1), (i+1,j), (i, j+1)]
            elif sym == '|':
                pipes[i,j] = [(i-1,j),(i+1,j)]
            elif sym == '-':
                pipes[i,j] = [(i,j-1),(i,j+1)]
            elif sym == 'F':
                pipes[i,j] = [(i,j+1),(i+1,j)]
            elif sym == '7':
                pipes[i,j] = [(i,j-1),(i+1,j)]
            elif sym == 'L':
                pipes[i,j] = [(i,j+1),(i-1,j)]
            elif sym == 'J':
                pipes[i,j] = [(i,j-1),(i-1,j)]
            else: # Shouldn't happen
                print sym
    return start, pipes

start, pipes = get_pipes(lines)

def try_path(start, first):
    prev, cur = start, first
    path = [start]
    while cur != start:
        path.append(cur)
        if cur not in pipes or prev not in pipes[cur]:
            return False
        nex = [p for p in pipes[cur] if p != prev][0]
        prev, cur = cur, nex
    return path

paths = [try_path(start, first) for first in pipes[start]]
path = [p for p in paths if p][0]

# solve easy
assert len(path)/2 == 6968

def solve_hard(path, m, n):
    pathset = set(path)
    dm, dn = 2*m-1, 2*n-1
    doub = [[0]*dn for i in range(dn)]
    for (i,j),(ii, jj) in zip(path, path[1:]+path[:1]):
        doub[2*i][2*j] = 1
        doub[i+ii][j+jj] = 1
    toadd = [(i,j) for i in range(dm) for j in range(dn) \
             if i in [0,dm-1] or j in [0,dn-1] and doub[i][j] == 0]
    for i,j in toadd:
        doub[i][j] = 2
    while toadd:
        i,j = toadd.pop()
        for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if not ((0 <= ii < dm) and (0 <= jj < dn)): continue
            if doub[ii][jj] != 0: continue
            doub[ii][jj] = 2
            toadd.append((ii,jj))
    return sum(1 for i in xrange(m) for j in xrange(n) if (not (i,j) in loop) and (doub[2*i][2*j] == 0))

assert solve_hard(path, m, n) == 413

# Alternative hard solution, figuted out after submissions
def solve_hard2(lines, path):
    lines = lines[:]
    m, n = len(lines), len(lines[0])
    start, ne, pr = path[0], path[1], path[-1]
    dirs = [(o[0]-start[0], o[1]-start[1]) for o in [ne, pr]]
    flags = 2*((1,0) in dirs) + ((0,1) in dirs)
    real_start = 'JL7F'[flags]
    lines[start[0]] = lines[start[0]].replace('S',real_start)
    setpath = set(path)

    res, state = 0, 0
    for diag in range(-m+1, n):
        for i in xrange(m):
            j = i + diag
            if (i,j) not in setpath:
                res += state
            else:
                state ^= (lines[i][j] in '|-FJ')
        assert state == 0
    return res

assert solve_hard2(lines, path) == 413
