text = open('input_day02.txt').read()
lines = text.splitlines()
nums = [map(int,x.split()) for x in lines]

def sgn(x):
    if x > 0: return 1
    if x < 0: return -1
    return 0

def is_safe(nums):
    diffs = [y-x for x,y in zip(nums[:-1],nums[1:])]
    return len(set(map(sgn, diffs))) == 1 and len(set(map(abs,diffs))-{1,2,3}) == 0

def is_safe2(line):
    return any(map(is_safe, [line] + [line[:i]+line[i+1:] for i in range(len(line))]))

def solve_day02_pt1():
    return sum(map(is_safe,nums))

def solve_day02_pt2():
    return sum(map(is_safe2,nums))
