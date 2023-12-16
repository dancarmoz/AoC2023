text = open('input_day16.txt').read()
lines = text.splitlines()

next_dirs = {'.': {'L':'L','R':'R','D':'D','U':'U'},
	     '/': {'L':'D','R':'U','D':'L','U':'R'},
	     '\\': {'L':'U','R':'D','D':'R','U':'L'},
	     '-': {'L':'L','R':'R','D':'LR','U':'LR'},
	     '|': {'L':'UD','R':'UD','D':'D','U':'U'}}

d_to_delta = {'U':(-1,0), 'D':(1,0), 'L': (0, -1), 'R': (0,1)}

def energize(si, sj, sd, lines):
    m, n = len(lines), len(lines[0])
    traveled = {(i,j,d): False for i in xrange(m) for j in xrange(n) for d in 'LRDU'}
    to_travel = [(si,sj,sd)]
    traveled[si,sj,sd] = True
    while to_travel:
        i,j,d = to_travel.pop()
        s = lines[i][j]
        for dd in next_dirs[s][d]:
            di, dj = d_to_delta[dd]
            ii, jj = i+di, j+dj
            if (ii,jj,dd) in traveled and not traveled[ii,jj,dd]:
                traveled[ii,jj,dd] = True
                to_travel.append((ii,jj,dd))
    return sum([any(traveled[i,j,d] for d in 'LRDU') for i in xrange(m) for j in xrange(n)])

# solve_easy
assert energize(0, 0, 'R', lines) == 8125

def solve_hard(lines):
    m, n = len(lines), len(lines[0])
    eners = [energize(i, 0, 'R', lines) for i in xrange(m)] +\
            [energize(0, j, 'D', lines) for j in xrange(n)] +\
            [energize(i, n-1, 'L', lines) for i in xrange(m)] +\
            [energize(m-1, j, 'U', lines) for n in xrange(n)]
    return max(eners)
assert solve_hard(lines) == 8489
