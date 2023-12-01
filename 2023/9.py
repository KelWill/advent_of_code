input = open("9.input").read()

# input = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""

DIRECTIONS = {
  "R": [0, 1],
  "U": [-1, 0],
  "D": [1, 0],
  "L": [0, -1],
}


seen = {}
seen[f"0,0"] = True

knots = [[0, 0] for i in range(0, 10)]


def show (head, tail, seen):
  for r in range(-5, 5):
    row = ""
    for c in range(-5, 5):
      key = f"{r},{c}"
      if r == head[0] and c == head[1]:
        row += "H"
      elif r == tail[0] and c == tail[1]:
        row += "T"
      elif key in seen:
        row += "#"
      else:
        row += "."
    print(row)
  print("")


def get_direction (head, tail):
  for dr in [-1, 0, 1]:
    for dc in [-1, 0, 1]:
      if head[0] + dr == tail[0] and head[1] + dc == tail[1]:
        return [0, 0]

  if head[0] != tail[0] and head[1] != tail[1]:
    dc = 1 if head[1] > tail[1] else -1
    dr = 1 if head[0] > tail[0] else -1
    return [dr, dc]

  elif head[0] == tail[0]:
    return [0, 1] if tail[1] < head[1] else [0, -1]
  elif head[1] == tail[1]:
    return [1, 0] if tail[0] < head[0] else [-1, 0]
  else:
    raise Exception("shouldn't reach here")    

for row in input.split("\n"):
  [dir, n] = row.split(" ")
  n = int(n)
  [head_dr, head_dc] = DIRECTIONS[dir]
  for i in range(0, n):
    head = knots[0]
    head[0] += head_dr
    head[1] += head_dc

    for tail in knots[1:]:      
      [tail_dr, tail_dc] = get_direction(head, tail)
      tail[0] += tail_dr
      tail[1] += tail_dc
      head = tail
      if tail == knots[-1]:
        seen[f"{tail[0]},{tail[1]}"] = True


print(len(seen.items()))

  