import re
ex = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

instructions = """cpy x y copies x (either an integer or the value of a register) into register y.
inc x increases the value of register x by one.
dec x decreases the value of register x by one.
jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
"""


def main(s):
    registers = {
        "a": 0,
        "b": 0,
        "c": 1,
        "d": 0,
    }

    instructions = s.split("\n")
    i = 0

    while i < len(instructions):
        row = instructions[i]
        if row.startswith("cpy"):
            reg, dest = re.match(r'cpy (\w+) (\w+)', row).groups()
            if reg.isdigit():
                registers[dest] = int(reg)
            else:
                registers[dest] = registers[reg]
        elif row.startswith("inc"):
            a, reg = row.split(" ")
            registers[reg] += 1
        elif row.startswith("dec"):
            a, reg = row.split(" ")
            registers[reg] -= 1
        elif row.startswith("jnz"):
            a, reg, jump = row.split(" ")
            if (reg.isdigit() and reg != "0") or (reg in registers and registers[reg]):
                i += int(jump)
                continue
        i += 1
    print(registers["a"])


main(ex)
main(open("./day12.input").read())
