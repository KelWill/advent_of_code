import functools
real = open("./day19.input").read()

@functools.cache
def ways_possible (pattern, remaining):
    if pattern == "":
        return 1    
    return sum(ways_possible(pattern[len(r):], remaining) for r in remaining if pattern.startswith(r))

def main (s):
    towels, patterns = s.split("\n\n")
    towels = tuple(towels.split(", "))
    patterns = patterns.split("\n")
    result = [*(ways_possible(p, towels) for p in patterns)]
    return sum(r > 0 for r in result), sum(result)

print(main(real))
