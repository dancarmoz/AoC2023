text = open('input_day08.txt').read()
lines = text.splitlines()
m, n = len(lines), len(lines[0])
M = max(m,n)

import itertools as it

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solve_day08_pt1():
    isanti = [[0]*n for i in xrange(m)]
    for i,j in it.product(range(m), range(n)):
        for ii,jj in it.product(range(m), range(n)):
            if lines[i][j] == lines[ii][jj] != '.' and (i,j) != (ii,jj):
                k,l = 2*i-ii, 2*j - jj
                if (0 <= k < m) and (0 <= l < n):
                    isanti[k][l] = 1
    return sum(map(sum,isanti))

def solve_day08_pt2():
    isanti = [[0]*n for i in xrange(m)]
    for i,j in it.product(range(m), range(n)):
        for ii,jj in it.product(range(m), range(n)):
            if lines[i][j] == lines[ii][jj] != '.' and (i,j) != (ii,jj):
                di,dj = i - ii, j - jj
                d = gcd(abs(di), abs(dj))
                for h in range(-M, M+1):
                    k, l = i + h * di/d, j + h * dj/d
                    if (0 <= k < m) and (0 <= l < n):
                        isanti[k][l] = 1
    return sum(map(sum,isanti))
