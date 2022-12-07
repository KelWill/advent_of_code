from collections import defaultdict 
input = open("7.input").read()

sizes = defaultdict(lambda: 0)
path = ["/"]
for row in input.split("\n"):
  if row.startswith("$ cd"):
    _, dest = row.split(" cd ")
    if dest == "..":
      path.pop()
    else:
      path.append(dest)
  elif row.startswith("$ ls") or row.startswith("dir"):
    continue
  else:
    size, name = row.split(" ")
    size = int(size)
    for i in range(len(path)):
      sizes["/".join(path[:i + 1])] += size

part1 = sum([size for k, size in sizes.items() if size <= 100000])
print(f"part1: {part1}")

unused_space = 70000000 - sizes["/"]
size_required = 30000000 - unused_space 

size_to_delete = min(*[size for k, size in sizes.items() if size >= size_required])
print(f"part2: {size_to_delete}")
