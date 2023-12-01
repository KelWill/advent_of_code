input = open("4.input").read()

count = 0
for row in input.split("\n"):
    [a, b, c, d] = map(int, row.replace("-", ",").split(","))
    if (a >= c and b <= d) or (c >= a and d <= b):
        count += 1

print(f"part 1: {count}")

count = 0
for row in input.split("\n"):
    [a, b, c, d] = map(int, row.replace("-", ",").split(","))
    if not (b < c or d < a):
        count += 1

print(f"part 2: {count}")
