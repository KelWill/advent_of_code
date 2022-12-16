import re

example = open("./15.example").read()


def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))

def is_goal (sensors, point):
  (x, y) = point
  for (sx, sy), sensor_range in sensors.items():
    point_to_beacon_dist = abs(x - sx) + abs(y - sy)
    if point_to_beacon_dist <= sensor_range:
      return False
  return True

def solve (input, grid_max):
  def is_point_in_range (point):
    (x, y) = point
    return 0 <= x <= grid_max and 0 <= y <= grid_max

  sensors = {}
  for row in input.split("\n"):
    sx, sy, bx, by = ints(row)
    dist = abs(bx - sx) + abs(sy - by)
    sensors[(sx, sy)] = dist
  
  for (sx, sy), dist in sensors.items():
    top = (sx, sy + dist + 1)
    right = (sx + dist + 1, sy)
    down = (sx, sy - dist - 1)
    left = (sx - dist - 1, sy)
    for (sign_dx, sign_dy) in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
      for dx in range(0, dist + 2):
        dy = dist + 1 - dx # whatever shift we're not doing to x, we do to y
        x = sx + dx * sign_dx
        y = sy + dy * sign_dy
        if not is_point_in_range((x, y)):
          continue

        if is_goal(sensors, (x, y)):
          return (x, y)

  raise Exception("no point found that satisfies criteria")

print(solve(example, 20))
# print(solve(open("15.input").read(), 4000000))
