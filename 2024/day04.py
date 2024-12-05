text = open('input_day04.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])

def solve_day4_pt1():
    dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
    xmass = [
        (i, j, (di, dj)) for i in range(m) for j in range(n) for di, dj in dirs
        if 'XMAS' == ''.join([
            lines[ii][jj] if (0 <= ii < m and 0 <= jj < n) else ''
            for ii, jj in [(i + k*di, j + k*dj) for k in range(4)]
        ])]
    return len(xmass)

def solve_day4_pt2():
    x_mass = [(i, j) for i in range(1, m-1) for j in range(1, n-1)
              if lines[i][j] == 'A' and
              sorted([lines[i-1][j-1],lines[i+1][j+1]]) == \
              sorted([lines[i+1][j-1],lines[i-1][j+1]]) == ['M','S']]
    return len(x_mass)
