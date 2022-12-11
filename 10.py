input = open("10.input").read()
# input = open("10.example").read()

sprite = 1
cycle = 0
summed_signal_strength = 0

def do_cycle ():
  r = cycle // 40
  if sprite - 1 <= (cycle % 40) <= sprite + 1:
    positions[r][cycle % 40] = "#"

positions = []
for i in range(0, 6):
  positions.append([" " for x in range(0, 40)])

for row in input.split("\n"):
  if row == "noop":
    do_cycle()
    cycle += 1
    if not (cycle - 20) % 40:
      summed_signal_strength += cycle * sprite
    continue

  for i in range(0, 2):
    do_cycle()
    cycle += 1
    if not (cycle - 20) % 40:
      summed_signal_strength += cycle * sprite

  add, v = row.split(" ")
  v = int(v)
  sprite += v

print(f"part1: {summed_signal_strength}")
print("part2:")
for row in positions:
  print("".join(row))
