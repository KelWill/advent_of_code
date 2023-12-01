import itertools
import sys

def get_elev (c):
  if c == "S":
    return ord("a")
  elif c == "E":
    return ord("z")
  return ord(c)

def solve (is_part_1):
  input = open("12.input" if len(sys.argv) == 1 else sys.argv[1]).read()
  grid = [list(x) for x in input.split("\n")]

  starting_r = 0
  starting_c = 0
  target = "S" if is_part_1 else "a"
  todo = [(r, c) for r, row in enumerate(grid) for c, col in enumerate(row) if col == target]

  moves = 0
  seen = set()
  while todo:
    moves+=1
    next_todo = []

    for (r, c) in todo:
      for (rr, cc) in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if not (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
          continue

        diff = get_elev(grid[rr][cc]) - get_elev(grid[r][c])
        if diff > 1:
          continue
        if (rr, cc) in seen:
          continue
        seen.add((rr, cc))
        next_todo.append((rr, cc))

        if grid[rr][cc] == "E":
          return moves
    todo = next_todo

print(solve(True))
print(solve(False))
