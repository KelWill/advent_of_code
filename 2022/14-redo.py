import re

real_input = open("14.input").read()
example_input = open("14.example").read()

grid = set()

def ints(s: str):
    return list(map(int, re.findall(r"-?\d+", s)))

def solve (input):
  max_c = 0
  for row in input.split("\n"):
    entries = row.split(" -> ")
    for a, b in zip(entries, entries[1:]):
      ar, ac = ints(a)
      br, bc = ints(b)

      [ar, br] = sorted([ar, br])
      [ac, bc] = sorted([ac, bc])

      for r in range(ar, br + 1):
        for c in range(ac, bc + 1):
          grid.add((r, c))
          max_c = max(max_c, c)

  def sand ():
    r = 500
    c = 0
    while True:
      moved = False
      for (rr, cc) in ((r, c + 1), (r - 1, c + 1), (r + 1, c + 1)):
        if (rr, cc) in grid or (cc >= max_c + 2):
          continue
        moved = True
        r = rr, c = cc
        break

      if r == 500 and c == 0:
        return True
      if not moved:
        grid.add((r, c))
        return False

  count = 0
  while True:
    count += 1
    if sand():
      return count

print(solve(example_input))