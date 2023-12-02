from collections import defaultdict
import re
ex = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

bag = "only 12 red cubes, 13 green cubes, and 14 blue cubes"


def part1(s):
    total = 0
    reqs = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    for i, row in enumerate(s.split("\n")):
        turns = [re.findall(r'(\d+) (\w+)', turn) for turn in row.split(";")]
        valid = True
        for turn in turns:
            if any(reqs[color] < int(n) for n, color in turn):
                valid = False
        if valid:
            total += i + 1
    return total


def part2(s):
    total = 0
    for row in s.split("\n"):
        maxima = defaultdict(int)
        for turn in row.split(";"):
            turn_colors = re.findall(r'(\d+) (\w+)', turn)
            for n, color in turn_colors:
                maxima[color] = max(maxima[color], int(n))
        total += maxima["red"] * maxima["blue"] * maxima["green"]
    return total


print("part1 example", part1(ex))
print("part1", part1(open("day2.input").read()))
print("part2 example", part2(ex))
print("part2", part2(open("day2.input").read()))
