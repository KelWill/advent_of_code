from collections import defaultdict

def dp (graph, seen=set(), party=tuple()):
    parties = []
    nodes_to_check = set(graph[party[0]]) if party else set(graph.keys())
    for p in party:
        nodes_to_check &= graph[p]
    for g in nodes_to_check:
        pp = key(party + (g,))
        if pp in seen:
            continue
        seen.add(pp)
        if g in party:
            continue
        if any(g not in graph[p] for p in party):
            continue
        parties += dp(graph, seen, pp)
    return parties or [party]
    

def key (l):
    return tuple(sorted(l))

def main (s):
    graph = defaultdict(set)
    links = set()
    for row in s.split("\n"):
        a, b = row.split("-")
        graph[a].add(b)
        graph[b].add(a)
        links.add(tuple(sorted((a, b))))
    
    trios = set()
    for a, b in links:
        cs = graph[a] & graph[b]
        for c in cs:
            trios.add(key((a, b, c)))
    
    p1 = 0
    for t in trios:
        p1 += any(comp.startswith("t") for comp in t)


    parties = dp(graph, set(), tuple())
    max_len = 0
    for p in parties:
        max_len = max(max_len, len(p))
    best_party = next(p for p in parties if len(p) == max_len)


    return p1, ",".join(best_party)


print(main(open("./day23.example").read()))
print(main(open("./day23.input").read()))


