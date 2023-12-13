import functools


ex = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


@functools.cache
def find_ways(spring_map, counts, curr_group_length=0, consumed_path=""):
    if not spring_map:
        return not counts and not curr_group_length

    char = spring_map[0]
    if char == "?":
        return find_ways("#" + spring_map[1:], counts, curr_group_length) + find_ways("." + spring_map[1:], counts, curr_group_length)
    elif char == "#":
        return find_ways(spring_map[1:], counts, curr_group_length + 1, consumed_path + spring_map[0])
    elif char == ".":
        if not curr_group_length:
            return find_ways(spring_map[1:], counts, 0, consumed_path + spring_map[0])
        if not counts or curr_group_length != counts[0]:
            return 0
        return find_ways(spring_map[1:], counts[1:], 0, consumed_path + spring_map[0])
    else:
        raise Exception(f"unknown char '{char}'")


def main(s, scale=1):
    total = 0
    for l in s.split("\n"):
        springs, contiguous_counts = l.split(" ")
        contiguous_counts = tuple(
            map(int, contiguous_counts.split(","))) * scale
        springs = "?".join([springs] * scale) + "."
        ways = find_ways(springs, contiguous_counts)
        total += ways
    return total


print("ex", main(ex, 5))
real_input = open("./day12.input").read()
print("real", main(real_input),
      main(real_input, 5))
