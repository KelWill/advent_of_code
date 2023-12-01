input = open("6.input").read()
# input = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

n = 14
for i in range(len(input)):
  if len(set(input[i:i + n])) == n:
    print(i + n)
    break
