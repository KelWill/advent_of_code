input = open("4.input").read()

def has_overlap(a, b, checked_reverse = False):
    for n in b:
        if (a[0] <= n <= a[1]):
            return True
    if checked_reverse == False:
        return has_overlap(b, a, True)
    return False

count = 0
for row in input.split("\n"):
    [left, right] = [[int(d) for d in s.split("-")] for s in row.split(",")]    
    if has_overlap(left, right): 
        count += 1

print(count)
