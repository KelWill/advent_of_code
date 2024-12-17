from collections import defaultdict
import heapq
import math
import random


ex = open("./day16.example").read()
real = open("./day16.input").read()

def main (s):
    maze = defaultdict(lambda: "#") | { r * 1j + c: char for r, row in enumerate(s.split("\n")) for c, char in enumerate(row) }
    start = next(pos for pos, char in maze.items() if char == "S")
    end = next(pos for pos, char in maze.items() if char == "E")

    rotate = [1j, -1j]
    scores = {}

    todos = [(0, 0, start, 1)]
    p1 = math.inf
    while todos:
        s, _r, pos, d = heapq.heappop(todos)
        if s > p1:
            continue
        if pos == end:
            p1 = min(p1, s)
            continue
        if (pos, d) in scores and scores[(pos, d)] < s:
            continue
        for r in rotate:
            dd = d * r
            ss = s + 1000
            if (pos, dd) in scores and scores[(pos, dd)] < ss:
                continue
            heapq.heappush(todos, (ss, random.random(), pos, dd))
            scores[(pos, dd)] = ss
        if maze[pos + d] == "#":
            continue
        heapq.heappush(todos, (s + 1, random.random(), pos + d, d))
        if (pos, d) not in scores:
            scores[(pos, d)] = s
        scores[(pos, d)] = min(scores[(pos, d)], s)

    todos = [(0, 0, start, 1, [0])]
    p2 = set()
    while todos:
        s, _r, pos, d, path = heapq.heappop(todos)
        if s > p1:
            continue
        if pos == end:
            p2 |= set(path)
            continue
        if (pos, d) in scores and scores[(pos, d)] < s:
            continue

        for r in rotate:
            dd = d * r
            ss = s + 1000
            if (pos, dd) in scores and scores[(pos, dd)] < ss:
                continue
            heapq.heappush(todos, (ss, random.random(), pos, dd, path))
            scores[(pos, dd)] = ss
        if maze[pos + d] == "#":
            continue
        heapq.heappush(todos, (s + 1, random.random(), pos + d, d, path + [pos + d]))
        if (pos, d) not in scores:
            scores[(pos, d)] = s
        scores[(pos, d)] = min(scores[(pos, d)], s)

    return p1, len(p2)


print(main(ex))
print(main(real))
        

