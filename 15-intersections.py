import re

def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))

def get_y_intercept (point, slope):
  (x, y) = point
  return y - x * slope

def is_goal (sensors, point):
  (x, y) = point
  for (sx, sy), sensor_range in sensors.items():
    point_to_beacon_dist = abs(x - sx) + abs(y - sy)
    if point_to_beacon_dist <= sensor_range:
      return False
  return True
    

def solve (input, valid_range):
  sensors = {}
  for row in input.split("\n"):
    sx, sy, bx, by = ints(row)
    dist = abs(bx - sx) + abs(sy - by)
    sensors[(sx, sy)] = dist
  
  up_slope_intercepts = []
  down_slope_intercepts = []
  for (x, y), dist in sensors.items():
    left_point = (x - dist - 1, y)
    bottom_point = (x, y - dist - 1)
    up_slope_intercepts.append(get_y_intercept(left_point, 1))
    up_slope_intercepts.append(get_y_intercept(bottom_point, 1))

    down_slope_intercepts.append(get_y_intercept(left_point, -1))
    down_slope_intercepts.append(get_y_intercept(bottom_point, -1))

  for up in up_slope_intercepts:
    for down in down_slope_intercepts:
      if (up - down) % 2:
        continue

      # y = x + up
      # y = -x + down
      # x + up = down - x
      # x = (down - up) / 2
      # (down - up) / 2 + up = (down + up) / 2

      x, y = (down - up) / 2, (up + down) / 2
      if not ((0 <= x <= valid_range) and (0 <= y <= valid_range)):
        continue

      if is_goal(sensors, (x, y)):
        return x * 4000000 +  y



print(solve(open("./15.example").read(), 20))
print(solve(open("./15.input").read(), 4000000))
