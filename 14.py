import itertools
import sys
import functools
import json

real_input = open("14.input").read()
example_input = open("14.example").read()


"""A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right. Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source."""
"""sand comes 500"""

"""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

grid = {}
max_y = 0
min_y = 100

def mark_points (start, end):
  [startx, starty] = start
  [endx, endy] = end

  global max_y
  global min_y

  max_y = max(max_y, starty, endy)
  min_y = min(min_y, starty, endy)

  if startx == endx:
    for y in range(starty, endy + 1):
      grid[(endx, y)] = 1
    for y in range(endy, starty + 1):
      grid[(endx, y)] = 1
  elif starty == endy:
    for x in range(startx, endx + 1):
        grid[(x, starty)] = 1
    for x in range(endx, startx + 1):
        grid[(x, starty)] = 1
  else:
    raise Exception("unexpected!")



def handle_row (row):
  points = row.split(" -> ")
  for i in range(0, len(points) - 1):
    start = list(map(int, points[i].split(",")))
    end = list(map(int, points[i + 1].split(",")))
    mark_points(start, end)


def print_grid (grid):
  for y in range(0, 13):
    row = ""
    for x in range(470, 510):
      c = " "
      if (x, y) not in grid:
        c = " "
      elif grid[(x, y)] == 1:
        c = "#"
      else:
        c = "o"
      row += c
    print(row)

def solve(input):
  for row in input.split("\n"):
    handle_row(row)

  def simulate():
    global max_y
    global min_y

    sandx = 500
    sandy = 0
    while True:
      moved = False
      for dx, dy in ((0, 1), (-1, 1), (1, 1)):
        if (sandx + dx, sandy + dy) not in grid and sandy + dy < max_y + 2:
          moved = True
          sandx = sandx + dx
          sandy = sandy + dy
          break

      if not moved:
        grid[(sandx, sandy)] = 2
        if sandy <= min_y:
          min_y -= 10
        if sandx == 500 and sandy == 0:
          return True
        return False
    return False
    
  sand_count = 0
  while True:
    sand_count += 1
    if simulate():
      print("end", sand_count)
      break
    # print_grid(grid)



# print(f"example input: {solve(example_input)}")


print(f"real input: {solve(real_input)}")

