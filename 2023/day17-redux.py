from heapq import heappop, heappush


def main(s):
    tiebreaker = 0
    ll = s.split("\n")
    positions = {(r + c * 1j): int(ll[r][c])
                 for r in range(len(ll)) for c in range(len(ll[r]))}
    todo = [(0, 0, 0, 1), (0, 0, 0, 1j)]
    seen = set()

    # trick to grab the largest position (because dictionaries preserves insertion order)
    end = [*positions][-1]

    while todo:
        cost, _, pos, prev_dir = heappop(todo)
        if pos == end:
            return cost
        if (pos, prev_dir) in seen:
            continue
        seen.add((pos, prev_dir))
        dirs = [1j * prev_dir, -1j * prev_dir]
        for v in dirs:
            c = cost
            p = pos
            for _dist in range(0, 3):
                p += v
                if not p in positions:
                    break
                c += positions[p]
                # tiebreaker does nothing other than allow heapq to compare two similar numbers
                # without trying to compare complex numbers (which causes it to error)
                tiebreaker += 1
                heappush(todo, (c, tiebreaker, p, v))
    raise Exception("no path to lower right")


print(main(open("./day17.input").read()))
