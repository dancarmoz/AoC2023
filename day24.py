import itertools as it
import numpy

text = open('input_day24.txt').read()
lines = text.splitlines()
stones = [[map(int, x.split(', ')) for x in l.split('@')] for l in lines]

def cross2d(s0, s1):
    (pxa, pya, pza), (vxa, vya, vza) = s0
    (pxb, pyb, pzb), (vxb, vyb, vzb) = s1
    la = lxa, lya, lza  = vya, -vxa, vxa*pya - vya*pxa
    lb = lxb, lyb, lzb  = vyb, -vxb, vxb*pyb - vyb*pxb
    la *= 2; lb *= 2
    sx, sy, sz  = [la[i+1]*lb[i+2] - la[i+2]*lb[i+1] for i in xrange(3)]
    if sz == 0: return (0, 0)
    sx, sy = sx/float(sz), sy/float(sz)
    if (sx - pxa)/vxa < 0 or (sx - pxb)/vxb < 0: return (0, 0)
    return sx, sy

def solve_easy(stones):
    mm, MM = 200000000000000, 400000000000000
    cpairs = [cross2d(*p) for p in it.combinations(stones, 2)]
    return sum([(mm <= x <= MM) and (mm <= y <= MM) for x,y in cpairs])

assert solve_easy(stones) == 16172

def stone_to_eq(s):
    (pxa, pya, pza), (vxa, vya, vza) = s
    return [vya, -vxa, -pya, pxa, 1, vxa*pya - vya*pxa]

def stone_to_eq_yz(s):
    # Same as above, but with x,y actually being the y,z coords
    (pza, pxa, pya), (vza, vxa, vya) = s
    return [vya, -vxa, -pya, pxa, 1, vxa*pya - vya*pxa]

# This actually isn't how I solved it - I assumed it was broken, i.e. the precision for px, py / py, pz
# wasn't good enough, and only checked it later. It turns out that it is good enough for yz but not for xy or zx,
# in my input. The inaccuracy is very small: it could also be easily fixed by enumerating over small (< 10)
# modifications to px, py, pz. Or by trying different sets of stones rather than the first 5.
# Slightly higher accuracy in float or integer arithmetic than numpy supports would also assure success.
def solve_hard_broken(stones):
    eqs = map(stone_to_eq, stones[:5])
    arr = numpy.array([e[:-1] for e in eqs])
    px, py, vx, vy, _ = [int(round(r)) for r in numpy.linalg.solve(arr, [-e[-1] for e in eqs])]
    res_xy = [px, py, vx, vy, py*vx - px*vy, 1]
    # Check precision.
    assert all(sum(a*b for a,b in zip(res_xy, e)) == 0 for e in eqs)
    
    eqs = map(stone_to_eq_yz, stones[:5])
    arr = numpy.array([e[:-1] for e in eqs])
    py2, pz, vy2, vz, _ = [int(round(r)) for r in numpy.linalg.solve(arr, [-e[-1] for e in eqs])]
    res_yz = [py2, pz, vy2, vz, pz*vy2 - py2*vz, 1]
    # Check precision.
    assert all(sum(a*b for a,b in zip(res_yz, e)) == 0 for e in eqs)
    assert py == py2 and vy == vy2
    return px + py + pz

def stone_to_eq_with_v(s, v):
    vx, vy, vz = v
    (pxa, pya, pza), (vxa, vya, vza) = s
    return [vya - vy, vx - vxa, (vxa - vx)*pya - (vya - vy)*pxa]

def stone_to_eq_yz_with_v(s, v):
    vz, vx, vy = v
    (pza, pxa, pya), (vza, vxa, vya) = s
    return [vya - vy, vx - vxa, (vxa - vx)*pya - (vya - vy)*pxa]

def solve2(eqs):
    a, b, e = eqs[0]
    c, d, f = eqs[1]
    det = a*d - b*c
    return -(d*e - b*f)/det, -(a*f - c*e)/det

def solve_hard(stones):
    eqs = map(stone_to_eq, stones[:5])
    arr = numpy.array([e[:-1] for e in eqs])
    _, _, vx, vy, _ = [int(round(r)) for r in numpy.linalg.solve(arr, [-e[-1] for e in eqs])]
    eqs = map(stone_to_eq_yz, stones[:5])
    arr = numpy.array([e[:-1] for e in eqs])
    _, _, vy2, vz, _ = [int(round(r)) for r in numpy.linalg.solve(arr, [-e[-1] for e in eqs])]
    assert vy2 == vy
    v = (vx, vy, vz)
    eqs = [stone_to_eq_with_v(s, v) for s in stones[:2]]
    px, py = solve2(eqs)
    eqs = [stone_to_eq_yz_with_v(s, v) for s in stones[:2]]
    py2, pz = solve2(eqs)
    assert py2 == py
    return px + py + pz

assert solve_hard(stones) == 600352360036779
    
    
