from collections import Counter
text = open('input_day07.txt').read()

text_easy = text.replace('A', 'Z').replace('K','Y').replace('T','B')
hands_easy = [x.split() for x in text_easy.splitlines()]

def classify_easy(h):
    return tuple(sorted(Counter(h).values(), reverse=True))


def solve(text, classify):
    hands = [x.split() for x in text.splitlines()]
    def cmph(h0, h1):
        h0, h1 = h0[0], h1[0]
        c0, c1 = classify(h0), classify(h1)
        if c0 > c1: return 1
        if c1 > c0: return -1
        return cmp(h0, h1)
    
    hands_so = sorted(hands, cmp=cmph)
    return sum([(i+1)*int(y) for i,(x,y) in enumerate(hands_so)])

assert solve(text_easy, classify_easy) == 249204891

text_hard = text_easy.replace('J','!')

def classify_hard(h):
    if h == '!!!!!': return (5,)
    ls = sorted(Counter(h.replace('!','')).values(),reverse=True)
    ls[0] += h.count('!')
    return tuple(ls)

assert solve(text_hard, classify_hard) == 249666369
