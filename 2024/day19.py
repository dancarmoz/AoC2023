text = open('input_day19.txt').read()
texts = text.split('\n\n')
towelset = set(texts[0].split(', '))
designs = texts[1].splitlines()
# m, n = len(lines), len(lines[0])

def pos(des):
    posend = [0]*len(des)+[1]
    for i in xrange(len(des)-1,-1,-1):
        for j in xrange(i+1,len(des)+1):
            if posend[j] and des[i:j] in twlset:
                posend[i] = 1
                break
    return posend[0]

def solve_day19_pt1():
    return sum(map(pos, designs))

def pos_count(des):
    posend = [0]*len(des)+[1]
    for i in xrange(len(des)-1,-1,-1):
        for j in xrange(i+1,len(des)+1):
            if des[i:j] in towelset:
                posend[i] += posend[j]
    return posend[0]

def solve_day19_pt2():
    return sum(map(pos_count, designs))
