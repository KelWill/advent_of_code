from collections import defaultdict
real = open("./day10.input").read()

ex = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""


def main (s):
    G = defaultdict(lambda: -1) | {r + c * 1j: int(char) for r, row in enumerate(s.split("\n")) for c, char in enumerate(row) }
    p1 = set()
    p2 = 0
    todo = [(p, p) for p, e in G.items() if e == 0]
    while todo:
        p, start = todo.pop()
        e = G[p]
        if e == 9:
            p2 += 1
            p1.add((start, p))
        for d in (-1, 1, 1j, -1j):
            if G[p + d] == e + 1:
                todo.append((p + d, start))

    return len(p1), p2

print(main(ex), main(real))