input = open("2.input").read()
# input = """A Y
# B X
# C Z"""
entries = [r.split(" ") for r in input.split("\n")]

score = 0
for [abc, xyz] in entries:
    elf_played = ord(abc) - ord("A")
    recommended = ord(xyz) - 23 - ord("A")

    score += recommended + 1
    if recommended == elf_played:
        score += 3
    elif recommended == (elf_played + 1) % 3:
        score += 6
print(f"part 1: %d" % score)

score = 0
for [abc, xyz] in entries:
    elf_played = ord(abc) - ord("A")

    if xyz == "Y":
        score += 3 + elf_played + 1
    elif xyz == "X":
        desired = (elf_played - 1)
        if desired == -1:
            desired = 2
        score += desired + 1
    else:
        desired = (elf_played + 1) % 3
        score += 6 + desired + 1
print(f"part 2: %d" % score)
