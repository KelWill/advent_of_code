from functools import cache

fav_number = 1350


def main():
    seen = set([(1, 1)])
    curr = [(1, 1)]
    steps = 0
    while curr:
        next_curr = []
        for x, y in curr:
            # if x == 31 and y == 39:
            #     return steps
            for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                xx = x + dx
                yy = y + dy
                if xx < 0 or yy < 0:
                    continue
                if is_wall(xx, yy):
                    continue
                if (xx, yy) in seen:
                    continue
                seen.add((xx, yy))
                next_curr.append((xx, yy))
        steps += 1
        if steps == 50:
            return len(seen)
        curr = next_curr


@cache
def is_wall(x, y):
    n = fav_number + x * x + 3 * x + 2 * x * y + y + y * y
    return n.bit_count() % 2 == 1


print(main())
