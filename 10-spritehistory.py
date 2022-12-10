input = open("10.input").read()
# input = open("10.example").read()

# storing the history of X at the time of the cycle
x = 1
sprites = [1]

for row in input.split("\n"):
    sprites.append(x)
    if row == "noop":
        continue
    sprites.append(x)

    _, v = row.split()
    x += int(v)

special_cycles = (x for x in range(0, 241) if not (x - 20) % 40)
summed_signal_strength = sum(sprites[i] * i for i in special_cycles)

print(f"part1: {summed_signal_strength}")

# sprites[1:] -- sprites[0] is fake starting value. We need to start with cycle-1
for i, x in enumerate(sprites[1:]):
    # end= you can override print's default end-line "\n"
    # yoinked from https://github.com/fuglede/adventofcode/blob/master/2022/day10/solutions.py 
    print("#" if i % 40 - 1 <= x <= i % 40 + 1 else " ", end = "" if (i + 1) % 40 else "\n")
