from collections import defaultdict

text = open('input_day25.txt').read()
lines = text.splitlines()

graph = defaultdict(list)
for l in lines:
    s, o = l.split(': ')
    for z in o.split():
        graph[s].append(z)
        graph[z].append(s)

def solve_min_cut(graph):
    nodes = graph.keys()
    V = set(nodes[:1])
    W = set(nodes[1:])
    while len(W):
        counts = [(sum(v in V for v in graph[u]), u) for u in W]
        if sum([c for c,u in counts]) <= 3:
            return len(V)*len(W)
        u = max(counts)[1]
        V.add(u)
        W.remove(u)
    return []

assert solve_min_cut(graph) == 589036
