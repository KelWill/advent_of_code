
def parse_rock (s):
    points = set()
    for r, row in enumerate(reversed(s.split("\n"))):
        for c, char in enumerate(row):
            if char != "#":
                continue
            points.add((r, c))
    return points


rocks = [parse_rock(s) for s in """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split("\n\n")]

example_jets = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

def show_grid (grid, rock):
    max_r = max(r for r, _c in rock)

    for r in range(max_r, -1, -1):
        row = "|"
        for c in range(0, 7):
            if [r, c] in rock:
                row += "@"
                continue
            if r >= len(grid):
                row += "o"
                continue

            row += "-" if r == 0 else "." if not grid[r][c] else "#"
        row += "|"
        print(row)


def apply_jet (grid, rock, jet):
    can_jet = True
    for [r, c] in rock:
        if (not (0 <= c + jet < 7)) or (r < len(grid) and grid[r][c + jet]):
            can_jet = False
    if can_jet:
        for i in range(len(rock)):
            rock[i][1] += jet

def apply_down (grid, rock):
    can_go_down = True
    for [r, c] in rock:
        if r > len(grid):
            continue
        if not grid[r - 1]:
            continue
        if grid[r - 1][c]:
            can_go_down = False

    if not can_go_down:
        for [r, c] in rock:
            while len(grid) <= r: grid.append([False] * 7)
            grid[r][c] = True
        return True
    else:
        for i in range(len(rock)):
            rock[i][0] += -1
        return False

def tick (grid, rock, jet):
    apply_jet(grid, rock, jet)
    return apply_down(grid, rock)

def solve (jets):
    jet_i = 0
    def get_jet (jets):
        nonlocal jet_i
        jets = [(j == ">") - (j != ">") for j in jets]
        while True:
            yield jets[jet_i % len(jets)]
            jet_i += 1

    grid = [[True] * 7]
    jet_generator = get_jet(jets)
    seen = {}
    goal = 1000000000000
    i = 0
    height = 0
    while i < goal:
        prev_grid_len = len(grid)
        rock_shape = rocks[i % len(rocks)]
        rock = [[r + len(grid) + 3, c + 2] for (r, c) in rock_shape]
        while not tick(grid, rock, next(jet_generator)): pass

        top_heights = []
        for c in range(7):
            for r in range(len(grid) - 1, -1, -1):
                if grid[r][c]:
                    top_heights.append(len(grid) - r)
                    break
        key = tuple(top_heights + [jet_i % len(jets)])

        height += len(grid) - prev_grid_len

        if key in seen:
            ii, hh = seen[key]
            h = len(grid) - hh
            pattern_length = i - ii
            remaining = (goal - i) // pattern_length
            i += pattern_length * remaining
            height += h * remaining
            print("height", height)
        seen[key] = (i, len(grid))

        i += 1

    return height


jets = open("17.input").read()
print(solve(example_jets))
print(solve(jets))

