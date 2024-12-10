text = open('input_day10.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])

def walk1(i,j,k):
    if not ((0 <= i < m) and (0 <= j <n)): return set()
    if not nss[i][j] == k: return set()
    if k == 9: return {(i,j)}
    return reduce(lambda x,y: x|y,
                  [walk1(ii,jj,k+1) for ii,jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]])

def solve_day10_pt1():
    return sum([len(walk1(i,j,0)) for i in range(m) for j in range(n)])

def walk2(i,j,k):
    if not ((0 <= i < m) and (0 <= j <n)): return 0
    if not nss[i][j] == k: return 0
    if k == 9: return 1
    return reduce(lambda x,y: x+y,
                  [walk2(ii,jj,k+1) for ii,jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]])

def solve_day10_pt2():
    return sum([(walk2(i,j,0)) for i in range(m) for j in range(n)])
