import itertools
import sys
import functools
import json

input = open("13.input" if len(sys.argv) == 1 else sys.argv[1]).read()

def compare (left, right):
  match left, right:
    case int(), int(): return (left < right) - (right < left)
    case int(), list(): return compare([left], right)
    case list(), int(): return compare(left, [right])
    case list(), list():
      for result in map(compare, left, right):
        if result: return result
      return compare(len(left), len(right))

s = 0
for i, pair in enumerate(input.split("\n\n")):
  a, b = pair.split("\n")
  res = compare(json.loads(a), json.loads(b))
  if res == 1:
    s += i + 1
print(s)

packets = [
  [[2]],
  [[6]]
]
for row in input.split("\n"):
  if row == "":
    continue
  packets.append(json.loads(row))

results = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)

m = 1
for i, p in enumerate(results):
  if p in [[[2]], [[6]]]:
    m *= (i + 1)
print(m)

