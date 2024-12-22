text = open('input_day21.txt').read()
lines = text.splitlines()
# m, n = len(lines), len(lines[0])

board0 = ['789','456','123','#0A']
board1 = ['#^A','<v>']
d0, d1 = [{board[i][j]:(i,j) for i in range(len(board)) for j in range(3)} \
          for board in [board0, board1]]

def paths_from_to_forb(s,e,f):
    si, sj = s
    ei, ej = e
    ci = ('^' if ei < si else 'v')*abs(si-ei)
    cj = ('<' if ej < sj else '>')*abs(sj-ej)
    res = []
    if (si, ej) != f: res.append(cj+ci+'A')
    if (ei, sj) != f: res.append(ci+cj+'A')
    return set(res)

def get_paths(s, d):
    c = d['A']
    paths = ['']
    for n in s:
        npaths = paths_from_to_forb(c, d[n], d['#'])
        paths = [p+np for p in paths for np in npaths]
        c = d[n]
    return paths

def part1_helper(s):
    z = get_paths(s, d0)
    z = sum([get_paths(x,d1) for x in z],[])
    z = sum([get_paths(x,d1) for x in z],[])
    return min(map(len,z))

# ~25ms
def solve_day21_pt1():
    return sum([int(s[:-1]) * part1_helper(s) for s in lines])

# ~1ms
def solve_day21_pt2():
    ds = 'A<>^v'
    npresses = {(i,j): 1 for i in ds for j in ds}
    for t in range(25):
        npresses = {(i,j): min([
            sum([npresses[x,y] for x,y in zip('A'+s[:-1],s)])
            for s in paths_from_to_forb(d1[i],d1[j],d1['#'])])
            for i in ds for j in ds}
    return sum([int(l[:-1]) * min([
        sum([npresses[x,y] for x,y in zip('A'+s[:-1],s)])
        for s in get_paths(l, d0)]) for l in lines])
