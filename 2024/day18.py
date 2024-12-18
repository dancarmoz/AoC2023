text = open('input_day18.txt').read()
lines = text.splitlines()
blocks = [map(int,l.split(',')) for l in lines]

import heapq
N = 73
si, sj = 1, 1
ei, ej = N-2, N-2
dirs = [(0,1),(0,-1),(1,0),(-1,0)]

# The code is more general than necessary since it was mostly copy-pasted from day 16.
def dijkstra(t):
    grid = [[0] * N for i in range(N)]
    for i in range(N):
        grid[i][0] = grid[0][i] = grid[N-1][i] = grid[i][N-1] = 1
    for x,y in blocks[:t]:
        grid[x+1][y+1] = 1
    states = [(0, (si, sj))]
    solved = {}
    while states and (ei, ej) not in solved:
        s, state = heapq.heappop(states)
        ni, nj = state
        if state in solved: continue
        solved[state] = s
        for di, dj in dirs:
            if not grid[ni+di][nj+dj]:
                heapq.heappush(states, (s+1, (ni+di, nj+dj)))
    return solved.get((ei, ej), False)

def solve_day18_pt1():
    return dijkstra(1024)

def solve_day18_pt2():
    a, b = 1024, len(blocks)
    while b - a > 1:
        m = (b+a)/2
        a, b = (m, b) if dijkstra(m) else (a, m)
    return lines[a]
