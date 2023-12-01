part_1_ex = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

part_2_ex = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def part1(s):
    total = 0
    for row in s.split("\n"):
        digits = [c for c in row if c.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


def part2(s):
    total = 0
    numbers = ["one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
    for row in s.split("\n"):
        digits = []
        for i, c in enumerate(row):
            if c.isdigit():
                digits.append(c)
            for j, numname in enumerate(numbers):
                if row[i:].startswith(numname):
                    digits.append(str(j + 1))
        total += int(digits[0] + digits[-1])
    return total


day1input = open("./day1.input").read()
print(f"part1 ex: {part1(part_1_ex)}, part2 ex: {part2(part_2_ex)}")
print(f"part1: {part1(day1input)}, part2: {part2(day1input)}")
