from itertools import combinations

text = open('input_day11.text').read()
lines = text.splitlines()

def solve(lines, spacing):
    m, n = len(lines), len(lines[0])
    rows = set([i for i in xrange(m) if lines[i] == '.'*n])
    cols = set([j for j in xrange(n) if all(lines[i][j]=='.' for i in xrange(m))])
    iis, jjs = [0], [0]
    for i in xrange(m):
        iis.append(iis[-1] + (spacing if i in rows else 1))
    for j in xrange(n):
        jjs.append(jjs[-1] + (spacing if j in cols else 1))
    hashes = [(iis[i],jjs[j]) for i in xrange(m) for j in xrange(n) if lines[i][j] == '#']
    return sum([abs(ii-i)+abs(jj-j) for (i,j),(ii,jj) in combinations(hashes, 2)])
        
assert solve(lines, 2) == 9623138
assert solve(lines, 1000000) == 726820169514

# alternative way to reach 1000000, if 2 had been worked out manually:
s1, s2 = solve(lines, 1), solve(lines, 2)
assert solve(lines, 1000000) == s1 + (s2 - s1)*999999
