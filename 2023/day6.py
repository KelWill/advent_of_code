import re

ex = """Time:      7  15   30
Distance:  9  40  200"""

real = """Time:        46     82     84     79
Distance:   347   1522   1406   1471"""


def get_ints(s):
    return list(map(int, re.findall(r'\d+', s)))


def part1(s):
    times, records = map(get_ints, s.split("\n"))

    prod = 1
    for time, record in zip(times, records):
        ways = 0
        goal = record + 1
        for hold_time in range(1, time):
            dist = (time - hold_time) * hold_time
            if dist >= goal:
                ways += 1
        prod *= ways
    return prod


def part2(s):
    times, records = s.split("\n")

    time = int("".join(re.findall('\d+', times)))
    record = int("".join(re.findall('\d+', records)))

    min_hold_time = 0
    for hold_time in range(1, time):
        if (time - hold_time) * hold_time > record:
            min_hold_time = hold_time
            break
    max_hold_time = 0
    for hold_time in range(time, 1, -1):
        if (time - hold_time) * hold_time > record:
            max_hold_time = hold_time
            break
    return max_hold_time - min_hold_time + 1


print("ex:", part2(ex))
print("real:", part2(real))
