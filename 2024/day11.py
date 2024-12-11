text = open('input_day11.txt').read()
lines = text.splitlines()
ns = map(int, lines[0].split())

# poor man's @functools.cache :(
blinks = {}
def blink(s, k):
    if k == 0: return 1
    if (s,k) not in blinks:
        ss = str(s)
        if s == 0:
            ne = [1]
        elif len(ss) % 2 == 0:
            ne = [int(ss[:len(ss)/2]), int(ss[len(ss)/2:])]
        else:
            ne = [s*2024]
        blinks[s, k] = sum([blink(n,k-1) for n in ne])
    return blinks[s, k]

# first run takes ~4ms
def solve_day11_pt1():
    return sum([blink(n, 25) for n in ns])

# first run (after running pt1) takes ~210ms
def solve_day11_pt2():
    return sum([blink(n, 75) for n in ns])
