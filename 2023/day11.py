from itertools import combinations


ex = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


def calc_dists(rows, scale):
    row_dist = []
    for r, row in enumerate(rows):
        row_dist.append((scale if len(set(row)) == 1 else 1) +
                        (row_dist[-1] if r else 0))
    return row_dist


def main(s, scale=2):
    rows = s.split("\n")
    row_dist = calc_dists(rows, scale)
    col_dist = calc_dists(list(zip(*rows)), scale)
    G = set((row_dist[r], col_dist[c])
            for r in range(len(rows)) for c in range(len(rows[r])) if rows[r][c] == "#")
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(G, 2))


print("ex:", main(ex), main(ex, 100))
input = open("day11.input").read()
print("real:", main(input), main(input, 1000000))
