
ex = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


def reflects(graph, reflection_row, smudge_count=0):
    equal_rows = zip(range(reflection_row, -1, -1),
                     range(reflection_row + 1, len(graph)))

    diff_count = 0
    for a, b in equal_rows:
        for c, d in zip(graph[a], graph[b]):
            if c != d:
                diff_count += 1

    return diff_count == smudge_count


def main(s, smudge_count=0):
    total = 0
    for x in s.split("\n\n"):
        rows = x.split("\n")
        cols = tuple(zip(*rows))
        for r in range(0, len(rows) - 1):
            if reflects(rows, r, smudge_count):
                total += 100 * (r + 1)
                break
        for c in range(0, len(cols) - 1):
            if reflects(cols, c, smudge_count):
                total += c + 1
                break

    return total


print("ex:", main(ex), main(ex, 1))
print("real:", main(open("./day13.input").read()),
      main(open("./day13.input").read(), 1))
