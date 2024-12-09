from itertools import combinations_with_replacement
import re
input = open(0).read()


def get_operators (n):
    if n == 0:
        yield []
        return
    ops = ["*", "+", "||"]
    for op in ops:
        for rest in get_operators(n - 1):
            yield [op] + rest

ans = 0
for line in input.split("\n"):
    goal, *rest = [*map(int, re.findall(r"\d+", line))]
    op_count = len(rest) - 1
    for ops in get_operators(op_count):
        nums = [*reversed([] + rest)]
        n = nums.pop()
        while nums:
            op = ops.pop()
            if op == "||":
                n = int(str(n) + str(nums.pop()))
            elif op == "*":
                n *= nums.pop()
            else:
                n += nums.pop()
            if n > goal:
                break
        if n == goal:
            ans += goal
            break

print(ans)
