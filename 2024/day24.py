
from collections import Counter, defaultdict
import itertools
import random

def simulate (gates, x, y, swaps = {}):
    values = {}
    for i in range(min(len(x), len(y))):
        values[f"x{str(i).zfill(2)}"] = x[i]
        values[f"y{str(i).zfill(2)}"] = y[i]

    while True:
        changed = False
        for a, b in gates:
            outputs = gates[(a, b)]
            for comb, c in outputs:
                if c in swaps:
                    c = swaps[c]
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


def test (gates, override, i):
    for dx, dy in [(1, 0), (0, 1), (1, 1), (0, 0)]:
        x = [0] * 45
        y = [0] * 45
        x[i] += dx
        y[i] += dy

        xn = int("".join(str(a) for a in reversed(x)), base=2)
        yn = int("".join(str(a) for a in reversed(y)), base=2)
        result = simulate(gates, x, y, override)
        if result != xn + yn:
            return False
    return True

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
    p2 = {
        # 'z11', 'z10' (tried and didn't seem to lead anywhere good)        
        # 'z40': 'z39', didn't seem to work
    }

    fixes = (
        ('fhg', 'z17'),
        ('z10', 'vcf'),
        ('z39', 'tnc'),
        ('dvb', 'fsq'),
        # ('z35', 'bwc')
        # ('z35', 'fsq')
        # ('z35', 'z36')
    )

    # possible fix 10 ('z10', 'z11')
    # possible fix 10 ('z10', 'fgb')
    # possible fix 10 ('z10', 'vcf')
    # possible fix 9 ('z10', 'z11')
    # possible fix 9 ('z10', 'fgb')
    # possible fix 9 ('z10', 'vcf')


    for a, b in fixes:
        p2[a] = b
        p2[b] = a




    # ('tnc', 'z39')
    # ('tnc', 'rvd')
    # ('z40', 'z39')
    # ('z40', 'rvd')

    print(",".join(sorted(p2.keys())))




    # possible fix 40 ('wrj', 'rtf')
    # possible fix 40 ('rtf', 'rvd')

    # possible fix 17 ('fhg', 'z17') — only fix for 17
    # 'z10', 'z11' —

    possible_swaps = set()
    for i in range(44, -1, -1):
        if not test(gates, p2, i):
            output_gates = set()
            for l in gates.values():
                for comb, c in l:
                    output_gates.add(c)
                checked = set()

            for a in output_gates:
                for b in output_gates:
                    if a == b or (b, a) in checked or (a, b) in checked:
                        continue
                    checked.add((a, b))
                    override = p2 | { a: b, b: a }
                    if test(gates, override, i):
                        print("possible fix", i, (a, b))
                        possible_swaps.add((a, b))
    print(f"testing out combos. there are {len(possible_swaps)} swaps")
    for combo in itertools.combinations(possible_swaps, 4 - len(p2)//2):
        s = set()
        for a, b in combo:
            s.add(a)
            s.add(b)
        if len(s) != 8:
            continue
        print(combo)
        overrides = {} | p2
        for a, b in combo:
            overrides[a] = b
            overrides[b] = a

        failed = False
        for i in range(44, -1, -1):
            if not test(gates, p2 | override, i):
                failed = True
                break
        if not failed:
            print("possible valid swaps", override)

    return simulate(gates, p1x, p1y)

# print(main(open("./day24.example").read()))
print(main(open("./day24.input").read()))
