ex = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def get_next(seq):
    if all(n == 0 for n in seq):
        return [0] + seq
    lower = get_next([b - a for a, b in zip(seq, seq[1:])])
    return seq + [seq[-1] + lower[-1]]


def main(s):
    part1 = 0
    part2 = 0
    for l in s.split("\n"):
        seq = list(map(int, l.split()))
        part1 += get_next(seq)[-1]
        part2 += get_next(list(reversed(seq)))[-1]

    return (part1, part2)


print("ex", main(ex))
print("real", main(open("day9.input").read()))
