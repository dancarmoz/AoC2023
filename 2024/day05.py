text = open('input_day05.txt').read()
ruless, pagess = text.split('\n\n')
rules, pages = ruless.splitlines(), pagess.splitlines()
pagen = [map(int, x.split(',')) for x in pages]
rulen = [map(int, x.split('|')) for x in rules]
ruleset = set(map(tuple, rulen))

def solve_day5_pt1_orig():
    good_pages = [g for g in pagen if not any(
        [(g[i],g[j]) in ruleset for i in xrange(1,len(g)) for j in xrange(i)])]
    return sum([g[len(g)/2] for g in good_pages])

# It turns out that for every pair of pages, exactly one of x|y or y|x is a rule.
# This is important for the correctness of the functions below.
npages = len(set(sum(pagen, [])))
assert len(ruleset) == npages * (npages - 1) / 2
# Also note there isn't one correct linear order of all possible pages,
# but rather an RPS-like relation between them.
from collections import Counter
assert npages % 2 == 1
assert Counter([x for x,y in rulen]).values() == [npages / 2]*npages

def solve_day5_pt1():
    good_pages = [g for g in pagen if not any(
        [(g[i],g[i-1]) in ruleset for i in xrange(1,len(g))])]
    return sum([g[len(g)/2] for g in good_pages])

def mycmp(x,y):
    if x == y: return 0
    if (x,y) in ss: return -1
    return 1

def solve_day5_pt2():
    bad_pages = [g for g in pagen if any(
        [(g[i],g[i-1]) in ruleset for i in xrange(1,len(g))])]
    bad_pages_sorted = [sorted(b, cmp=mycmp) for b in bad_pages]
    return sum([g[len(g)/2] for g in bad_pages_sorted])
