text = open('input_day13.txt').read()
lines = text.splitlines()
# ns = map(int, lines[0].split())
# m, n = len(lines), len(lines[0])

import re
games = [[map(int,re.findall('\d+', l)) for l in b.splitlines()] for b in text.split('\n\n')]


def play_pt1(game):
	(ax,ay),(bx,by),(tx,ty) = game
	gs = [(i, (tx-ax*i)/bx) for i in range(101) if \
              (tx-ax*i) % bx == 0 and (tx -ax*i)*by == (ty - ay*i)*bx]
	if not gs: return 0
	return min([3*i+j for i,j in gs])

def solve_day13_pt1():
    return sum(map(play_pt1,games))

def play_pt2(game):
    ex = 10000000000000
    (ax,ay),(bx,by),(tx,ty) = game
    tx, ty = tx+ex, ty+ex
    dd = -(ax*by - ay*bx)
    rx, ry = bx*ty - tx*by, tx*ay - ax*ty
    if not ((rx % dd) == 0 and (ry % dd) == 0): return 0
    rx /= dd
    ry /= dd
    if not (rx >= 0 and ry >= 0): return 0
    return 3*rx + ry

def solve_day13_pt2():
    return sum(map(play_pt2,games))
