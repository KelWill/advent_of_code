

from collections import defaultdict
import math


def simulate (gates, x, y):
    values = {}
    for i in range(len(x)):
        values[f"x{str(i).zfill(2)}"] = x[i]
        values[f"y{str(i).zfill(2)}"] = y[i]

    while True:
        changed = False
        for a, b in gates:
            outputs = gates[(a, b)]
            for comb, c in outputs:
                if c in values or (a not in values) or (b not in values):
                    continue
                if comb == "AND":
                    values[c] = values[a] and values[b]
                elif comb == "OR":
                    values[c] = values[a] or values[b]
                elif comb == "XOR":
                    values[c] = values[a] != values[b]
                changed = True
        if not changed:
            break

    zs = []
    for k, v in values.items():
        if not k.startswith("z"):
            continue
        zs.append((k, v))

    return int("".join("1" if v else "0" for k,v in sorted(zs, reverse=True)), 2)

def main (s):
    initial_values, gate_string = s.split("\n\n")
    xy = [[], []]
    for r in initial_values.split("\n"):
        a, b = r.split(": ")
        xy[a.startswith("y")].append(int(b))
    p1x, p1y = xy

    gates = defaultdict(list)
    for row in gate_string.split("\n"):
        a, comb, b, _, c = row.split(" ")
        gates[(a, b)].append((comb, c))

    return simulate(gates, p1x, p1y)

print(main(open("./day24.example").read()))
# print(main(open("./day24.input").read()))
