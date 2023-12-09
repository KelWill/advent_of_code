import re


ex = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def get_ints(s):
    return list(map(int, re.findall(r'-?\d+', s)))


def get_next(seq):
    if all(n == 0 for n in seq):
        return [0] + seq
    if len(set(seq)) == 1:
        return seq + [seq[0]]

    lower = [b - a for a, b in zip(seq, seq[1:])]
    lower = get_next(lower)
    return [seq[0] - lower[0]] + seq


def main(s):
    seqs = []
    for l in s.split("\n"):
        seqs.append(get_next(get_ints(l)))

    return sum(seq[0] for seq in seqs)


print("ex", main(ex))
print("real", main(open("day9.input").read()))
