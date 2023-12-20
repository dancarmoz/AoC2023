text = open('input_day20.txt').read()
lines = text.splitlines()

dd = {}
for l in lines:
    sp = l.split(' -> ')
    if sp[0] == 'broadcaster': k, cmd  = 'start', '0'
    else: k, cmd = sp[0][1:], sp[0][0]
    dd[k] = (cmd, sp[1].split(', '))



def solve_easy(dd):
    sigs = [0, 0]
    flip_flops = {k : 0 for k in dd.keys() if dd[k][0] == '%'}
    cons = {k : {kk: 0 for kk, v in dd.items() if k in v[1]} for k in dd.keys() if dd[k][0] == '&'}
    for i in xrange(1000):
        sigs[0] += 1
        signals = [(k, 0, 'start') for k in dd['start'][1]]
        while signals:
            dest, sig, source = signals.pop(0)
            sigs[sig] += 1
            if dest in flip_flops and sig == 0:
                flip_flops[dest] ^= 1
                nsig = flip_flops[dest]
                signals += [(k, nsig, dest) for k in dd[dest][1]]
            elif dest in cons:
                cons[dest][source] = sig
                nsig = not all(cons[dest].values())
                signals += [(k, nsig, dest) for k in dd[dest][1]]
    return sigs[0] * sigs[1]

assert solve_easy(dd) == 807069600

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(x,y):
    return x*y/gcd(x,y)

def solve_hard_1(dd):
    flip_flops = {k : 0 for k in dd.keys() if dd[k][0] == '%'}
    cons = {k : {kk: 0 for kk, v in dd.items() if k in v[1]} for k in dd.keys() if dd[k][0] == '&'}
    rx_source = [k for k in dd if 'rx' in dd[k][1]][0]
    times = {s : [] for s in cons[rx_source].keys()}
    for i in xrange(20000):
        signals = [(k, 0, 'start') for k in dd['start'][1]]
        while signals:
            dest, sig, source = signals.pop(0)
            if dest == rx_source and sig == 1:
                times[source].append(i+1)
            if dest in flip_flops and sig == 0:
                flip_flops[dest] ^= 1
                nsig = flip_flops[dest]
                signals += [(k, nsig, dest) for k in dd[dest][1]]
            elif dest in cons:
                cons[dest][source] = sig
                nsig = not all(cons[dest].values())
                signals += [(k, nsig, dest) for k in dd[dest][1]]
    # Assert simple periodic sequences.
    for t in times.values():
        assert set(t[:1]) == set([y-x for x,y in zip(t[:-1],t[1:])])
    return reduce(lcm, [t[0] for t in times.values()])

assert solve_hard_1(dd) == 221453937522197

# Calculate the periods directly from the mask circuits.
def solve_hard_2(dd):
    flip_flops = {k : 0 for k in dd.keys() if dd[k][0] == '%'}
    cons = {k : {kk: 0 for kk, v in dd.items() if k in v[1]} for k in dd.keys() if dd[k][0] == '&'}
    masks = []
    for ss in dd['start'][1]:
        mask, bit, dic = 0, 1, {}
        while ss in flip_flops:
            nexts = [aaa for aaa in dd[ss][1] if aaa in flip_flops]
            to_tap = [aaa for aaa in dd[ss][1] if aaa in cons]
            dic[ss] = bit
            mask += bit*len(to_tap)
            bit *= 2
            if len(nexts) == 0:
                ss = to_tap[0]
            else:
                assert len(nexts) == 1
                ss = nexts[0]
        feed = sum(dic.get(k, 0) for k in dd[ss][1])
        assert feed + mask == 2**12
        masks.append(mask)
    return reduce(lcm, masks)

assert solve_hard_2(dd) == 221453937522197
	

    
