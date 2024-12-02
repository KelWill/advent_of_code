import re
from collections import Counter, defaultdict

ex = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
real = open("./day2.input").read()

def is_safe (l):
    increasing = l[0] < l[1]
    for a, b in zip(l, l[1::]):
        diff = abs(a - b)
        if diff > 3 or diff <= 0:
            return False
        if increasing and a > b:
            return False
        if not increasing and a < b:
            return False
    return True

def main (s):
    p1count = 0
    p2count = 0
    for l in s.split("\n"):
        l = [*map(int, l.split())]
        p1count += is_safe(l)
        p2safe = is_safe(l)
        for skip in range(0, len(l)):
            if is_safe(l[0:skip] + l[skip + 1:]):
                p2safe = True
                break
        p2count += p2safe

    return p1count, p2count

print(main(ex))
print(main(real))