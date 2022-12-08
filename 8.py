input = open("8.input").read()

# input = """30373
# 25512
# 65332
# 33549
# 35390"""

grid = [list(map(int, list(row))) for row in input.split("\n")]

best_view_score = 0
externally_visible = 0

for r0 in range(len(grid)):
  row = grid[r0]

  for c0 in range(len(row)):
    total_view_score = 1

    visible = False
    for [dr, dc] in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
      r = r0
      c = c0
      view_score = 0

      while True:
        r += dr
        c += dc

        if not (0 <= r < len(grid) and 0 <= c < len(row)):
          visible = True
          break
        elif grid[r][c] >= grid[r0][c0]:
          view_score += 1
          break
        else:
          view_score += 1

      total_view_score *= view_score
    if visible:
      externally_visible += 1
    best_view_score = max(total_view_score, best_view_score)

print(f"part1 {externally_visible}")
print(f"part2 {best_view_score}")