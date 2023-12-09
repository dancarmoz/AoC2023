text = open('input_day02.txt').read()

def parse_gameline(line):
    rounds = line.split(': ')[1].split('; ')
    return [[x.split() for x in r.split(', ')] for r in rounds]

games = [parse_gameline(line) for line in text.splitlines()]

def get_max_game(game):
    d = {'red': 0, 'green': 0, 'blue': 0}
    for g in game:
        for (n,c) in g:
            n = int(n)
            d[c] = max(d[c], n)
    return d

def solve_easy(games):
    ds = map(get_max_game, games)
    return sum([i+1 for i, d in enumerate(ds) if \
                d['red'] <= 12 and d['green'] <= 13 and d['blue'] <= 14])

assert solve_easy(games) == 2268

def solve_hard(games):
    ds = map(get_max_game, games)
    return sum([d['red']*d['green']*d['blue'] for d in ds])

assert solve_hard(games) == 63542
