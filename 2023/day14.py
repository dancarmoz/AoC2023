text = open('input_day14.txt').read()
lines = text.splitlines()

def trans_strs(mat):
    return map(''.join, zip(*mat))

def score_line(line):
    res = 0
    score = n = len(line)
    for i, s in enumerate(line):
        if s == '#': score = n - i - 1
        elif s == 'O':
            res += score
            score -= 1
    return res

def solve_easy(lines):
    return sum(map(score_line, trans_strs(lines)))

assert solve_easy(lines) == 106378

def tilt_line(line):
    line = line + '#'
    res = ''
    n = len(line)
    for i, s in enumerate(line):
        if s == '#': res += '.' * (i-len(res)) + '#'
        elif s == 'O': res += 'O'
    return res[:-1]

def full_tilt(lines):
    lines = trans_strs(map(tilt_line, trans_strs(lines)))
    lines = map(tilt_line, lines)
    lines = trans_strs([tilt_line(l[::-1])[::-1] for l in trans_strs(lines)])
    lines = [tilt_line(l[::-1])[::-1] for l in lines]
    return lines

def solve_hard(lines, n):
    all_lines = [lines]
    lines_set = set(''.join(lines))
    while True:
        lines = full_tilt(lines)
        jj = ''.join(lines)
        if jj in lines_set:
            cycle_start = all_lines.index(lines)
            cycle_len = len(all_lines) - cycle_start
            break
        all_lines.append(lines)
        lines_set.add(jj)
    final = all_lines[(n-cycle_start) % cycle_len + cycle_start]
    return sum((i+1)*l.count('O') for i, l in enumerate(final[::-1]))

assert solve_hard(lines, 1000000000) == 90795
