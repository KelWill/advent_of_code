from dataclasses import dataclass
import re


example_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

@dataclass
class Valve:
    name: str
    flow_rate: int
    to: tuple

def ints (s):
    return list(map(int, re.findall("-?\d+", s)))

def parse_row (row):
    name = row[6:8]
    flow_rate = ints(row)[0]
    row = row.replace("valves", "valve")
    to = row.split(" valve ")[1].split(", ")

    return Valve(name, flow_rate, to)


def calculate_distances (valve, all_valves):
    distances = {}
    for k, v in all_valves.items():
        distances[v.name] = 0 if v == valve else 1e9
    unvisited = set(k for k, v in all_valves.items())
    curr = valve
    while curr:
        for n in curr.to:
            distances[n.name] = min(distances[curr.name] + 1, distances[n.name])
        unvisited.remove(curr.name)
        min_dist = 1e9
        next_node = None
        for name in unvisited:
            if distances[name] < min_dist:
                min_dist = distances[name]
                next_node = name
        if not next_node:
            return distances
        curr = all_valves[next_node]
    return distances





def solve (input):
    valves = [parse_row(row) for row in input.split("\n")]
    valve_dict = {}
    for valve in valves:
        valve_dict[valve.name] = valve

    for valve in valves:
        valve.to = [valve_dict[k] for k in valve.to]

    for valve in valves:
        valve.distances = calculate_distances(valve, valve_dict)

    positive_valves = [v for v in valves if v.flow_rate > 0]

    max_flow_rate_for_valves = {}

    def dp (curr, visited, t, score):
        nonlocal max_flow_rate_for_valves
        key = "-".join(sorted(visited))
        max_flow_rate_for_valves[key] = max(max_flow_rate_for_valves.get(key, 0), score)
        for valve in positive_valves:
            if valve.name in visited: continue

            updated_t = t + curr.distances[valve.name] + 1
            if updated_t > 26: continue

            dp(valve, visited | set([valve.name]), updated_t, score + valve.flow_rate * (26 - updated_t))

    dp(valve_dict["AA"], set(), 0, 0)
    print(max_flow_rate_for_valves)

    m = 0
    for visited, score1 in max_flow_rate_for_valves.items():
        for other, score2 in max_flow_rate_for_valves.items():
            shared = set(visited.split("-")) & set(other.split("-"))
            if shared: continue
            m = max(m, score1 + score2)
    print(m)


solve(example_input)
solve(open("16.input").read())