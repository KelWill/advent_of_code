import itertools
import sys
import functools

input = open("13.input" if len(sys.argv) == 1 else sys.argv[1]).read()

def compare (left, right):
  if type(left) == int and type(right) == int:
    if left < right:
      return 1
    if left > right:
      return -1
    return 0
  if type(left) == list and type(right) == list:
    for i in range(len(left)):
      if i >= len(right):
        return -1
      comp = compare(left[i], right[i])
      if comp != 0:
        return comp
    return len(left) < len(right)

  if type(left) == list:
    return compare(left, [right])
  if type(right) == list:
    return compare([left], right)

s = 0
for i, pair in enumerate(input.split("\n\n")):
  a, b = pair.split("\n")
  res = compare(eval(a), eval(b))
  print(a, b, res)
  if res == 1:
    s += i + 1

packets = [
  [[2]],
  [[6]]
]
for row in input.split("\n"):
  if row == "":
    continue
  packets.append(eval(row))

results = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)
print(results)

m = 1
for i, p in enumerate(results):
  if str(p) == "[[2]]" or str(p) == "[[6]]":
    m *= (i + 1)
print(m)

