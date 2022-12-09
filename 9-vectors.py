from Util import Vector

def get_direction (a, b):
  if a.chess_distance(b) < 2:
    return Vector(0, 0)
  update = b - a
  return Vector(*[u / (abs(u) or 1) for u in update.loc])

DIRECTIONS = {
  "U": Vector(-1, 0),
  "D": Vector(1, 0),
  "L": Vector(0, -1),
  "R": Vector(0, 1),
}

def solve (knot_length):
  seen = set()
  knots = [Vector(0, 0) for i in range(0, knot_length)]
  for row in open("./9.input").read().split("\n"):
    dir, steps = row.split()
    steps = int(steps)

    for i in range(steps):
      knots[0] += DIRECTIONS[dir]
      for i in range(1, len(knots)):
        update = get_direction(knots[i], knots[i - 1])
        knots[i] += update

      seen.add(str(knots[-1]))
  return len(seen)

print(f"part1 {solve(2)}")
print(f"part2 {solve(10)}")