text = open('input_day09.txt').read()
lines = text.splitlines()
ns = map(int, lines[0])
if len(ns) % 2 == 1: ns += [0]

# runs in ~11.5s
def solve_day09_pt1_orig():
    arr = []
    for i in xrange(0,len(ns),2):
        arr += [i/2]*ns[i] + [-1]*ns[i+1]
    for j in range(len(arr)-1,-1,-1):
        val = arr[j]
        if val == -1: continue
        arr[j] = -1
        arr[arr.index(-1)] = val
    return sum(j*arr[j] for j in range(len(arr)) if arr[j] != -1)

# runs in ~17ms
def solve_day09_pt1():
    arr = []
    for i in xrange(0,len(ns),2):
        arr += [i/2]*ns[i] + [-1]*ns[i+1]
    i = 0
    for j in range(len(arr)-1,-1,-1):
        val = arr[j]
        if val == -1: continue
        arr[j] = -1
        while arr[i] != -1:
            i += 1
        arr[i] = val
        if i == j: break
    return sum(j*arr[j] for j in range(len(arr)) if arr[j] != -1)

# runs in ~1.3s
def solve_day09_pt2_orig():
    blocks, gaps, count = [], [], 0
    for i in xrange(0,len(ns),2):
        blocks.append([count, ns[i], i/2])
        gaps.append([count+ns[i], ns[i+1]])
        count += ns[i]+ns[i+1]
    for j in range(len(blocks)-1,-1,-1):
        for i in range(j):
            if gaps[i][1] >= blocks[j][1]:
                blocks[j][0] = gaps[i][0]
                gaps[i][0] += blocks[j][1]
                gaps[i][1] -= blocks[j][1]
                break
    return sum([z * y * (2*x+y-1) / 2 for x,y,z in blocks])

import heapq
# runs in ~45ms
def solve_day09_pt2():
    blocks, gaps, count = [], [[] for g in range(10)], 0
    for i in xrange(0,len(ns),2):
        blocks.append([count, ns[i], i/2])
        gaps[ns[i+1]].append(count+ns[i])
        count += ns[i]+ns[i+1]
    for i in xrange(1,10):
        heapq.heapify(gaps[i])
    for j in range(len(blocks)-1,-1,-1):
        s, g = min([(10*len(ns),10)] + [(gaps[g][0], g) for g in xrange(blocks[j][1],10) if gaps[g]])
        if s > blocks[j][0]: continue
        blocks[j][0] = s
        heapq.heappop(gaps[g])
        blen = blocks[j][1]
        if g > blen:
            heapq.heappush(gaps[g - blen], s + blen)
    return sum([z * y * (2*x+y-1) / 2 for x,y,z in blocks])
