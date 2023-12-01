input = open("7.input").read()
# input = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k"""


graph = { "files": {}, "children": {}, "self": "/" }
curr = graph
rows = input.split("\n")
i = 0

while i < len(rows):
  row = rows[i]
  if row.startswith("$ ls"):
    i += 1
    row = rows[i]
    while i < len(rows) and not rows[i][0].startswith("$"):
      row = rows[i]
      if row.startswith("dir"):
        _, name = row.split(" ")
        curr["children"][name] = {
          "self": name,
          "files": {},
          "children": {},
          "parent": curr,
        }
      else:
        size, name = row.split(" ")
        curr["files"][name] = int(size)
      i += 1
    i -= 1
  else:
    if row == "$ cd ..":
      if "parent" in curr:
        curr = curr["parent"]
    elif row == "$ cd /":
      curr = graph
    else:
      cd, _, child = row.split(" ")
      curr = curr["children"][child]
  i += 1

def calculate_size(curr):
  size = 0
  for key in curr["files"]:
    size += curr["files"][key]
  for key in curr["children"]:
    child = curr["children"][key]
    size += calculate_size(child)
  curr["size"] = size
  return size

def flatten (l):
  results = []
  for item in l:
    if isinstance(item, list):
      item = flatten(item)
      results += item
    else:
      results.append(item)
  return results

def to_sizes (curr):
  return [curr["size"]] + flatten([to_sizes(child) for key, child in curr["children"].items()])

calculate_size(graph)
sizes = to_sizes(graph)

part1 = sum([size for size in sizes if size <= 100000])
print(f"part1: {part1}")

unused_space = 70000000 - graph["size"]
size_required = 30000000 - unused_space 

size_to_delete = min(*[size for size in sizes if size >= size_required])
print(f"part2: {size_to_delete}")
