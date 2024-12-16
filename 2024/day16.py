text = open('input_day16.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])
Si, Sj = m-2, 1
Ei, Ej = 1, n-2

import heapq
dirs = {0: (0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}

# runs in ~130ms
def solve_day16_pt1():
    solved = dict()
    states = [(0, (Si, Sj, 0))]
    while states and (Ei, Ej, 0) not in solved and (Ei, Ej, 1) not in solved:
        s, state = heapq.heappop(states)
        ni, nj, d = state
        if state in solved: continue
        solved[state] = s
        heapq.heappush(states, (s+1000, (ni, nj, (d+1)%4)))
        heapq.heappush(states, (s+1000, (ni, nj, (d-1)%4)))
        di, dj = dirs[d]
        if lines[ni+di][nj+dj] != '#':
            heapq.heappush(states, (s+1, (ni+di, nj+dj, d)))
    return max(solved.get((Ei, Ej, 0), -1), solved.get((Ei, Ej, 1), -1))


# runs in ~280ms, note that this includes the runtime of pt1
def solve_day16_pt2():
    pt1_score = solve_day16_pt1()
    states = [(0, (Si, Sj, 0), None)]
    solved = dict()
    while states:
        s, state, pstate = heapq.heappop(states)
        if s > pt1_score: break
        ni, nj, d = state
        if state in solved:
            if solved[state][0] == s:
                solved[state][1].add(pstate)
            continue
        solved[state] = (s, {pstate})
        heapq.heappush(states, (s+1000, (ni, nj, (d+1)%4), state))
        heapq.heappush(states, (s+1000, (ni, nj, (d-1)%4), state))
        di, dj = dirs[d]
        if lines[ni+di][nj+dj] != '#':
            heapq.heappush(states, (s+1, (ni+di, nj+dj, d), state))
    # backtrace paths
    queue = [(Ei, Ej, d) for d in range(2) if solved.get((Ei, Ej, d), (0,None))[0] == pt1_score]
    inpaths = set()
    while queue:
        state = queue.pop()
        if state not in inpaths and state:
            inpaths.add(state)
            queue += list(solved[state][1])
    return len(set([(i,j) for i,j,d in inpaths]))
