import re

ex = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def get_ints(s):
    return list(map(int, re.findall(r'\d+', s)))


def step(seed_range, mappers):
    result = []
    seed_ranges = [seed_range]
    while seed_ranges:
        (start, end) = seed_ranges.pop()

        if start >= end:
            continue
        changed = False
        for (_name, map_start, map_end, diff) in mappers:
            if end <= map_start or start >= map_end:
                continue
            changed = True
            sliced_range = (max(start, map_start) + diff,
                            min(end, map_end) + diff)

            left_range = (start, map_start) if start < map_start else (0, 0)
            right_range = (map_end, end) if map_end < end else (0, 0)

            # print(f"{(start, end)} is in range {(map_start, map_end)} with diff {diff}. Updated to {left_range}, {sliced_range}, {right_range}")

            seed_ranges.append(left_range)
            seed_ranges.append(right_range)
            result.append(sliced_range)
        if not changed:
            result.append((start, end))

    return result


def get_min_loc(seeds, mappers):
    seed_locs = []
    for (seed_start, seed_end) in seeds:
        curr = [(seed_start, seed_end)]
        next_curr = []
        for seed_maps in mappers:
            for seed_range in curr:
                next_curr += step(seed_range, seed_maps)
            curr = next_curr
            next_curr = []
        seed_locs += curr

    return min([start for start, end in seed_locs])


def main(s):
    first, *rest = s.split("\n\n")
    mappers = []
    maps = []
    for r in rest:
        name = None
        for line in r.split("\n"):
            if ":" in line:
                name = line
                mappers.append(maps)
                maps = []
                continue
            [dest_start, source_start, range_len] = get_ints(line)
            source_end = source_start + range_len
            diff = dest_start - source_start
            maps.append((name, source_start, source_end, diff))
    mappers.append(maps)
    mappers = [m for m in mappers if m]
    seed_ints = get_ints(first)
    part1_seeds = [(x, x + 1) for x in get_ints(first)]
    part2_seeds = [(seed_ints[i], seed_ints[i] + seed_ints[i + 1])
                   for i in range(0, len(seed_ints), 2)]

    return (get_min_loc(part1_seeds, mappers), get_min_loc(part2_seeds, mappers))


print("ex", main(ex))
print("real", main(open("./day5.input").read()))
# go backwards?
