input = open("6.input").read()
# input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

counts = {}
n = 14
for i in range(0, n):
  if not input[i] in counts:
    counts[input[i]] = 0
  counts[input[i]] += 1

for i in range(n, len(input)):
  counts[input[i - n]] -= 1
  if counts[input[i - n]] == 0:
    del counts[input[i - n]]
  if not input[i] in counts:
    counts[input[i]] = 0
  counts[input[i]] += 1
  print(len(counts.keys()))
  if len(counts.keys()) == n:
    print(i + 1)
    break
