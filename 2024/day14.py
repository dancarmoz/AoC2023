text = open('input_day14.txt').read()
lines = text.splitlines()
# ns = map(int, lines[0].split())
# m, n = len(lines), len(lines[0])
import re
ns = [map(int,re.findall('[-\d]+',l)) for l in lines]
w, h = 101, 103

def product(li):
    return reduce(lambda x,y: x*y,li,1)

def solve_day14_pt1():
    nps = [((a+100*c) % w, ((b+100*d)%h)) for a,b,c,d in ns]
    quads = [0]*4
    for x,y in nps:
        if x == w/2 or y == h/2: continue
        q = (x < w/2) + (y < h/2)*2
        quads[q] += 1
    return product(quads)

# Scores a state based on adjacent robots on the x-axis, assuming a christmas tree has long rows.
def score_state(t):
    dd = set()
    for a,b,c,d in ns:
        dd.add(((a+t*c)%w,(b+t*d) % h))
    return sum([(x+1, y) in dd for x,y in dd])

def score_state_symmetry(t):
    dd = set()
    for a,b,c,d in ns:
        dd.add(((a+t*c)%w,(b+t*d) % h))
    return max([sum([(A-x, y) in dd for x,y in dd]) for A in range(2*(w-1))])

def argmax(scores):
    return max([(s,i) for i,s in enumerate(scores)])[1]

# Runs in ~1.3s.
def solve_day14_pt2():
    scores = map(score_state, range(w*h))
    return argmax(scores)

'''
In the correct configuration, the lines (horizontal or vertical) contatining the tree are much
denser than random ones. So if we count the number of robots in each line, the distribution in
the right time will be much more skewed, which can be detected by a function giving more weight
to higher density lines.
The useful property of this score is that these counts only depend on the elapsed time modulo
the line's length, as the periods of x or y coordinates are just the width and height, not their
product. Thus we can find the best "x" time and the best "y" time separately, and join them using
the Chinese Remainder Theorem.
'''
def score_projection(t, i):
    counts = [0]*((w,h)[i])
    for a,b,c,d in ns:
        coords = (a+t*c)%w,(b+t*d) % h
        counts[coords[i]] += 1
    return sum([a**4 for a in counts])

# Runs in ~17ms.
def solve_day14_pt2_crt():
    xt = argmax([score_projection(t, 0) for t in xrange(w)])
    yt = argmax([score_projection(t, 1) for t in xrange(h)])
    return (xt*inv_mod(h,w)*h + yt*inv_mod(w,h)*w)%(w*h)
    

def inv_mod(a,p):
    b = p
    caa, cba = 1, 0
    while b != 0:
        caa, cba = cba, caa - (a/b) * cba
        a, b = b , a%b
    # assert a == 1
    return caa
