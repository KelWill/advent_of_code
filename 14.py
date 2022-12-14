import itertools
import sys
import functools
import json

real_input = open("14.input").read()
example_input = open("14.example").read()

def print_grid (grid):
  for y in range(0, 11):
    row = ""
    for x in range(480, 510):
      row += " " if (x, y) not in grid else "#" if grid[(x, y)] == 1 else "o"
    print(row)


def get_points (start, end):
  (startx, starty) = start
  (endx, endy) = end

  if startx == endx:
    return [(startx, y) for y in range(min(starty, endy), max(starty, endy) + 1)]
  elif starty == endy:
    return [(x, starty) for x in range(min(startx, endx), max(endx, startx) + 1)]
  else:
    raise Exception(f"unexpected start {start} and end {end}")

def create_grid (input):
  grid = {}
  max_y = 0

  for row in input.split("\n"):
    points = row.split(" -> ")
    for i in range(0, len(points) - 1):
      start = list(map(int, points[i].split(",")))
      end = list(map(int, points[i + 1].split(",")))
      for point in get_points(start, end):
        grid[point] = 1
        max_y = max(max_y, point[1])

  return (grid, max_y)

def solve (input, is_part_1):
  (grid, max_y) = create_grid(input)

  def simulate():
    sandx = 500
    sandy = 0

    while True:
      moved = False
      for dx, dy in ((0, 1), (-1, 1), (1, 1)):
        blocked = (sandx + dx, sandy + dy) in grid
        if not is_part_1:
          blocked = blocked or (sandy + dy) >= max_y + 2
        if blocked:
          continue

        moved = True
        sandx = sandx + dx
        sandy = sandy + dy
        break

      if is_part_1 and sandy > max_y:
        return True

      if not moved:
        grid[(sandx, sandy)] = 2
        if not is_part_1 and (sandx == 500 and sandy == 0):
          return True
        return False
      
  sand_count = 0
  while True:
    sand_count += 1
    if simulate():
      return sand_count

print(f"example input part1: {solve(example_input, True) - 1}")
print(f"example input part2: {solve(example_input, False)}")

print(f"part1: {solve(real_input, True) - 1}")
print(f"part2: {solve(real_input, False)}")
