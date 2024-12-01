"""Its left and center tiles are traps, but its right tile is not.
Its center and right tiles are traps, but its left tile is not.
Only its left tile is a trap.
Only its right tile is a trap.
"""

import functools


real = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."
ex = ".^^.^.^^^^"


def is_trapped(i, parent_row):
    left = parent_row[i - 1] if i else False
    right = parent_row[i + 1] if i < len(parent_row) - 1 else False

    check = [left, right]

    trap_setups = [
        [True,  False],
        [False, True],
    ]

    return any(check == t for t in trap_setups)


def main(s, n):
    row = tuple(x == "^" for x in s)
    total = 0
    for i in range(n):
        total += sum(not x for x in row)
        row = tuple(is_trapped(j, row) for j in range(len(s)))
    return total


print(main(ex, 10))
print(main(real, 400000))
