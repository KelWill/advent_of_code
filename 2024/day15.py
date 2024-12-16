from collections import defaultdict
real = open("./day15.input").read()
ex = open("./day15.example").read()

small_ex = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

def main (s):
    s = s.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")

    map_string, moves = s.split("\n\n")
    moves = moves.replace("\n", "")
    move_map = {
        "^": -1j,
        "v": 1j,
        ">": 1,
        "<": -1,
    }

    M = defaultdict(str) | { r * 1j + c: char for r, row in enumerate(map_string.split("\n")) for c, char in enumerate(row) if char != "." }
    R = max(int(p.imag) for p in M.keys())
    C = max(int(p.real) for p in M.keys())
    pos = next(k for k, v in M.items() if v == "@")
    for m in moves:
        d = move_map[m]
        if M[pos + d] == "#":
            continue
        if not M[pos + d]:
            del M[pos]
            pos += d
            M[pos] = "@"
            continue

        if d.real:
            above = []
            curr = pos + d
            while M[curr] in "[]" and M[curr]:
                above.append(curr)
                curr += d         
            if M[curr] == "#":
                continue
        else:
            above = []
            if M[pos + d] == "[":   
                above = push_box(M, [pos + d, pos + d + 1], d)
            elif M[pos + d == "]"]:
                above = push_box(M, [pos + d, pos + d - 1], d)
            else:
                raise Exception("huh?")
            if not above:
                continue

        for a in reversed(above):
            if not M[a]:
                continue
            if M[a + d]:
                print(f"trying to move {a} ({M[a]}) to {a + d} ({M[a + d]})")
                raise Exception("unable to move")
            M[a + d] = M[a]
            del M[a]

        del M[pos]
        pos += d
        M[pos] = "@"

    return sum(p.imag * 100 + p.real for p, v in M.items() if v == "[")

def push_box (M, boxes, d):
    result = []
    while boxes:
        b = boxes.pop(0)
        if b in result:
            continue
        result.append(b)
        p = b + d
        if M[p] == "#":
            return []
        if M[p] == "[":
            boxes.append(p)
            boxes.append(p + 1)
        if M[p] == "]":
            boxes.append(p)
            boxes.append(p - 1)

    return result
            

print(main(ex))
print(main(real))
