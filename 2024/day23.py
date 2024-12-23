text = open('input_day23.txt').read()
lines = text.splitlines()
import itertools as it
# ns = map(int, lines)
# m, n = len(lines), len(lines[0])

edges = [l.split('-') for l in lines]
edgset = set(sum([[tuple(e), tuple(e[::-1])] for e in edges],[]))
verts = set(sum(edges, []))
gv = {v : [] for v in verts}
for u,v in edgset:
    gv[u].append(v)
gvs = {v:set(gv[v]) for v in verts}

# ~8ms
def solve_day23_pt1():
    return sum([((v,w) in edgset and (u[0] == 't' or v[0] == 't' or w[0] == 't'))
                for u, nu in gv.items() for v,w in it.combinations(nu,2)])/3


def max_clique(used, rems):
    global MAX_LEN, MAX_CLIQUE
    if len(used) + len(rems) <= MAX_LEN: return
    if not rems:
            MAX_LEN = len(used)
            MAX_CLIQUE = used
    for r in rems:
            max_clique(used+[r], rems & gvs[r])
            rems = rems - set([r])

# ~4ms
def solve_day23_pt2():
    global MAX_LEN, MAX_CLIQUE
    MAX_LEN, MAX_CLIQUE = 0, []
    max_clique([], verts)
    return ','.join(sorted(MAX_CLIQUE))
