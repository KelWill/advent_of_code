from collections import Counter
import math
import re
ex = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def part1(s):
    total = 0
    reqs = Counter({"red": 12, "green": 13, "blue": 14})
    for i, row in enumerate(s.split("\n")):
        turns = [re.findall(r'(\d+) (\w+)', turn) for turn in row.split(";")]
        if not any(Counter({color: int(n) for n, color in turn}) > reqs for turn in turns):
            total += i
    return total


def part2(s):
    total = 0
    for row in s.split("\n"):
        maxima = Counter()
        for turn in row.split(";"):
            turn_colors = re.findall(r'(\d+) (\w+)', turn)
            maxima = maxima | Counter({color: int(n)
                                      for n, color in turn_colors})
        total += math.prod(maxima.values())
    return total


print("part1 example", part1(ex))
print("part1", part1(open("day2.input").read()))
print("part2 example", part2(ex))
print("part2", part2(open("day2.input").read()))
