from dataclasses import dataclass
import re


ex = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def get_ints(s):
    return list(re.findall(r'-?\d+', s))


@dataclass
class Line:
    px: int
    py: int
    pz: int
    dx: int
    dy: int
    dz: int


def find_intersection(l1: Line, l2: Line):
    # x1 = px + t * dx
    # y1 = py + t * dy
    # x2 = px2 + t2 * dx2
    # y2 = py2 + t2 * dy2
    # px + t * dx = px2 + t2 * dx2
    # py + t * dy = py2 + t2 * dy2
    # t = (px2 - px + t2 * dx2) / dy
    # px + (px2 - px + t2 * dx2)(dx/dy) = px2 + t2 * dx2
    # (px - px2)/dx2 + (px2 - px + t2 * dx2)(dx/dy)/dx2 = t2
    # (px - px2)/dx2 + (px2 - px)*(dx/(dy * dx2)) + t2 * (dx/dy) = t2
    # t2 = ((px - px2)/dx2 + (px2 - px)*(dx/(dy * dx2))) / ((dy) * (dy - dx))

    return 0


def main(s):
    lines = []
    for l in s.split("\n"):
        x, y, z, dx, dy, dz = get_ints(l)
        lines.append(((x, dx), (y, dy), (z, dz)))


print("ex", main(ex))
