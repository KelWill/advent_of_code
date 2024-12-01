import re
from collections import defaultdict
input = """Disc #1 has 13 positions; at time=0, it is at position 11.
Disc #2 has 5 positions; at time=0, it is at position 0.
Disc #3 has 17 positions; at time=0, it is at position 11.
Disc #4 has 3 positions; at time=0, it is at position 0.
Disc #5 has 7 positions; at time=0, it is at position 2.
Disc #6 has 19 positions; at time=0, it is at position 17.
Disc #7 has 11 positions; at time=0, it is at position 0."""

ex = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""


def main(s):
    discs = []
    for i, row in enumerate(s.split("\n")):
        [pos_count, start] = map(int, re.match(
            r'.+ (\d+) positions.+ position (\d+)\.', row).groups())
        start = start + i + 1
        discs.append((pos_count, start))

    for disc in discs:
        print(disc)
    t = 0
    while any((start + t) % pos_count for pos_count, start in discs):
        t += 1
    return t


print(main(ex))
print(main(input))

"""
x = 12 mod 13
x = 2 mod 5

"""
