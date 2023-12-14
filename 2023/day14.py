
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
    result = [x for x in row]
    prev_solid_point = -1
    for r, char in enumerate(row):
        if char == "#":
            prev_solid_point = r
        elif char == "O" and prev_solid_point == r - 1:
            prev_solid_point = r
        elif char == "O":
            result[prev_solid_point + 1] = 'O'
            result[r] = '.'
            prev_solid_point += 1
    return "".join(result)


def reverse_row_directions(rows):
    return ["".join([x for x in reversed(row)]) for row in rows]


def transpose(rows):
    return [*zip(*rows)]


def roll_dir(rows, dir):
    if dir == "N" or dir == "S":
        rows = transpose(rows)
    if dir == "S" or dir == "E":
        rows = reverse_row_directions(rows)
    rows = tuple(roll_row(row) for row in rows)
    if dir == "S" or dir == "E":
        rows = reverse_row_directions(rows)
    if dir == "N" or dir == "S":
        rows = transpose(rows)
    return rows


def get_key(rows):
    return "".join([c for r in rows for c in r])


def roll_for_cycles(rows, n):
    seen = {}
    rows = tuple(rows)
    r = 0
    bumped = False
    while r < n:
        for dir in ["N", "W", "S", "E"]:
            rows = roll_dir(rows, dir)
        key = get_key(rows)
        if key in seen and not bumped:
            cycle_length = r - seen[key]
            # ...I should probably do math here
            while r < n - cycle_length:
                r += cycle_length
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
