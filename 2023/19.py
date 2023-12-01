import re
from collections import defaultdict 
import math

example = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

def parse_input (line):
    results = {}
    for (robot, depenency_string) in re.findall("Each ([a-z]+) robot costs ([^.]+)", line):
        costs = dict(map(lambda t: (t[1], int(t[0])), re.findall("(\d+) (\w+)", depenency_string)))
        results[robot] = costs
    return results


def solve(input):

    blueprint_list = [parse_input(line) for line in input.split("\n")]

    geodes = 0
    def dp (blueprint, robot_count, resource_count, t):
        nonlocal geodes
        if t == 0:
            geodes = max(geodes, resource_count.get("geode", 0))
            return
        if t < 0:
            raise Exception(f"can't have negative time {t}")

        max_robots = defaultdict(lambda: 0)
        for robot, cost in blueprint.items():
            for k, n in cost.items():
                max_robots[k] = max(max_robots[k], n)

        possible_next_robots = [robot for robot, cost in blueprint.items() if all(robot_count[k] for k in cost) and robot_count[robot] < max_robots[robot]]

        for robot in possible_next_robots:
            cost = blueprint[robot]
            required_time = 0
            for k, n in cost.items():
                required = n - resource_count[k]
                if required <= 0:
                    continue
                required_time = max(math.ceil(required / robot_count[k]), required_time)

            updated_resource_count = resource_count.copy()
            for k, n in robot_count.items():
                updated_resource_count[k] += n * required_time
            
            for k, n in cost.items():
                updated_resource_count[k] -= n
            
            updated_robot_count = robot_count.copy()
            updated_robot_count[robot] += 1
            dp(blueprint, updated_robot_count, updated_resource_count, t - required_time)

    for blueprint in blueprint_list:
        robot_count = defaultdict(lambda: 0)
        robot_count["ore"] = 1
        print(dp(blueprint, robot_count, defaultdict(lambda: 0), 24))
        print(geodes)
        geodes = 0

solve(example)