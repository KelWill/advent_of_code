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


def main(s):
    s = s.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")

    map_string, moves = s.split("\n\n")
    moves = moves.replace("\n", "")
    move_map = {
        "^": -1j,
        "v": 1j,
        ">": 1,
        "<": -1,
    }

    M = defaultdict(str) | {
        r * 1j + c: char
        for r, row in enumerate(map_string.split("\n"))
        for c, char in enumerate(row)
        if char != "."
    }
    pos = next(k for k, v in M.items() if v == "@")
    del M[pos]
    for m in moves:
        d = move_map[m]
        if M[pos + d] == "#":
            continue
        if not M[pos + d]:
            pos += d
            continue

        boxes = [pos + d]
        if d in (1j, -1j):
            boxes.append(pos + d + (1 if M[pos + d] == "[" else -1))
        above = push_box(M, boxes, d)
        if not above:
            continue

        for a in reversed(above):
            if M[a + d]:
                raise Exception("unable to move {a} ({M[a]}) to {a + d} ({M[a + d]}")
            M[a + d] = M[a]
            del M[a]
        pos += d

    return sum(p.imag * 100 + p.real for p, v in M.items() if v == "[")


def push_box(M, boxes, d):
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
            boxes += [p, p + 1]
        if M[p] == "]":
            boxes += [p, p - 1]

    return result


print(main(ex))
print(main(real))
