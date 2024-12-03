text = open('input_day04.txt').read()
lines = text.splitlines()
cards = [[set(map(int, x.split())) for x in l.split(': ')[1].split(' | ')] for l in lines]

def solve_easy(cards):
    return sum(2**(n-1) if n else 0 for n in [len(a&b) for a,b in cards])

assert solve_easy(cards) == 26443

def solve_hard(cards):
    lens = [len(a&b) for a,b in cards]
    n_cards = [1]*len(lens)
    for i in range(len(cards)):
        for j in xrange(i+1, i + lens[i]+1):
            n_cards[j] += n_cards[i]
    return sum(n_cards)

assert solve_hard(cards) == 6284877
