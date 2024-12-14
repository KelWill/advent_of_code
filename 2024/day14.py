import re
real = open("./day14.input").read()


ex = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""


def get_ints (s):
    return [*map(int, re.findall(r"-?\d+", s))]


def get_next_pos (x, y, dx, dy, X, Y):
    x += dx
    y += dy
    if x >= X:
        x -= X
    if y >= Y:
        y -= Y
    if y < 0:
        y += Y
    if x < 0:
        x += X
    return (x, y, dx, dy)
    

def render_robots (robots, X, Y):
    robots = [(x, y) for x, y, dx, dy in robots]
    results = ""
    for y in range(Y):
        line = ""
        for x in range(X):
            r = robots.count((x, y))
            line += "." if not r else "#"
        results += line + "\n"
    return results

def get_safety_score (robots, X, Y):
    midx = X // 2
    midy = Y // 2
    quadrant_ranges = [(range(*a), range(*b)) for a, b in [
        ((0, midx), (0, midy)),
        ((midx + 1, X), (0, midy)),
        ((0, midx), (midy + 1, Y)),
        ((midx + 1, X), (midy + 1, Y)),
    ]]
    quad_counts = [0, 0, 0, 0]
    for x, y in robots:
        for i, ranges in enumerate(quadrant_ranges):
            xr, yr = ranges
            if x in xr and y in yr:
                quad_counts[i] += 1

    prod = 1
    for q in quad_counts:
        prod *= q
    return prod


def main(s, width, height):
    robots = []
    for line in s.split("\n"):
        a, b, c, d = get_ints(line)
        robots.append((a, b, c, d))

    i = 0
    while True:
        robots = [get_next_pos(*r, width, height) for r in robots]
        tree = render_robots(robots, width, height)
        if "######" in tree:
            print(tree)
            i += 1
            print(i)

    # return get_safety_score(robots, width, height)


print(main(ex, 11, 7))
print(main(real, 101, 103))
