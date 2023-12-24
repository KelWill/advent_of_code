from collections import defaultdict
from pprint import pprint


ex = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""
real = open("./day23.input").read()

SLOPES = {
    ">": 1j,
    "<": -1j,
    "v": 1,
    "^": -1,
}


def main(s):
    rows = s.split("\n")
    board = {r + c * 1j: rows[r][c]
             for r in range(len(rows)) for c in range(len(rows[0])) if rows[r][c] != "#"}

    start = rows[0].index(".") * 1j
    end = len(rows) - 1 + rows[-1].index(".") * 1j

    part1 = 0
    todo = [(start, set())]
    while todo:
        curr, visited = todo.pop()
        if curr == end:
            part1 = max(part1, len(visited))
            continue
        for d in (1, -1, 1j, -1j):
            if curr + d not in board:
                continue
            if curr + d in visited:
                continue
            if board[curr] in SLOPES and d != SLOPES[board[curr]]:
                continue
            todo.append((curr + d, visited | set([curr + d])))

    junctions = set([start, end])
    for b in board:
        if sum(b + d in board for d in (1, -1, 1j, -1j)) > 2:
            junctions.add(b)

    graph = defaultdict(list)

    def find_links(j):
        todo = [(j, set([j]))]
        while todo:
            curr, seen = todo.pop()
            if curr != j and curr in junctions:
                graph[j].append((curr, len(seen) - 1))
                continue
            for d in [d for d in (1, -1, 1j, -1j) if curr + d in board and not curr + d in seen]:
                todo.append((curr + d, seen | set([curr + d])))

    for j in junctions:
        find_links(j)

    part2 = 0
    todo = [(start, set([start]), 0)]
    while todo:
        curr, seen, l = todo.pop()
        if curr == end:
            part2 = max(l, part2)
            continue
        for n, l2 in graph[curr]:
            if n in seen:
                continue
            todo.append((n, seen | {n}, l + l2))

    return part1, part2


print("ex", main(ex))
print("real", main(real))
