import math

ex = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


def main(s):
    nodes = {}
    for l in s.split("\n"):
        left, right = l.split(" -> ")

        dests = right.split(", ")
        if left == "broadcaster":
            nodes[left] = {
                "dests": dests,
                "parents": [],
                "type": left,
            }
        else:
            t = left[0]
            name = left[1:]

            nodes[name] = {
                "name": name,
                "type": t,
                "dests": dests,
                "parents": []
            }
            if t == "%":
                nodes[name]["state"] = False
            else:
                nodes[name]["input_names"] = []
                nodes[name]["inputs"] = []

    for node_name in nodes:
        node = nodes[node_name]
        dests = node["dests"]
        for dest in dests:
            if not dest in nodes:
                continue
            nodes[dest]["parents"].append(node_name)
            if nodes[dest]["type"] == '&':
                nodes[dest]["input_names"].append(node_name)
                nodes[dest]["inputs"].append(False)

    cycle_counts = {}

    def handle_pulse(name, start, level, turns):
        if name not in nodes:
            return []
        node = nodes[name]
        if node["type"] == "%":
            if level:
                return []
            node["state"] = not node["state"]
            return [(dest, name, node["state"]) for dest in node["dests"]]
        else:
            i = node["input_names"].index(start)
            node["inputs"][i] = level
            next_pulse = not all(node["inputs"])
            if all(node["inputs"]) and not name in cycle_counts:
                cycle_counts[name] = turns
            return [(dest, name, next_pulse) for dest in node["dests"]]

    high_count = 0
    low_count = 0
    for turn in range(1, 100000):
        low_count += 1
        todo = [(name, "broadcast", False)
                for name in nodes["broadcaster"]["dests"]]
        while todo:
            high_count += sum(pulse_level for name, start, pulse_level in todo)
            low_count += sum(not pulse_level for name,
                             start, pulse_level in todo)
            nxt = []
            for name, start, pulse_level in todo:
                nxt += handle_pulse(name, start, pulse_level, turn)
            todo = nxt
    print(cycle_counts)

    def when_is_node(name, level):
        node = nodes[name]
        if node["type"] == "broadcaster":
            if not level:
                return [1]
            raise Exception("broadcaster never pulses")
        if node["type"] == "%":
            return [when_is_node(p, not level) for p in node["parents"]]
        elif node["type"] == "&":
            if node["name"] in cycle_counts and cycle_counts[name] != 1:
                x = cycle_counts[node["name"]]
                if level == True:
                    return x
                else:
                    return f"shouldn't get here"
            if level:
                return math.lcm(*[when_is_node(parent, False) for parent in node["parents"]])
            else:
                return math.lcm(*[when_is_node(parent, True)
                                  for parent in node["parents"]])

    print(when_is_node("hp", True))
    print("lcm", math.lcm(*cycle_counts.values()))
    prod = 1
    for x in cycle_counts.values():
        prod *= x
    return high_count * low_count


# print(main(ex))
print(main(open("./day20.input").read()))
