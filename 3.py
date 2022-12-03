input = open("3.input").read()

def get_priority (c):
    if c == c.upper():
        return ord(c) - ord("A") + 27
    return ord(c) - ord("a") + 1

total = 0
for row in input.split("\n"):
    half_len = len(row)//2
    first_half = set(row[:half_len]) & set(row[half_len:len(row)])
    total += get_priority(list(first_half)[0])

print("part 1: %d" % total)

total = 0
sets = []
for row in input.split("\n"):
    sets.append(set(row))
    if len(sets) == 3:
        shared = sets[0] & sets[1] & sets[2]
        total += get_priority(list(shared)[0])
        sets = []

print("part 2: %d" % total)
