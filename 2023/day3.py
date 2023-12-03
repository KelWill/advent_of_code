import re
from operator import add
from functools import reduce
import math

ex = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def main(s):
    board = s.split("\n")
    nums = {}
    total = 0

    for r, row in enumerate(board):
        for m in re.finditer(r'\d+', row):
            num = tuple([(r, c)
                         for c in range(m.start(), m.end())])
            nums[num] = int(reduce(add, [board[r][c] for (r, c) in num]))

    adjacencies = {(r, c): set() for r in range(len(board)) for c in range(
        len(board[r])) if not board[r][c].isdigit() and not board[r][c] == "."}

    DRDC = [(dr, dc) for dr in (1, 0, -1)
            for dc in (1, 0, -1) if dr or dc]

    for num in nums:
        valid = False
        for (r, c) in num:
            for dr, dc in DRDC:
                if (r + dr, c + dc) in adjacencies:
                    adjacencies[(r + dr, c + dc)].add(num)
                    valid = True

        if valid:
            total += nums[num]

    gear_total = 0
    for r, c in adjacencies:
        adj = adjacencies[(r, c)]
        if board[r][c] != "*" or len(adj) != 2:
            continue
        gear_total += math.prod([nums[num] for num in adj])
    return (total, gear_total)


print(main(ex))
print(main(open("./day3.input").read()))
