input = open("8.input").read()

# input = """30373
# 25512
# 65332
# 33549
# 35390"""

grid = []

for row in input.split("\n"):
  grid.append(list(int(x) for x in list(row)))

best_view_score = 0
for r0 in range(len(grid)):
  trees = grid[r0]

  for c0 in range(len(trees)):
    tree_height = trees[c0]
    seen = False

    r = r0
    c = c0

    total_view_score = 1  

    for [dr, dc] in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
      r = r0
      c = c0
      view_score = 0

      while r < len(grid) and c < len(trees) and c >= 0 and r >= 0:
        r += dr
        c += dc

        if r >= len(grid) or c >= len(trees) or c < 0 or r < 0:
          total_view_score *= view_score
          break
        elif grid[r][c] >= tree_height:
          view_score += 1
          total_view_score *= view_score
          break
        else:
          view_score += 1

    best_view_score = max(total_view_score, best_view_score)

print(best_view_score)