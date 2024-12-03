import heapq
text = open('input_day17.txt').read()
lines = text.splitlines()
heats = [map(int, l) for l in lines]

d_to_delta = {'U':(-1,0), 'D':(1,0), 'L': (0, -1), 'R': (0,1)}

# My original solution for the first stage. In retrospect, the more general solution for the
# second case is also better for the first case (simpler code and fewer vertices).
nexts_easy = {'': 'DR',
     'D': 'LRD', 'DD': 'LRD', 'DDD': 'LR',
     'U': 'LRU', 'UU': 'LRU', 'UUU': 'LR',
     'L': 'UDL', 'LL': 'UDL', 'LLL': 'UD',
     'R': 'UDR', 'RR': 'UDR', 'RRR': 'UD'}

def solve_easy(heats):
    m, n = len(heats), len(heats[0])
    verts = {(i,j,s):1000000000 for i in xrange(m) for j in xrange(n) for s in nexts_easy}
    verts[0,0,''] = 0
    to_touch, touched = [(0,(0,0,''))], set()
    
    while to_touch:
        v, (i, j, d)  = heapq.heappop(to_touch)
        if (i,j,d) in touched: continue
        touched.add((i,j,d))
        if (i,j) == (m-1, n-1):
            return v
        for nd in nexts_easy[d]:
            di, dj = d_to_delta[nd]
            ii, jj = i+di, j+dj
            if d and d[-1] == nd: nd = d + nd
            if (ii,jj,nd) not in verts: continue
            nv = v + heats[ii][jj]
            if nv < verts[ii,jj,nd]:
                verts[ii,jj,nd] = nv
                heapq.heappush(to_touch, (nv, (ii, jj, nd)))

assert solve_easy(heats) == 724

nexts_hard = {'': 'DR',
     'D': 'LR',
     'U': 'LR',
     'L': 'UD',
     'R': 'UD'}

def solve_hard(heats, min_step, max_step):
    m, n = len(heats), len(heats[0])
    verts = {(i,j,s):1000000000 for i in xrange(m) for j in xrange(n) for s in 'LRDU'}
    verts[0,0,''] = 0
    to_touch, touched = [(0,(0,0,''))], set()

    while to_touch:
        v, (i, j, d)  = heapq.heappop(to_touch)
        if (i,j,d) in touched: continue
        touched.add((i,j,d))
        if (i,j) == (m-1, n-1):
            return v
        for nd in nexts_hard[d]:
            di, dj = d_to_delta[nd]
            for k in xrange(min_step, max_step + 1):
                ii, jj = i+k*di, j+k*dj
                if (ii,jj,nd) not in verts: continue
                nv = v + sum(heats[i+kk*di][j+kk*dj] for kk in xrange(1,k+1))
                if nv < verts[ii,jj,nd]:
                    verts[ii,jj,nd] = nv
                    heapq.heappush(to_touch, (nv, (ii, jj, nd)))

assert solve_hard(heats, 4, 10) == 877
# Solve easy with hard
assert solve_hard(heats, 1, 3) == 724
