from collections import defaultdict
real = open("./day8.input").read()

ex = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def main (s):
    lines = s.split("\n")
    G = { r + c * 1j: lines[r][c] for r in range(len(lines)) for c in range(len(lines[r])) }
    
    points_by_type = defaultdict(list)
    for pos, c in G.items():
        if c == ".":
            continue
        points_by_type[c].append(pos)
    
    result = set()
    for positions in points_by_type.values():
        pairs = [(a, b) for a in positions for b in positions if a != b]
        for a, b in pairs:
            for v in (b - a, a - b):
                curr = a
                while curr in G:
                    result.add(curr)
                    curr += v

    return len(result)

print(main(ex))
print(main(real))

