text = open('input_day15.txt').read()
seq = text.replace('\n','').split(',')

def fu(s):
    return sum(pow(17,i+1,256)*j for i, j in enumerate(map(ord, s[::-1])))%256

# Solve easy
assert sum(map(fu,seq)) == 505427

def act(cmd, boxes):
    if cmd[-1] == '-':
        label = cmd[:-1]
        box = boxes[fu(label)]
        if label in box[0]:
                ii = box[0].index(label)
                pp = box[0].pop(ii), box[1].pop(ii)
        return
    label, st = cmd.split('=')
    box = boxes[fu(label)]
    if label in box[0]:
            ii = box[0].index(label)
            box[1][ii] = int(st)
    else:
            box[0].append(label)
            box[1].append(int(st))

def solve_hard(seq):
    boxes = [([], []) for i in xrange(256)]
    for s in seq:
        act(s, boxes)
    return sum([(i+1)*(j+1)*t for i,b in enumerate(boxes) for j,t in enumerate(b[1])])

assert solve_hard(seq) == 243747
