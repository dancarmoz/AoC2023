text = open('input_day03.txt').read()
lines = text.splitlines()

def solve_both(lines):
    m, n = len(lines), len(lines[0])
    ij_to_num = {}
    sum_good = 0
    stars = []
    for i in xrange(m):
        j = 0
        while j < n:
            if lines[i][j] not in '1234567890':
                if lines[i][j] == '*':
                    stars.append((i, j))
                j+=1
                continue
            j0 = j
            while j<140 and lines[i][j] in '1234567890':
                j+=1
            j1 = j
            num = int(lines[i][j0:j1])
            is_good = False
            for ii in xrange(max(i-1, 0), min(i+2, m)):
                for jj in range(max(j0-1, 0), min(j1+1, n)):
                    if lines[ii][jj] not in '1234567890.':
                        is_good = True
            if is_good:
                sum_good += num
            for jj in xrange(j0, j1):
                ij_to_num[i,jj] = (i,j0,j1,num)
    sum_gears = 0
    for i,j in stars:
        sn = set([ij_to_num[ii,jj] for ii in range(i-1, i+2) for jj in range(j-1, j+2)
                  if (ii, jj) in ij_to_num])
        if len(sn) != 2: continue
        a, b = sn
        sum_gears += a[3] * b[3]
    return sum_good, sum_gears

assert solve_both(lines) == (522726, 81721933)
        
            
