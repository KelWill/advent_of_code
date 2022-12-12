import itertools
import sys

def get_elev (c):
  if c == "E":
    return ord("z")
  elif c == "S":
    return ord("a")
  else:
    return ord(c)

def solve (is_part_1):
  input = open("12.input" if len(sys.argv) == 1 else sys.argv[1]).read()
  data = [list(x) for x in input.split("\n")]

  starting_r = 0
  starting_c = 0
  for r, row in enumerate(data):
    for c, col in enumerate(row):
      if col == "E":
        starting_r = r
        starting_c = c

  positions = [[starting_r, starting_c]]
  seen = set()
  moves = 0
  while positions:
    moves += 1
    next_positions = []
    for [r0, c0] in positions:
      for [dr, dc] in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        r = r0 + dr
        c = c0 + dc

        if not (0 <= r < len(data) and 0 <= c < len(data[0])):
          continue

        key = str([r, c])
        if key in seen:
          continue

        diff = get_elev(data[r0][c0]) - get_elev(data[r][c])

        if (diff > 1):
          continue

        next_positions.append([r, c])
        seen.add(key)

        if data[r][c] == "S" or data[r][c] == "a":
          return moves

    positions = next_positions

print(solve())
