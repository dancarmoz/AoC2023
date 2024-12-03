from numpy import searchsorted

text = open('input_day05.txt').read()
blocks = text.split('\n\n')
blines = [b.splitlines()[1:] for b in blocks[1:]]
ranges = [sorted([map(int, x.split()) for x in bl], key = lambda x:x[1]) for bl in blines]

seeds = map(int, blocks[0].split()[1:])

def solve_easy(seeds, ranges):
    res = []
    for seed in seeds:
        for bl in ranges:
            ii = searchsorted([x[1] for x in bl], seed, side='right')-1
            dest, source, l = bl[ii]
            if source <= seed < source + l:
                seed += dest - source
        res.append(seed)
    return min(res)

assert solve_easy(seeds, ranges) == 173706076

seed_ranges = zip(seeds[::2], seeds[1::2])

def solve_hard(seed_ranges, ranges):
    modified_ranges = []
    for rng in ranges:
        res = []
        for i in xrange(len(rng)-1):
            res.append(rng[i])
            d,s,l = rng[i]
            if rng[i+1][1] > s + l:
                res.append([s+l, s+l, rng[i+1][1]-(s+l)])
        res.append(rng[-1])
        modified_ranges.append(res)

    cur_ranges = seed_ranges[:]
    for bl in modified_ranges:
        next_ranges = []
        ind = 0
        while ind < len(cur_ranges):
            start, le = cur_ranges[ind]
            ii = searchsorted([x[1] for x in bl], start+1, side='right')-1
            if ii == -1:
                next_ranges.append((start, min(le, bl[0][1] - start)))
                if bl[0][1] < start + le:
                    cur_ranges[ind] = (bl[0][1], le - (bl[0][1] - start))
                else:
                    ind += 1
                continue
            dest, source, l = bl[ii]
            rlen = max(min(le, l - (start - source)),0)
            next_ranges.append((start + dest - source, rlen))
            if le == rlen:
                ind += 1
                continue
            if rlen > 0:
                cur_ranges[ind] = (source + l, le - rlen)
                continue
            if ii != len(bl) - 1:
                print ii, (start, le), (dest, source, l), rlen
                assert False
            next_ranges.append((start, le))
            ind += 1
        cur_ranges = next_ranges

    return min(cur_ranges)[0]

assert solve_hard(seed_ranges, ranges) == 11611182
