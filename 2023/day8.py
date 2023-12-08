import math
import re


ex = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


class Node:
    def __init__(self, left, right):
        self.L = left
        self.R = right


def main(s):
    moves, node_string = s.split("\n\n")

    nodes = {}
    for line in node_string.split("\n"):
        [a, l, r] = re.match(r'(\w+) = \((\w+), (\w+)\)', line).groups()
        nodes[a] = (l, r)

    loop_lengths = []
    for curr in [node for node in nodes if node.endswith("A")]:
        loop = {}
        move_count = 0
        while True:
            move = 0 if moves[move_count % len(moves)] == "L" else 1
            curr = nodes[curr][move]
            move_count += 1
            if not curr.endswith("Z"):
                continue
            entry = (move_count % len(moves), curr)
            if entry in loop:
                # assuming only a single Z-touching loop
                # and that A to first Z == Z to Z
                loop_lengths.append(move_count - loop[entry])
                break
            else:
                loop[entry] = move_count

    return math.lcm(*loop_lengths)


print("ex:", main(ex))
print("real:", main(open("./day8.input").read()))
