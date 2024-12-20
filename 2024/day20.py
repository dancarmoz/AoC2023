text = open('input_day20.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])
ll = [l for l in lines if 'S' in l][0]; Si, Sj = lines.index(ll), ll.index('S')
ll = [l for l in lines if 'E' in l][0]; Ei, Ej = lines.index(ll), ll.index('E')

path = {(Si, Sj): 0}
ci, cj = Si, Sj
while (ci, cj) != (Ei, Ej):
    ns = [(ci + di, cj + dj) for di, dj in dirs]
    ni, nj = [(ni, nj) for ni, nj in ns if lines[ni][nj] != '#' and (ni, nj) not in path][0]
    path[ni,nj] = path[ci,cj] + 1
    ci, cj = ni, nj

def dist(p,q):
    return abs(q[0]-p[0])+abs(q[1]-p[1])

def find_cheats_lc(dis, minscore):
    dds = [(i,j) \
           for i in range(-dis,dis+1) for j in range(-dis,dis+1) if 1 < abs(i)+abs(j) <= dis]
    cheats = [(p,q,path[q]-path[p]-dist(p,q)) for p in path.keys() for q in \
              [(p[0]+i, p[1]+j) for i,j in dds] if q in path and path[q]-path[p] >= dist(p,q) + minscore]
    return len(cheats)

def find_cheats(dis, minscore):
    ncheats = 0
    dds = [(i,j,abs(i)+abs(j)) \
           for i in range(-dis,dis+1) for j in range(-dis,dis+1) if 1 < abs(i)+abs(j) <= dis]
    for p, pp in path.items():
        for i,j,d in dds:
            q = p[0]+i, p[1]+j
            if q in path and path[q] - pp >= d + minscore:
                ncheats += 1
    return ncheats

# ~10ms
def solve_day20_pt1():
    return find_cheats(2,100)

# ~1s
def solve_day20_pt2():
    return find_cheats(20,100)
