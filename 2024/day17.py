real = open("./day17.input").read()

ex = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

import re

def nums (s):
    return [*map(int, re.findall(r"-?\d+", s))]


def main (s, A_override = None):
    registers, program = s.split("\n\n")
    A, B, C = nums(registers)
    if A_override:
        A = A_override
    program = nums(program)
    i = 0
    results = []
    while i < len(program):
        op, literal_operand = program[i:i + 2]
        combo_operand = ([literal_operand] * 4 + [A, B, C])[literal_operand]
        if op == 0:
            A = int(A // (2 ** combo_operand))
        if op == 1:
            B = int(B) ^ int(literal_operand)
        if op == 2:
            B = int(combo_operand % 8)
        if op == 3 and A != 0 and i != literal_operand:
            i = literal_operand
            continue
        if op == 4:
            B = B ^ C
        if op == 5:
            results.append(int(combo_operand % 8))
        if op == 6:
            B = int(A // (2 ** combo_operand))
        if op == 7:
            C = int(A // (2 ** combo_operand))
        i += 2

    return ",".join([*map(str, results)])

print("ex", main(ex))
print("real", main(real))

match_count = 0
i = 2944
while True:
    x = "2,4,1,1,7,5,0,3,1,4,4,4,5,5,3,0"
    m = 1
    r = main(real, i)
    if x.endswith(r):
        print(i, r)
        i = i << 3
        continue
    if m > match_count:
        print(i, match_count, r)
        match_count = m

    i += 1
