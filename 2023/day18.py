text = open('input_day18.txt').read()
lines = text.splitlines()

cmds = [(x,int(y), z[2:-1]) for x,y,z in [l.split() for l in lines]]
cmds_easy = [(x,y) for x,y,z in cmds]

d_to_delta = {'U':(-1,0), 'D':(1,0), 'L': (0, -1), 'R': (0,1)}

def solve_easy(cmds):
    path = [(0,0)]
    for d,n in cmds:
        i,j = path[-1]
        di, dj = d_to_delta[d]
        path += [(i+di*k, j+dj*k) for k in xrange(1,n+1)]
    mi, mj = [min([x[i] for x in path]) for i in [0,1]]
    path_sh = [(i-mi+1, j-mj+1) for i,j in path]
    path_sh_set = set(path_sh)
    m, n = [max([x[i] for x in path_sh])+2 for i in [0,1]]
    area = [[1]*n for i in range(m)]
    toadd = [(i,j) for i in range(m) for j in range(n) \
             if i in [0,m-1] or j in [0,n-1]]
    for i,j in toadd:
        area[i][j] = 0
    while toadd:
        i,j = toadd.pop()
        for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if not ((0 <= ii < m) and (0 <= jj < n)): continue
            if area[ii][jj] == 0 or (ii,jj) in path_sh_set: continue
            area[ii][jj] = 0
            toadd.append((ii,jj))
    return sum(map(sum,area))

assert solve_easy(cmds_easy) == 67891

cmds_hard = [('RDLU'[int(z[-1])], int(z[:-1], 16)) for x,y,z in cmds]

def solve_hard(cmds):
    # Assume zigzaging LR/UD, starting with LR.
    assert cmds[0][0] in 'LR'
    # Also assumes we are travelling clockwise along the path, so that
    # the outer edge is always on the path's left.
    area, x, y, pax = 0, 0, 0, (cmds[-1][0] == 'D')
    for (d1,k1), (d2,k2) in zip(cmds[::2], cmds[1::2]):
        dx = {'L':-1,'R':1}[d1]*k1
        dy = {'D':-1,'U':1}[d2]*k2
        ay = y + (dx > 0)
        x, y = x + dx, y + dy
        ax = x + (dy < 0)
        area += (ax - pax)*ay
        pax = ax
    assert area > 0
    return area

assert solve_hard(cmds_easy) == 67891
assert solve_hard(cmds_hard) == 94116351948493
