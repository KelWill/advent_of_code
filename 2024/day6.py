from collections import defaultdict

input = open(0).read().split("\n")

starting_map = defaultdict(str) | { y + x * 1j: input[y][x] for x in range(len(input[0])) for y in range(len(input))}
starting_pos = next(pos for pos, v in starting_map.items() if v == "^")

def p1 ():
    p1_map = defaultdict(str) | starting_map
    pos = starting_pos
    dir = -1
    while p1_map[pos]:
        p1_map[pos] = "X"
        if p1_map[pos + dir] == "#":
            dir *= -1j
        else:
            pos += dir

    return p1_map

def has_loop (m):
    pos = starting_pos
    dir = -1
    seen = set()
    while m[pos]:
        if (pos, dir) in seen:
            return True
        seen.add((pos, dir))
        if m[pos + dir] == "#":
            dir *= -1j
        else: pos += dir
    return False

def p2 ():
    m = p1()
    return sum(has_loop(m | { k: "#" }) for k in [key for key, v in m.items() if v == "X" if key != starting_pos])


print(sum(v == "X" for v in p1().values()))
print(p2())

