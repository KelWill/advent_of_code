ex = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

DIRS = {
    "U": -1,
    "D": 1,
    "L": -1j,
    "R": 1j
}


def extract_instruction(hex):
    last_digit = int(hex[-1])
    rest = hex[1:-1]
    return "RDLU"[last_digit], int(rest, base=16)


def is_valid_loop(points, check_same_directions=False):
    for a, b in zip(points, points[1:] + [points[0]]):
        if sum((a[0] == b[0], a[1] == b[1])) != 1:
            print(f"invalid loop: cannot move from {a} to {b}")
            return False
    directions = [(0 if a[0] == b[0] else 1 if a[0] > b[0] else -1, 0 if a[1] == b[1] else 1 if a[1] > b[1] else -1)
                  for a, b in zip(points, points[1:] + [points[0]])]
    if check_same_directions:
        for i in range(len(directions) - 2):
            if directions[i] == directions[i + 1] and directions[i] == directions[i + 2]:
                print(
                    f"invalid loop. Moving the same direction between {points[i:i + 3]}")
                return False
    return True


f = open("./day18.ouput", "w")


def print_loop(points):
    f = open("./day18.ouput", mode="a")

    if not is_valid_loop(points):
        print("cannot print invalid loop")
        raise Exception("Invalid Loop")

    loop = set(points)
    for a, b in zip(points, points[1:] + [points[0]]):
        ar, ac = a
        br, bc = b
        max_r, min_r = max(ar, br), min(ar, br)
        max_c, min_c = max(ac, bc), min(ac, bc)
        for r in range(min_r, max_r):
            assert ac == bc, f"{ac} == {bc}"
            loop.add((r, ac))
        for c in range(min_c, max_c):
            assert ar == br, f"{ar} == {br}"
            loop.add((ar, c))

    max_r, min_r = max(p[0] for p in points), min(p[0] for p in points)
    max_c, min_c = max(p[1] for p in points), min(p[1] for p in points)

    for r in range(min_r, max_r + 1):
        f.write(str(r).ljust(5) + "".join("#" if (r, c)
                in loop else "." for c in range(min_c, max_c + 1)) + "\n")
    f.write("\n")
    f.close()


def tidy_loop(points, first_tidy=True):
    if not is_valid_loop(points):
        raise Exception("unable to tidy an invalid loop")
    points_and_directions = []
    for a, b in zip(points, points[1:] + [points[0]]):
        dir = (0 if a[0] == b[0] else 1 if a[0] > b[0] else -1,
               0 if a[1] == b[1] else 1 if a[1] > b[1] else -1)
        points_and_directions.append([a, dir])

    def find_next_point_index(ps, dir):
        for i, x in enumerate(ps):
            if x[1] != dir:
                return i
        return -1

    tidied_loop = []
    while points_and_directions:
        curr_point, curr_dir = points_and_directions.pop(0)
        i = find_next_point_index(points_and_directions, curr_dir)
        if i >= 0:
            points_and_directions = points_and_directions[i:]
        tidied_loop.append(curr_point)

    if first_tidy and len(points) > 4:
        tidied_loop = tidy_loop(tidied_loop[-2:] + tidied_loop[:-2], False)

    if not is_valid_loop(tidied_loop, check_same_directions=True):
        raise Exception("invalid loop created")
    return tidied_loop


# slice off the top rectangle then repeat
def calculate_area(points):
    points = tidy_loop(points)

    if len(points) == 0:
        return 0
    if len(points) == 4:
        print_loop(points)
        rlist = [r for r, c in points]
        clist = [c for r, c in points]
        area = abs(max(rlist) - min(rlist) + 1) * \
            abs(max(clist) - min(clist) + 1)
        return area

    if len(points) < 4:
        raise Exception(f"not enough points: {points}")

    top_r = min(r for r, c in points)
    top_c = min(c for r, c in points if r == top_r)
    first_point_i = next(i for i, (r, c) in enumerate(
        points) if r == top_r and c == top_c)
    if first_point_i < 2:
        return calculate_area(points[-2:] + points[:-2])

    if first_point_i > len(points) - 3:
        return calculate_area(points[-4:] + points[:-4])

    a, b, c, d = points[first_point_i - 1:first_point_i + 3]
    rect = [a, b, c, d]
    print(points[first_point_i - 3:first_point_i + 4])
    print(first_point_i, rect)
    print_loop(points)
    assert points[first_point_i][0] == points[first_point_i +
                                              1][0], f"{points[first_point_i][0]} == {points[first_point_i + 1][0]} Rs match up"

    # if we're moving back and forth in a line, we need some special logic
    if [r for r, c in rect].count(top_r) > 2:
        # b will always be the left-most, upmost point
        if (c[1] > b[1] and d[1] > c[1]) or (c[1] < b[1] and d[1] < c[1]):
            raise Exception(f"invalid loop: {rect}")

        replacement_points = []
        # b is too far left?
        # c is too far left
        # c is too far right
        if a[0] == b[0]:
            replacement_points = [a, c, d]
        elif c[1] < b[1]:
            replacement_points = [a, b, d]
        elif c[1] > d[1]:
            replacement_points = [a, b, d]
        else:
            print("rect", rect)
            raise Exception("didn't think about this case")

        print("replacing a back and forth", rect, "with", replacement_points)
        area = 0
        return area + calculate_area(points[:first_point_i - 1] + replacement_points + points[first_point_i + 3:])

    next_r_for_a_d = min(a[0], d[0])
    next_r_for_loop = min(r for r, c in points if r != top_r)
    if next_r_for_a_d == next_r_for_loop:
        next_r = next_r_for_a_d
        area = (abs(top_r - next_r)) * (abs(b[1] - c[1]) + 1)
        # if the Rs are the same, we can drop down 2
        if a[0] == d[0]:
            replacement_points = [(next_r, a[1]), (next_r, d[1])]
        # if A is further up, we need to preserve the next D point
        # because we're using the A's R as next_r
        elif a[0] < d[0]:
            replacement_points = [(next_r, a[1]), (next_r, d[1]), d]
        # otherwise, we want to preserve the A point
        else:
            replacement_points = [a, (next_r, a[1]), (next_r, d[1])]

        updated_points = points[:first_point_i - 1] + \
            replacement_points + points[first_point_i + 3:]

        if not is_valid_loop(updated_points):
            print('unable to replace', rect, "with", replacement_points)
            raise Exception("invalid replacement")

        return area + calculate_area(updated_points)


def main(s, is_part_2=False):
    loop = []
    curr = 0
    instructions = []
    for line in s.split("\n"):
        dir, n, hex = line.split()
        if is_part_2:
            dir, n = extract_instruction(hex[1:-1])
        instructions.append((dir, int(n)))

    loop = []
    curr = 0
    while instructions:
        dir, n = instructions.pop(0)
        while instructions and dir == instructions[0][0]:
            n += instructions.pop(0)[1]
        curr += DIRS[dir] * n
        loop.append(curr)

    loop = list((int(x.real), int(x.imag)) for x in loop)
    print_loop(loop)
    print(loop)
    return calculate_area(loop)


real = open("./day18.input").read()
# print("ex part 1:", main(ex, is_part_2=False))
print("real part 1", main(real, is_part_2=False))

# print("ex part 2:", main(ex, is_part_2=True))
# print("real part 2:", main(real, is_part_2=True))
