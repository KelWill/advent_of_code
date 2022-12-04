input = open("4.input").read()

count = 0
for row in input.split("\n"):
    [left, right] = [[int(d) for d in s.split("-")] for s in row.split(",")]    
    overlaps = (left[0] <= right[0] and left[1] >= right[0]) or (left[0] >= right[0] and right[1] >= left[0]) or (left[0] <= right[1] and left[1] >= right[1]) or (right[0] <= left[1] and right[1] >= left[1])
    if overlaps: 
        count += 1

print(count)

