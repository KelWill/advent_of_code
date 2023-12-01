
# The manual explains that the computer supports two registers and six instructions (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named a and b, can hold any non-negative integer, and begin with a value of 0. The instructions are as follows:

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
# All three jump instructions work with an offset relative to that instruction. The offset is always written with a prefix + or - to indicate the direction of the jump (forward or backward, respectively). For example, jmp +1 would simply continue with the next instruction, while jmp +0 would continuously jump back to itself forever.

# The program exits when it tries to run an instruction beyond the ones defined.

# For example, this program sets a to 2, because the jio instruction causes it to skip the tpl instruction:

# inc a
# jio a, +2
# tpl a
# inc a
# What is the value in register b when the program in your puzzle input is finished executing?


def main(command_str):
    a, b = 1, 0
    i = 0

    commands = command_str.split("\n")
    print(commands)
    while i < len(commands):
        parts = commands[i].split()
        instruction = parts[0]
        if instruction == "inc":
            if parts[1] == "a":
                a = a + 1
            else:
                b = b + 1
            i = i + 1
        if instruction == "tpl":
            if parts[1] == "a":
                a = a * 3
            else:
                b = b * 3
            i = i + 1
        if instruction == "hlf":
            if parts[1] == "a":
                a = int(a / 2)
            else:
                b = int(b / 2)
            i = i + 1
        if instruction == "jmp":
            i = i + int(parts[1])
        if instruction == "jie":
            if (parts[1].startswith("a") and a % 2 == 0) or (parts[1].startswith("b") and b % 2 == 0):
                i = i + int(parts[2])
            else:
                i = i + 1
        if instruction == "jio":
            if (parts[1].startswith("a") and a == 1) or (parts[1].startswith("b") and b == 1):
                i = i + int(parts[2])
            else:
                i = i + 1
    return b


ex = """inc a
jio a, +2
tpl a
inc a"""
instructions = """jio a, +22
inc a
tpl a
tpl a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
jmp +19
tpl a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7"""

print(main(ex))
print(main(instructions))
