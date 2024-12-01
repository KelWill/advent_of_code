
ex = 5
real = 3001330


class Elf:
    def __init__(self, num) -> None:
        self.next = None
        self.number = num


def part1(elf_count):
    elves = [Elf(i + 1) for i in range(elf_count)]
    for a, b in zip(elves, elves[1:] + [elves[0]]):
        a.next = b

    elf = elves[0]
    while elf.next != elf:
        elf.next = elf.next.next
        elf = elf.next
    return elf.number


def part2(elf_count):
    elves = [i for i in range(elf_count)]
    elf = 0
    prev_elf_val = 0
    while len(elves) > 1:
        elves.pop((elf + len(elves) // 2) % len(elves))
        if elves[elf % len(elves)] != prev_elf_val:
            elf += 2
        else:
            elf += 1
        elf = elf % len(elves)
        prev_elf_val = elves[elf]

    return elves[0] + 1


# print(part1(ex), part2(ex))

for n in range(1, 100):
    print(n, part2(n))
# print(part1(real), part2(real))
