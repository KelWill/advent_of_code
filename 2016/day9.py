

"""
ADVENT contains no markers and decompresses to itself with no changes, resulting in a decompressed length of 6.
A(1x5)BC repeats only the B a total of 5 times, becoming ABBBBBC for a decompressed length of 7.
(3x3)XYZ becomes XYZXYZXYZ for a decompressed length of 9.
A(2x2)BCD(2x2)EFG doubles the BC and EF, becoming ABCBCDEFEFG for a decompressed length of 11.
(6x1)(1x3)A simply becomes (1x3)A - the (1x3) looks like a marker, but because it's within a data section of another marker, it is not treated any differently from the A that comes after it. It has a decompressed length of 6.
X(8x2)(3x3)ABCY becomes X(3x3)ABC(3x3)ABCY (for a decompressed length of 18), because the decompressed data from the (8x2) marker (the (3x3)ABC) is skipped and not processed further.
"""

ex = """ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY"""


def get_decompressed_string(s, start=0):
    if s.find("(", start) == -1:
        return s
    i = s.index("(", start)
    j = s.index(")", i)
    a, b = map(int, s[i + 1:j].split("x"))
    rs = s[j + 1: j + 1 + a]
    return get_decompressed_string(s[0:i] + rs * b + s[j + 1 + a:], i + a * b)


def get_decompressed_length(s):
    if "(" not in s:
        return len(s)
    i = s.index("(")
    j = s.index(")", i)
    a, b = map(int, s[i + 1:j].split("x"))
    before = s[0:i]
    rs = s[j + 1:j + 1 + a]
    after = s[j + 1 + a:]
    return len(before) + b * get_decompressed_length(rs) + get_decompressed_length(after)


# print(get_decompressed_length("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
for r in ex.split("\n"):
    print(r, get_decompressed_string(r))
print(get_decompressed_length(open("day9-input").read()))
