

def step(a):
    b = [0 if x else 1 for x in reversed(a[0:])]
    return a + [0] + b


def get_checksum(l):
    checksum = [1 if a == b else 0 for a, b, in zip(l[::2], l[1::2])]
    if not len(checksum) % 2:
        return get_checksum(checksum)
    return checksum


def main(s, goal_length):
    a = [1 if x == "1" else 0 for x in s]
    while len(a) < goal_length:
        a = step(a)
    a = a[:goal_length]
    return "".join(map(str, get_checksum(a)))


print(get_checksum([1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0]))

print("ex:", main("10000", 20))
print("real:", main("11110010111001001", 272))
print("real:", main("11110010111001001", 35651584))
