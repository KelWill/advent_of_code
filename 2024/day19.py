import functools


real = open("./day19.input").read()
ex = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


@functools.cache
def ways_possible (pattern, remaining):
    ways = 0
    if pattern == "":
        return 1
    for i, r in enumerate(remaining):
        if not pattern.startswith(r):
            continue
        ways += ways_possible(pattern[len(r):], remaining)
    return ways



def main (s):
    towels, patterns = s.split("\n\n")
    towels = tuple(towels.split(", "))
    patterns = patterns.split("\n")

    return sum(ways_possible(p, towels) for p in patterns)

print(main(ex))
print(main(real))





