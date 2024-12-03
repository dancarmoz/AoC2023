text = open('input_day03.txt').read()

import re

muls = re.findall('mul\([1-9][0-9]?[0-9]?,[1-9][0-9]?[0-9]?\)', text)

def solve_day03_pt1():
    return sum([x*y for x,y in [map(int, s[4:-1].split(',')) for s in muls]])

def solve_day03_pt2():
    # using text.index only works if each mul instruction is unique
    assert len(set(muls)) = len(muls)
    indices = [text.index(m) for m in muls]
    act = [1]*len(text)
    state = 1
    for i in range(len(text)):
        if text[i:i+4] == 'do()':
            state = 1
        elif text[i:i+7] == "don't()":
            state = 0
        act[i] = state
    acmuls = [m for i,m in zip(indices, muls) if act[i]]
    return sum([x*y for x,y in [map(int, s[4:-1].split(',')) for s in acmuls]])
