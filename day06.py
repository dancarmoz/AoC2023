text = open('input_day06.txt').read()
lines = text.splitlines()
times, dists = [map(int, x.split()[1:]) for x in lines]

product = lambda ls: reduce(lambda x,y: x*y, ls)

def solve_easy(times, dists):
    return product([len([k for k in range(n) if k*(n-k) > d]) for n,d in zip(times,dists)])

assert solve_easy(times, dists) == 3317888

tm, dist = [int(''.join(x.split(':')[1].split())) for x in lines]

def solve_hard(tm, dist):
    for k in xrange(tm/2 + 1):
        if k*(tm - k) > dist:
            return tm - 2*k  + 1

assert solve_hard(tm, dist) == 24655068
