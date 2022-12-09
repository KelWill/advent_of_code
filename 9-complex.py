input = open("9.input").read()

DIRECTIONS = {
  "R": 1j,
  "L": -1j,
  "U": -1,
  "D": 1,
}


def get_direction (head, tail):
  dist = head - tail
  chess_distance = max(abs(dist.real), abs(dist.imag))
  if chess_distance < 2:
    return 0
  return dist.real / abs(dist.real or 1) + dist.imag * 1j / abs(dist.imag or 1)

def solve (knot_length):
  seen = {}
  knots = [0 + 0j for i in range(0, knot_length)]

  for row in input.split("\n"):
    [dir, n] = row.split(" ")
    n = int(n)
    for i in range(0, n):
      knots[0] += DIRECTIONS[dir]
      for i in range(1, len(knots)):
        tail_dir = get_direction(knots[i - 1], knots[i])
        knots[i] += tail_dir
        if i == len(knots) - 1:
          seen[f"{knots[i]}"] = True
  return len(seen.items())


print(f"part1 {solve(2)}")
print(f"part2 {solve(10)}")

