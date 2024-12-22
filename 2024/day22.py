text = open('input_day22.txt').read()
lines = text.splitlines()
ns = map(int, lines)
# m, n = len(lines), len(lines[0])

def advsec(x):
    x = (x ^ (x<<6)) & 0xffffff
    x = (x ^ (x>>5)) & 0xffffff
    x = (x ^ (x<<11)) & 0xffffff
    return x

def adv2000(x):
    for i in xrange(2000):
        x = advsec(x)
    return x

# runs in ~1s
def solve_day22_pt1():
    return sum(map(adv2000,ns))

def add_monkey_deals(x, d):
    prices = [x%10]
    for i in xrange(2000):
        x = advsec(x)
        prices.append(x%10)
    diffs = [y-x for x,y in zip(prices[:-1], prices[1:])]
    seen = set()
    for i in range(4,2001):
        z = tuple(diffs[i-4:i])
        if z not in seen:
            seen.add(z)
            d[z] = d.get(z,0) + prices[i]

# runs in ~4.54s
def solve_day22_pt2():
    d = {}
    for x in ns:
        add_monkey_deals(x, d)
    return max(d.values())
