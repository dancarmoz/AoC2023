text = open('input_day22.txt').read()
lines = text.splitlines()
brickss = [[map(int,x.split(',')) for x in l.split('~')] for l in lines]
bricks = [[
    [x,y,z]
    for x in xrange(b[0], c[0]+1)
    for y in xrange(b[1], c[1]+1)
    for z in xrange(b[2], c[2]+1)
] for b,c in brickss]

# Initialize world state. The ground is -10, the air is -1
X, Y, Z = [max([x[i] for y in brickss for x in y])+1 for i in xrange(3)]
world = [[[-10] + [-1]*(Z-1) for y in xrange(Y)] for x in xrange(X)]
for i,b in enumerate(bricks):
    for x,y,z in b:
        world[x][y][z] = i

# Let bricks fall to final position
flag = True
while flag:
    flag = False
    for i,b in enumerate(bricks):
        if not all(world[x][y][z-1] in [-1,i] for x,y,z in b): continue
        flag = True
        for j in xrange(len(b)):
            x,y,z = b[j]
            world[x][y][z-1], world[x][y][z] = i, -1
            b[j] = x,y,z-1

# Get sets of "resing on", ignoring self and air:
is_on = []
for i,b in enumerate(bricks):
    is_on.append(set(world[x][y][z-1] for x,y,z in b) - set([-1,i]))

def solve_easy(is_on):
    unsafes = reduce(set.union, [x for x in is_on if len(x)==1]) - set([-10])
    return len(bricks) - len(unsafes)

assert solve_easy(is_on) == 471

def solve_hard(is_on):
    res = 0
    for i in xrange(len(bricks)):
        would_fall = set([i])
        flag = True
        while flag:
            flag = False
            for j in xrange(len(bricks)):
                if j in would_fall: continue
                if len(is_on[j] - would_fall) == 0:
                    flag = True
                    would_fall.add(j)
        res += len(would_fall) - 1
    return res

# Timed at about 1.16 seconds.
assert solve_hard(is_on) == 68525
