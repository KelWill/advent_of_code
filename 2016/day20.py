real = open('./day20.input').read()
ex = """5-8
0-2
4-7"""


def combine_ranges(ranges):
    ranges = sorted(ranges)
    results = []
    start, end = ranges.pop(0)
    while ranges:
        startx, endx = ranges.pop(0)
        if startx > end + 1:
            results.append((start, end))
            start = startx
            end = endx
        else:
            end = max(endx, end)
    results.append((start, end))
    return results


def main(s, ip_count):
    ranges = []
    for x in s.split("\n"):
        a, b = map(int, x.split("-"))
        ranges.append((a, b))

    results = combine_ranges(ranges)
    ip = results[0][1] + 1

    for a, b in results:
        ip_count -= (b - a + 1)

    return ip, ip_count + 1


print("ex:", main(ex, 9))
print("real:", main(real, 4294967295))
