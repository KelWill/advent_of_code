from collections import defaultdict

input = open(0).read().split("\n")

m = defaultdict(str) | { c + r * 1j: input[r][c] for c in range(len(input[0])) for r in range(len(input))}
pos = [pos for pos, v in m.items() if v == "^"][0]
dirs = [-1j, 1, 1j, -1]
diri = 0

while m[pos]:
    m[pos] = "X"
    dir = dirs[diri % 4]
    if m[pos + dir] == "#":
        diri += 1
    else:
        pos += dir

print(sum(v == "X" for v in m.values()))

starting_dict = defaultdict(str) | { c + r * 1j: input[r][c] for c in range(len(input[0])) for r in range(len(input))}

def has_loop (m):
    pos = [pos for pos, v in m.items() if v == "^"][0]
    dirs = [-1j, 1, 1j, -1]
    diri = 0
    seen = set()
    while m[pos]:
        m[pos] = "X"
        dir = dirs[diri % 4]
        if (pos, dir) in seen:
            return True
        seen.add((pos, dir))
        if m[pos + dir] == "#":
            diri += 1
        else:
            pos += dir
    return False

def brute_force ():
    keys =  [c + r * 1j for c in range(len(input[0])) for r in range(len(input))]
    loop_count = 0
    i = 0
    for k in keys:
        i += 1
        print(i, len(keys), i / len(keys) * 100)
        m = defaultdict(str) | { c + r * 1j: input[r][c] for c in range(len(input[0])) for r in range(len(input))}
        if m[k] != ".":
            continue
        m[k] = "#"
        loop_count += has_loop(m)
    return loop_count

print(brute_force())

