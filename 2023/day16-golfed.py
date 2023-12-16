def count_energized(positions, start):
    seen = set()
    beams = [start]
    while beams:
        next_beams = []
        for p, v in beams:
            if (p, v) in seen or p not in positions:
                continue
            seen.add((p, v))
            match positions[p]:
                case "|" if v.imag:
                    next_beams += [(p, 1), (p, -1)]
                case "-" if v.real:
                    next_beams += [(p, 1j), (p, -1j)]
                case "\\":
                    next_beams.append((p, complex(v.imag, v.real)))
                case "/":
                    next_beams.append((p, -complex(v.imag, v.real)))
                case _:
                    next_beams.append((p, v))
        beams = [(p + v, v)
                 for p, v in next_beams]

    return len(set(p for p, v in seen))


def main(s):
    rows = s.split("\n")
    positions = {r + c * 1j: char for r,
                 row in enumerate(rows) for c, char in enumerate(row)}
    starts = [(r + c * 1j, v) for r in range(len(rows))
              for c, v in [(0, 1j), (len(rows[0]) - 1, -1j)]] + [(r + c * 1j, v) for c in range(len(rows[0])) for r, v in [(0, 1), (len(rows) - 1, -1)]]
    max_energized = max(count_energized(positions, start) for start in starts)
    return count_energized(positions, (0, 1j)), max_energized


print(main(open("./day16.input").read()))
