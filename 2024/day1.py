import re
from collections import Counter

ex = """3   4
4   3
2   5
1   3
3   9
3   3"""
real = open("./day1.input").read()

def get_ints(s):
    return map(int, re.findall(r"\d+", s))

def main (s):
    left, right = zip(*[get_ints(line) for line in s.split("\n")])
    right = Counter(right)
    # part1: return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))
    return sum(a * right[a] for a in left)
print(main(ex), main(real))