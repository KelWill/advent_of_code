input = open("./5.input").read()
import re

# input = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

[start, instruction_string] = input.split("\n\n")

part_2 = True

def parse_columns (start):
    rows = start.split("\n")
    col_indexes = rows.pop()
    cols = []
    for i in range(len(col_indexes)):
        if col_indexes[i] == " ":
            continue
        col = [row[i] for row in rows if row[i].isalpha()]
        col.reverse()
        cols.append(col)
    return cols

def parse_instructions (instruction_string):
    result = []
    for row in instruction_string.split("\n"):
        match = re.search("move (\d+) from (\d+) to (\d+)", row)
        result.append(map(int, list(match.groups())))
    return result

instructions = parse_instructions(instruction_string)
cols = parse_columns(start)
for [move, start, end] in instructions:
    to_add = []
    for i in range(move):
        to_add.append(cols[start - 1].pop())
    if part_2:
        to_add.reverse()
    for v in to_add:
        cols[end - 1].append(v)

result = ""
for i in range(len(cols)):
    result += cols[i][len(cols[i]) - 1]

print(result)
