text = open('input_day01.txt').read()
lines = text.splitlines()
left, right = zip(*[map(int,x.split()) for x in lines])
ls, rs = map(sorted, [left, right])

from collections import Counter

def solve_day01_pt1():
    return sum([abs(y-x) for x,y in zip(ls, rs)])

def solve_day01_pt2():
    cnt = Counter(rs)
    return sum([x*cnt.get(x,0) for x in ls])
