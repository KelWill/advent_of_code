

start = 20151125


def next(n, row, col):
    row = row - 1
    col = col + 1
    if row == 0:
        row = col
        col = 1
    return ((n * 252533) % 33554393, row, col)


row = 1
col = 1
code = start
while True:
    code, row, col = next(code, row, col)
    if row == 3010 and col == 3019:
        print(code)
        break

# row 3010, column 3019.
