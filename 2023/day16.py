ex = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""


def count_energized(positions, beams):
    seen = set()
    while beams:
        next_beams = []
        for beam in beams:
            p, v = beam
            if p not in positions or beam in seen:
                continue
            seen.add(beam)
            x = positions[p]
            if x == "." or (x == "|" and v.imag == 0) or (x == "-" and v.real == 0):
                next_beams.append((p, v))
            elif x == "|":
                next_beams += [(p, 1), (p, -1)]
            elif x == "-":
                next_beams += [(p, 1j), (p, -1j)]
            elif x == "\\":
                next_beams.append((p, v.imag if v.imag else v.real * 1j))
            elif x == "/":
                next_beams.append((p, v * 1j * [-1, 1][bool(v.imag)]))
            else:
                raise Exception("unknown")
        beams = [(p + v, v) for p, v in next_beams]

    return len(set(p for p, v in seen))


def main(s):
    rows = s.split("\n")

    positions = {}
    for r in range(len(rows)):
        for c, char in enumerate(rows[r]):
            positions[r + c * 1j] = char

    max_energized = 0
    for r in range(len(rows)):
        for c, v in [(0, 1j), (len(rows[0]) - 1, -1j)]:
            pos = r + c * 1j
            count = count_energized(positions, [(pos, v)])
            max_energized = max(max_energized, count)

    for c in range(len(rows[0])):
        for r, v in [(0, 1), (len(rows) - 1, -1)]:
            pos = r + c * 1j
            count = count_energized(positions, [(pos, v)])
            max_energized = max(max_energized, count)

    return count_energized(positions, [(0, 1j)]), max_energized


print(main(ex))
print(main(open("./day16.input").read()))
