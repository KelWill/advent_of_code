input = open("4.input").read()

count = 0
for row in input.split("\n"):
    [x1, y1, x2, y2] = [int(d) for d in row.replace("-", ",").split(",")]    
    if (x1 >= x2 and y1 <= y2) or (x2 >= x1 and y2 <= y1):
        count += 1

print(f"part 1 {count}")

count = 0
for row in input.split("\n"):
    [x1, y1, x2, y2] = [int(d) for d in row.replace("-", ",").split(",")]    
    if max(x1, x2) <= min(y1, y2):
        count += 1

print(f"part 2: {count}")
