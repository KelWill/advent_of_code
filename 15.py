import re

example = open("./15.example").read()

def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))

def solve (input, max_y):
  sensors_and_beacons = {}
  beacons = set()
  for row in input.split("\n"):
    sx, sy, bx, by = ints(row)
    sensors_and_beacons[(sx, sy)] = (bx, by)
    beacons.add((bx, by))

  no_beacon = set()

  for y in range(0, max_y + 1):
    intervals = []
    for (sx, sy), (bx, by) in sensors_and_beacons.items():
      td = abs(sx - bx) + abs(sy - by)
      distance_to_y = abs(y - sy)
      xdiff = td - distance_to_y
      if xdiff < 0:
        continue
      intervals.append((sx - xdiff, sx + xdiff))

    intervals.sort()
    combined_intervals = []
    for (lo, hi) in intervals:
      if not combined_intervals:
        combined_intervals.append([lo, hi])
      else:
        last_high = combined_intervals[-1][1]
        if lo <= last_high + 1:
          combined_intervals[-1][1] = max(hi, combined_intervals[-1][1])
        else:
          combined_intervals.append([lo, hi])
    if len(combined_intervals) != 1:
      assert len(combined_intervals) == 2
      assert combined_intervals[0][1] + 2 == combined_intervals[1][0]
      return y + (combined_intervals[0][1] + 1) * 4000000

print(solve(example, 20))
print(solve(open("15.input").read(), 4000000))
