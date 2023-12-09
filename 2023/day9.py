ex = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def get_next(seq):
    if all(n == 0 for n in seq):
        return 0
    return seq[-1] + get_next([b - a for a, b in zip(seq, seq[1:])])


def main(s):
    seqs = [list(map(int, l.split())) for l in s.split("\n")]
    return (sum(get_next(seq) for seq in seqs),
            sum(get_next(list(reversed(seq))) for seq in seqs))


print("ex", main(ex))
print("real", main(open("day9.input").read()))
