text = open('input_day08.txt').read()
lines = text.splitlines()
lr = lines[0]
lr_len = len(lr)
dd = {}
for r in lines[2:]:
    a,b,c = r.replace('=','').replace('(','').replace(',','').replace(')','').split()
    dd[a] = {'L':b,'R':c}


def solve_easy(dd):
    cur, count = 'AAA', 0
    while cur != 'ZZZ':
        cur = dd[cur][lr[count % lr_len]]
        count += 1
    return count

assert solve_easy(dd) == 14893

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(x,y):
    return x*y/gcd(x,y)

def solve_hard(dd):
    starts = [k for k in dd if k.endswith('A')]

    to_next_z = {k : [None]*lr_len for k in dd}
    def populate(k, i):
        path = [(k, i)]
        nk, ni = dd[k][lr[i]], (i+1)%lr_len
        while not (nk.endswith('Z') or to_next_z[nk][ni]):
            path.append((nk, ni))
            nk, ni = dd[nk][lr[ni]], (ni+1)%lr_len
        if nk.endswith('Z'):
            end, l = nk, 0
        else:
            end, l = to_next_z[nk][ni]
        for j,(kk,ii) in enumerate(path[::-1]):
            to_next_z[kk][ii] = (end, l+j+1)
        if not to_next_z[nk][ni]:
            return (nk, ni)
        return None

    for ks in starts:
        cur = (ks, 0)
        while cur and not to_next_z[cur[0]][cur[1]]:
            cur = populate(*cur)

    # Assert the problem is in easy-mode.
    for ks in starts:
        ke, l = to_next_z[ks][0]
        assert l % lr_len == 0
        assert (ke, l) == to_next_z[ke][0]

    return reduce(lcm, [to_next_z[ks][0][1] for ks in starts])

assert solve_hard(dd) == 10241191004509
