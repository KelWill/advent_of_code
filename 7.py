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
  if row[2:] == "ls":
    i += 1
    row = rows[i]
    while i < len(rows) and rows[i][0] != "$":
      row = rows[i]
      first, second = row.split(" ")

      if first == "dir":
        curr["children"][second] = {
          "self": second,
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
    if row[0] != "$":
      print("invalid row", row)
      break
    if row == "$ cd ..":
      if "parent" in curr:
        curr = curr["parent"]
    elif row == "$ cd /":
      curr = graph
    else:
      cd, x, child = row.split(" ")
      curr = curr["children"][child]
  i += 1

total = 0

def calculate_size(curr):
  global total
  size = 0
  for key in curr["files"]:
    size += curr["files"][key]
  for key in curr["children"]:
    child = curr["children"][key]
    size += calculate_size(child)
  curr["size"] = size
  if size <= 100000:
    total += size
  return size

calculate_size(graph)
unused_space = 70000000 - graph["size"]
size_required = 30000000 - unused_space 

results = []
def dfs (curr):
  results.append(curr)
  for key in curr["children"]:
    dfs(curr["children"][key])

dfs(graph)
print(results)


found = None
for dir in results:
  if dir["size"] >= size_required and (found == None or dir["size"] < found["size"]):
    found = dir

print(found["size"])
