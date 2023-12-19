text = open('input_day19.txt').read()
blocks = text.split('\n\n')

flows_d = {f[:f.index('{')] : [x.split(':')  for x in f[f.index('{') + 1 : -1].split(',')]
           for f in blocks[0].splitlines()}
x,m,a,s = 'xmas'
parts = [eval(p.replace('=',':')) for p in blocks[1].splitlines()]

def process(p, flows_d):
    counter = 0
    f = flows_d['in']
    # Lazy way to avoid possible infinite loop
    for counter in xrange(len(flows_d) + 1):
        for cmd in f:
            if len(cmd) == 1:
                res = cmd[0]
                break
            cond, res = cmd
            if eval(str(p[cond[0]])+cond[1:]):
                break
        if res == 'A': return True
        if res == 'R': return False
        f = flows_d[res]
    return False

def solve_easy(flows_d, parts):
    return sum(sum(p.values()) for p in parts if process(p, flows_d))

assert solve_easy(flows_d, parts) == 425811

def trace(box, fl, passed, flows_d):
    if fl == 'A': return [box]
    if fl in passed: return [] # 'R' or infinite loop
    passed = set(passed)
    passed.add(fl)
    cmds = flows_d[fl]
    res = []
    for cond, dest in cmds[:-1]:
        box_t, box = split_box(box, cond)
        if box_t:
            res += trace(box_t, dest, passed, flows_d)
        if not box:
            break
    else:
        res += trace(box, cmds[-1][0], passed, flows_d)
    return res

prod = lambda lst: reduce(lambda x,y: x*y, lst)

def solve_hard(flows_d):
    start_box = {t:(1,4001) for t in 'xmas'}
    res = trace(start_box, 'in', set(['R']), flows_d)
    return sum(prod(b - a for a,b in box.values()) for box in res)

assert solve_hard(flows_d) == 131796824371749
