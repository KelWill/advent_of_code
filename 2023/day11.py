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


def main(s, scale=2):
    rows = s.split("\n")
    empty_row_count = []
    for r, row in enumerate(rows):
        empty_row_count.append((len(set(row)) == 1) *
                               (scale - 1) + (empty_row_count[-1] if r else 0))
    empty_col_count = []
    for c, col in enumerate(zip(*rows)):
        empty_col_count.append((len(set(col)) == 1) *
                               (scale - 1) + empty_col_count[-1] if c else 0)

    G = set()
    for r, row in enumerate(rows):
        for c in range(len(row)):
            if row[c] == "#":
                G.add((r + empty_row_count[r], c + empty_col_count[c]))

    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(G, 2))


print("ex:", main(ex), main(ex, 100))
input = open("day11.input").read()
print("real:", main(input), main(input, 1000000))
