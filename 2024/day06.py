text = open('input_day06.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])
si = [i for i in xrange(m) if '^' in lines[i]][0]
sj = lines[si].index('^')
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_visited():
    visited = [[0]*n for i in xrange(m)]
    ci, cj, d = si, sj, 0
    while True:
        visited[ci][cj] = 1
        di, dj = dirs[d]
        ni, nj = ci+di, cj + dj
        if not (0 <= ni < m and 0 <= nj < n): break
        if lines[ni][nj] != '#':
            ci, cj = ni, nj
        else:
            d = (d + 1) % 4
    return visited

def solve_day06_pt1():
    visited = get_visited()
    return sum(map(sum, visited))

def is_looping(modlines):
    ci, cj, d = si, sj, 0
    visited = set()
    while True:
        if (ci, cj, d) in visited: return True
        visited.add((ci, cj, d))
        di, dj = dirs[d]
        ni, nj = ci+di, cj + dj
        if not (0 <= ni < m and 0 <= nj < n): return False
        if modlines[ni][nj] != '#':
            ci, cj = ni, nj
        else:
            d = (d + 1) % 4

def modify_lines(i,j):
    return lines[:i] + [lines[i][:j]+'#'+lines[i][j+1:]] + lines[i+1:]

def solve_day06_pt2():
    visited = get_visited()
    return sum([is_looping(modify_lines(i,j)) \
                for i in xrange(m) for j in xrange(n) \
                if visited[i][j] and (i,j) != (si, sj)])

def solve_day06_pt2_better():
    ci, cj, d = si, sj, 0
    visited = [[0]*n for i in xrange(m)]
    visited[si][sj] = 1
    path, count = [], 0
    while True:
        if not visited[ci][cj]:
            modlines = modify_lines(ci, cj)
            count += int(is_looping_from_path(modlines, path))
        path.append((ci, cj, d))
        visited[ci][cj] = 1
        di, dj = dirs[d]
        ni, nj = ci+di, cj + dj
        if not (0 <= ni < m and 0 <= nj < n): return count
        if lines[ni][nj] != '#':
            ci, cj = ni, nj
        else:
            d = (d + 1) % 4
