import re
ex = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
real = open("day3.input").read()

def get_ints (s):
    return [*map(int, re.findall(r'-?\d+', s))]

def p1 (s):
    nums = get_ints(" ".join(re.findall(r"mul\(\d+,\d+\)", s)))
    return sum(a * b for a,b in zip(nums[0::2], nums[1::2]))

def p2 (s):
    lines = s.split("don't()")
    result = p1(lines[0])
    for l in lines[1:]:
        _first, *rest = l.split("do()")
        result += p1(" ".join(rest))
    return result

print(p1(ex), p2(ex))
print(p1(real), p2(real))
