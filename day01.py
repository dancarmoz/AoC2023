text = open('input_day01.txt').read()


def solve_easy(text):
    strip = 'abcdefghijklmnopqrstuvwxyz'
    for s in strip:
        text = text.replace(s, '')
    return sum([int(x[0] + x[-1]) for x in text.splitlines()])

assert solve_easy(text) == 53386

def solve_hard(text):
    nums = zip([
        'zero','one','two','three','four','five','six','seven','eight','nine'
    ], range(10))
    for s, d in nums:
        text = text.replace(s, s+str(d)+s)
    return solve_easy(text)

assert solve_hard(text) == 53312
