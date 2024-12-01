import re
import itertools

ex = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""


def is_safe_floor(floor):
    chips, gens = floor
    if len(gens) == 0:
        return True
    if len(chips) == 0:
        return True
    return chips & gens == chips


def get_next_options(curr_floor, floors):
    options = []
    chips, gens = floors[curr_floor]

    moves = []
    op_size = len(chips) + len(gens)
    keys = list(chips) + list(gens)
    for take1 in range(op_size):
        for take2 in range(take1 + 1, op_size + 1):
            move = [set(), set()]
            move[take1 >= len(chips)] |= {keys[take1]}
            if take2 < op_size:
                move[take2 >= len(chips)] |= {keys[take2]}
            moves.append(move)

    if curr_floor < len(floors) - 1:
        for chip_move, gen_move in moves:
            curr_chips, curr_gen = floors[curr_floor]
            next_chips, next_gen = floors[curr_floor + 1]
            updated_current_floor = (
                curr_chips - chip_move, curr_gen - gen_move)
            updated_next_floor = (next_chips | chip_move, next_gen | gen_move)
            if is_safe_floor(updated_current_floor) and is_safe_floor(updated_next_floor):
                options.append((curr_floor + 1, floors[:curr_floor] + (updated_current_floor,) +
                               (updated_next_floor,) + floors[curr_floor + 2:]))
    if curr_floor > 0 and any(chips | gens for chips, gens in floors[:curr_floor]):
        for chip_move, gen_move in moves:
            curr_chips, curr_gen = floors[curr_floor]
            next_chips, next_gen = floors[curr_floor - 1]
            updated_current_floor = (
                curr_chips - chip_move, curr_gen - gen_move)
            updated_prev_floor = (next_chips | chip_move, next_gen | gen_move)
            if is_safe_floor(updated_current_floor) and is_safe_floor(updated_prev_floor):
                options.append((curr_floor - 1, floors[:curr_floor - 1] + (
                    updated_prev_floor,) + (updated_current_floor,) + floors[curr_floor + 1:]))
    return options


def get_key(curr_floor, floors):
    pairs = []
    chips = set()
    for c, g in floors:
        chips |= c
    chip_floor = 0
    gen_floor = 0
    for chip in chips:
        for i in range(len(floors)):
            chips, gens = floors[i]
            if chip in chips:
                chip_floor = i
            if chip in gens:
                gen_floor = i
        pairs.append((chip_floor, gen_floor))
    return (curr_floor,) + tuple(sorted(pairs))


def part1(s):
    floors = tuple((set(), set()) for i in range(0, 4))

    all_chips = set()
    for i, row in enumerate(s.split("\n")):
        chips = re.findall(r"(\w+)-compatible microchip", row)
        generators = re.findall(r"(\w+) generator", row)
        for chip in chips:
            floors[i][0].add(chip)
            all_chips.add(chip)
        for gen in generators:
            floors[i][1].add(gen)
    floor_possibilities = [(0, floors)]
    step_count = 0
    seen = set()
    while len(floor_possibilities):
        floor_possibilities = sum([get_next_options(
            curr_floor, floors) for curr_floor, floors in floor_possibilities], [])
        step_count += 1

        filtered_floor_possibilities = []
        for poss in floor_possibilities:
            if get_key(*poss) in seen:
                continue
            filtered_floor_possibilities.append(poss)
            seen.add(get_key(*poss))
        floor_possibilities = filtered_floor_possibilities

        for curr_floor, floors in floor_possibilities:
            if curr_floor != 3:
                continue
            if len(floors[3][0]) != len(floors[3][1]) or len(floors[3][0]) != len(all_chips):
                continue
            return step_count

    raise Exception("no answer")


print(part1(ex))
print(part1(open("./day11.input").read()))
