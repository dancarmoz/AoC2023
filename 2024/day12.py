text = open('input_day12.txt').read()
lines = text.splitlines()
# ns = map(int, lines[0].split())
m, n = len(lines), len(lines[0])

IS_DONE = [[0]*n for i in xrange(m)]

def check_val(ii, jj, val):
    return (0 <= ii < m and 0 <= jj < n and lines[ii][jj] == val)

def get_region_pt1(i, j):
    if IS_DONE[i][j]: return 0
    val = lines[i][j]
    queue = [(i,j)]
    IS_DONE[i][j] = 1
    area, perim = 0, 0
    while queue:
        i, j = queue.pop()
        area += 1
        for ii, jj in [(i+1, j),(i-1,j),(i, j+1), (i, j-1)]:
                if not check_val(ii, jj, val):
                        perim += 1
                        continue
                if not IS_DONE[ii][jj]:
                        queue.append((ii,jj))
                        IS_DONE[ii][jj] = 1
    return area*perim 

def solve_day12_pt1():
    global IS_DONE
    IS_DONE = [[0]*n for i in xrange(m)]
    return sum([get_region_pt1(i,j) for i in xrange(m) for j in xrange(n)])

'''
To find the number of sides of the perimeter, we instead count the number of vertices in it
(they are equal, as in any linear boundary). To identify corners, for every plot in the region
we consider the four 2x2 squares that contain it (whose centers are each of the plot's corners).
For each such square, we can identify whether the matching corner is a vertex of the region or not
by the pattern of its four surrounding plots. If X denotes the gardent's type and . denotes
any other type (inclding out of bounds), then we have the following rules:

X.  .X  ..  ..   
..  ..  X.  .X      -> The corner is a vertex

XX  X.  ..  .X  XX   
..  X.  XX  .X  XX  -> The corner is a not a vertex

XX  X.  .X  XX   
X.  XX  XX  .X      -> The corner is a vertex; but, it is counted 3 times (once for each X).
Therefore, we should count it as 1/3 of a vertex for each X, so that it sums to 1.

X.  .X
.X  X.  -> The most interesting case: the corner is actually 2 vertices! It is a different
vertex for each of its Xs. This is true both in the case that the two Xs belong are part of
the same region (and the center contribute 2 vertices to the region) or part of two different
regions (and the center contributes 1 vertex to each of the regions). Thus it is always correct
to count it as 1 perimeter vertex, for each X (and 2 total).

The dict below encapsulates the data above, where X is replaced with 1 and . with 0, and the
square is flattened into a 4-tuple.
'''
count_corners = {
    (0,0,0,1) : 1,
    (0,0,1,0) : 1,
    (0,1,0,0) : 1,
    (1,0,0,0) : 1,
    (0,0,1,1) : 0,
    (1,1,0,0) : 0,
    (1,0,1,0) : 0,
    (0,1,0,1) : 0,
    (1,1,1,1) : 0,
    (1,1,1,0) : 1/3.,
    (1,1,0,1) : 1/3.,
    (1,0,1,1) : 1/3.,
    (0,1,1,1) : 1/3.,
    (0,1,1,0) : 1,
    (1,0,0,1) : 1,
}

def get_region_pt2(i,j):
	if IS_DONE[i][j]: return 0
	val = lines[i][j]
	queue = [(i,j)]
	IS_DONE[i][j] = 1
	area, perim = 0, 0
	while queue:
		i, j = queue.pop()
		area += 1
		for ik in xrange(i-1, i+1):
			for jk in xrange(j-1, j+1):
				shape = tuple(
                                    [int(check_val(ii, jj, val)) \
                                         for ii in range(ik,ik+2) for jj in range(jk, jk+2)])
				perim += count_corners[shape]
		for ii, jj in [(i+1, j),(i-1,j),(i, j+1), (i, j-1)]:
			if not check_val(ii, jj, val): continue
			if not IS_DONE[ii][jj]:
				queue.append((ii,jj))
				IS_DONE[ii][jj] = 1
	perim = int(round(perim))
	return area*perim

def solve_day12_pt2():
    global IS_DONE
    IS_DONE = [[0]*n for i in xrange(m)]
    return sum([get_region_pt2(i,j) for i in xrange(m) for j in xrange(n)])
