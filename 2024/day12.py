from collections import defaultdict

ex = open("./day12.ex").read().strip()
real = open("./day12.input").read().strip()

def visit(G, pos):
    directions = (1, -1, 1j, -1j)
    seen = set()
    edge = 0
    c = G[pos]
    todo = [pos]
    seen.add(pos)
    while todo:
        pos = todo.pop()
        neighbors = [pos + d for d in directions]
        edge += sum(G[n] != c for n in neighbors)
        to_add = [n for n in neighbors if G[n] == c and not n in seen]
        seen |= set(to_add)
        todo += to_add

    sides = 0
    for p in seen:
        upper_right_corner = all(G[p + d] != c for d in (1j, 1))
        upper_left_corner = all(G[p + d] != c for d in (1j, -1))
        lower_left_corner = all(G[p + d] != c for d in (-1j, -1))
        lower_right_corner = all(G[p + d] != c for d in (-1j, 1))

        inner_upper_right_corner = (
            G[p + 1 + 1j] != c and G[p + 1] == c and G[p + 1j] == c
        )
        inner_bottom_right_corner = (
            G[p + 1 - 1j] != c and G[p + 1] == c and G[p - 1j] == c
        )
        inner_bottom_left_corner = (
            G[p - 1 - 1j] != c and G[p - 1] == c and G[p - 1j] == c
        )
        inner_upper_left_corner = (
            G[p - 1 + 1j] != c and G[p - 1] == c and G[p + 1j] == c
        )

        sides += (
            upper_right_corner
            + upper_left_corner
            + lower_left_corner
            + lower_right_corner
            + inner_upper_right_corner
            + inner_bottom_right_corner
            + inner_bottom_left_corner
            + inner_upper_left_corner
        )

    return seen, edge, sides


def main(s):
    lines = s.split("\n")
    G = defaultdict(str) | {
        r + c * 1j: char for r, row in enumerate(lines) for c, char in enumerate(row)
    }
    seen = set()
    positions = [*G.keys()]
    p1 = 0
    p2 = 0
    for pos in positions:
        if pos in seen:
            continue
        plot_seen, edge, sides = visit(G, pos)
        p1 += len(plot_seen) * edge
        p2 += len(plot_seen) * sides
        seen |= plot_seen
    return p1, p2


print(main(ex))
print(main(real))
