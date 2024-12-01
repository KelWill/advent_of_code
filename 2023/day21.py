ex = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


def part1(s, n):
    rows = s.split("\n")
    plots = {r + c * 1j: row[c] for r, row in enumerate(rows)
             for c in range(len(row)) if row[c] != "#"}
    start = next(pos for pos in plots if plots[pos] == "S")

    endable = set()
    seen = set([start])
    todo = [start]
    for r in range(n):
        nxt = []
        for pos in todo:
            if (n - r) % 2 == 0:
                endable.add(pos)
            for d in (-1, 1, 1j, -1j):
                if pos + d in seen or pos + d not in plots:
                    continue
                nxt.append(pos + d)
                seen.add(pos + d)
        todo = nxt
    return len(endable | set(todo))


def part2(s, n):
    rows = s.split("\n")
    plots = {r + c * 1j: row[c] for r, row in enumerate(rows)
             for c in range(len(row)) if row[c] != "#"}
    start = next(pos for pos in plots if plots[pos] == "S")

    edge = set()
    for r in range(len(rows)):
        for c in range((len(rows[r]))):
            if r == 0 or r == len(rows) - 1 or c == 0 or c == len(rows[r]) - 1:
                edge.add(r + c * 1j)

    seen = set([start])
    todo = [start]
    odds = set()
    edge_reach_counts = {}
    for r in range(n):
        nxt = []
        for pos in todo:
            if (n - r) % 2:
                odds.add(pos)
            for d in (-1, 1, 1j, -1j):
                if pos + d in edge and not pos + d in edge_reach_counts:
                    edge_reach_counts[pos + d] = r
                if pos + d in seen or pos + d not in plots:
                    continue
                nxt.append(pos + d)
                seen.add(pos + d)
        todo = nxt
    print(edge_reach_counts)


print("ex", part1(ex, 6))
print("ex part 2", part2(ex, 128))
# print("real", part1(open("./day21.input").read(), 64))
