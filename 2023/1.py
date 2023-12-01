input = open("./1.input").read()
maxes = [sum([int(s) for s in elf.split("\n")]) for elf in input.split("\n\n")]
maxes.sort(reverse=True)
print(sum(maxes[:3]))
