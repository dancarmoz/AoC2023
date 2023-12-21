text = open('input_day21.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])

# Check special map properties, crucial for hard part.
assert m == n == 131
assert lines[m/2][n/2] == 'S'
start = (m/2, n/2)
assert '#' not in [lines[i][j] for iis, jjs in [
    ([0]*n, range(n)), ([m/2]*n, range(n)), ([m-1]*n, range(n)),
    (range(m), [0]*m), (range(m), [n/2]*m), (range(m), [n-1]*m)
    ] for i,j in zip(iis, jjs)]

def solve_easy_naive(lines, start, k):
    cur_set = set([start])
    for t in xrange(k):
        cur_set = set([
            (ii,jj) for i,j in cur_set for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            if lines[ii][jj] != '#'])
    return len(cur_set)

assert solve_easy_naive(lines, start, 64) == 3758

# Only remember the wavefront. This works on my input, but maybe not always?
def solve_easy_better(lines, start, k):
    sizes = [0, 1]
    cur_set, prev_set = set([start]), set()
    for t in xrange(k):
        prev_set, cur_set = cur_set, set([
            (ii,jj) for i,j in cur_set for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            if lines[ii % m][jj % n] != '#' and (ii,jj) not in prev_set])
        sizes.append(sizes[-2] + len(cur_set))
    return sizes[1:]

assert solve_easy_better(lines, start, 64)[-1] == 3758

step_count = 26501365
# step count is in fact 2023*100*131 + 65.
assert step_count % m == (m-1)/2

def delta_sub(lst, d = 1):
    return [y-x for x,y in zip(lst[:-d], lst[d:])]

def solve_hard_interpolate(lines, start, step_count):
    sizes = solve_easy_better(lines, start, m*5)[step_count % m :: m]
    diff = delta_sub(sizes)
    diff_diff = delta_sub(diff)
    assert len(set(diff_diff)) == 1
    A, B, C = diff_diff[0], diff[0], sizes[0]
    bb = step_count / m
    return A*bb*(bb-1)/2 + B*bb + C

assert solve_hard_interpolate(lines, start, step_count) == 621494544278648

def solve_hard_investigate(lines, start, step_count):
    cur_set, prev_set, target_set = set([start]), set(), set()
    for t in xrange(m/2 + 2*m):
        prev_set, cur_set = cur_set, set([
            (ii,jj) for i,j in cur_set for ii,jj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            if lines[ii % m][jj % n] != '#' and (ii,jj) not in prev_set])
        if (t+1)%2 == 1:
            target_set |= cur_set
    blocks = {(i,j):0 for i in range(-2,3) for j in range(-2,3)}
    for i,j in target_set:
        blocks[i/m,j/n] += 1
    A = blocks[-2, 0] + blocks[ 2, 0] + blocks[ 0,-2] + blocks[ 0, 2]
    B = blocks[-1,-1] + blocks[-1, 1] + blocks[ 1,-1] + blocks[ 1, 1]
    C = blocks[ 1, 2] + blocks[-1, 2] + blocks[ 1,-2] + blocks[-1,-2] # (same as +-2, +-1)
    D = blocks[ 0, 1] # Same as (+-1, 0), (0, +-1)
    E = blocks[ 0, 0]
    bb = step_count / m
    return A + (bb-1)*B + bb*C + bb**2*D + (bb-1)**2*E

assert solve_hard_investigate(lines, start, step_count) == 621494544278648
