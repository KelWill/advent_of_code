
real = open('./day14.input').read()
ex = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


def roll_row(row):
    row = ''.join(row)
    return "#".join('O' * r.count('O') + '.' * r.count('.')
                    for r in row.split("#"))


def reverse_row_directions(rows):
    return ["".join([x for x in reversed(row)]) for row in rows]


def transpose(rows):
    return [*zip(*rows)]


def roll_dir(rows, dir):
    if dir == "N" or dir == "S":
        rows = transpose(rows)
    if dir == "S" or dir == "E":
        rows = reverse_row_directions(rows)
    rows = [roll_row(row) for row in rows]
    if dir == "S" or dir == "E":
        rows = reverse_row_directions(rows)
    if dir == "N" or dir == "S":
        rows = transpose(rows)
    return rows


def get_key(rows):
    return "".join([c for r in rows for c in r])


def roll_for_cycles(rows, n):
    seen = {}
    r = 0
    bumped = False
    while r < n:
        for dir in ["N", "W", "S", "E"]:
            rows = roll_dir(rows, dir)
        key = get_key(rows)
        if key in seen and not bumped:
            cycle_length = r - seen[key]
            r += ((n - r - cycle_length) // cycle_length) * cycle_length
            bumped = True
        seen[key] = r
        r += 1

    return rows


def get_north_load(rows):
    load = 0
    for i, row in enumerate(rows):
        scale = len(rows) - 1 - i
        load += scale * sum(x == "O" for x in row)
    return load


def main(s):
    rows = s.split("\n")
    rows = ['#' * len(rows[0])] + rows + ['#' * len(rows[0])]
    rows = ['#' + row + '#' for row in rows]
    part1_rows = roll_dir(tuple(rows), "N")

    return get_north_load(part1_rows), get_north_load(roll_for_cycles(rows, 1000000000))


print("ex:", main(ex))
print("real:", main(real))
