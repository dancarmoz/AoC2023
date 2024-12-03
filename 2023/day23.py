text = open('input_day23.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])
start, end = (0, 1), (m-1, n-2)

d_to_delta = {'^':(-1,0), 'v':(1,0), '<': (0, -1), '>': (0,1)}
delta_to_op = {d_to_delta[a]:b for a,b in zip('^v<>','v^><')}

def travel_easy(count, traveled, i, j):
    while True:
        count += 1
        if (i,j) == end: return count
        if lines[i][j] in d_to_delta:
            nexts = [d_to_delta[lines[i][j]]]
        else:
            nexts = d_to_delta.values()
        filt_nexts = []
        for di, dj in nexts:
            ii, jj = i+di, j+dj
            if lines[ii][jj] in ['#',delta_to_op[di,dj]] or (ii,jj) in traveled: continue
            filt_nexts.append((ii,jj))
        if not filt_nexts: return -1
        elif len(filt_nexts) == 1:
            (i, j), = filt_nexts
            traveled.add((i, j))
            continue
        else:
            return max([travel_easy(count, traveled | set([(ii,jj)]), ii, jj) for ii, jj in filt_nexts])

# Start after first step, to avoid boundary issues.
assert travel_easy(0, set([start, (1, 1)]), 1, 1) == 2190

lines_hard = text.replace('<','.').replace('>','.').replace('v','.').replace('^','.').splitlines()
# Reduce the problem to the graph between non-linear nodes, to speed up main backtrack.
nodes = [start, end] + [
    (i,j) for i in xrange(1,m-1) for j in xrange(1,n-1)
    if lines_hard[i][j] == '.' and
    len([(di,dj) for di, dj in delta_to_op if lines_hard[i+di][j+dj]=='.']) > 2]
nodes_to_i = {n: i for i,n in enumerate(nodes)}
N = len(nodes)
graph = [[] for i in xrange(N)]
for ni in xrange(2, N):
    nn = nodes[ni]
    for (di, dj) in delta_to_op:
        prev = (i, j) = nn
        cur = (ii, jj) = (i+di, j+dj)
        if lines_hard[ii][jj] == '#': continue
        count = 1
        while cur not in nodes_to_i:
            i, j = cur
            nx = [(i+di, j+dj) for di, dj in delta_to_op
                  if lines_hard[i+di][j+dj] == '.' and (i+di, j+dj) != prev]
            if len(nx) == 0: break
            elif len(nx) == 1:
                prev, cur = cur, nx[0]
                count += 1
                continue
            assert False
        if cur in nodes_to_i:
            graph[ni].append((nodes_to_i[cur], count))
for ni in xrange(2,N):
    for s,d in graph[ni]:
        if s < 2:
            graph[s].append((ni,d))

traveled = [1] + [0]*(N-1)
def travel_hard(count, traveled, node):
    if node == 1: return count
    res = -1
    for nd, dist in graph[node]:
        if traveled[nd]: continue
        traveled[nd] = 1
        res = max(res, travel_hard(count + dist, traveled, nd))
        traveled[nd] = 0
    return res

# assert travel_hard(0, traveled, 0) == 6258 # works, but takes ~10s

# Faster solution method by Yoaz Tzfati
BEST = 0
def travel_hard_bnb(count, node, bound):
    global BEST, traveled
    if node == 1:
        BEST = max(count, BEST)
        return
    bound -= sum([d for nd, d in graph[node] if not traveled[nd]])
    for nd, dist  in graph[node]:
        if bound + dist < BEST or traveled[nd]: continue
        traveled[nd] = 1
        travel_hard_bnb(count + dist, nd, bound + dist)
        traveled[nd] = 0

def solve_hard_bnb():
    global BEST, traveled
    BEST = 0
    traveled = [1] + [0]*(N-1)
    total_bound = sum(d for edges in graph for u, d in edges)/2
    travel_hard_bnb(0, 0, total_bound)
    return BEST

assert solve_hard_bnb() == 6258
