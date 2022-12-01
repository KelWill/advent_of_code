import functools

input = open("./1.input").read()

maxes = []
for elf in input.split("\n\n"):
    sum = 0
    for n in elf.split("\n"):
        sum += int(n)
    maxes.append(sum)
    maxes.sort(reverse=True)
    if len(maxes) > 3:
        maxes.pop()

print(functools.reduce(lambda sum, x: sum + x, maxes, 0))
