import sys
from math import prod
from operator import add, mul

input = open("11.input" if len(sys.argv) == 1 else sys.argv[1]).read()

class Monkey:
    def __init__ (self, s):
        _, items_, op_, div_, true_, false_ = s.split("\n")
        self.items = [*map(int, items_.split(": ")[1].split(", "))]
        self.op = self._parseOp(op_)
        self.div = int(div_.split(" by ")[1])
        self.true = int(true_.split(" monkey ")[1])
        self.false = int(false_.split(" monkey ")[1])
        self.seen = 0

    def _parseOp (self, line):
        [left, op, right] = line.split(" = ")[1].split()
        def operation (item):
            fn = add if op == "+" else mul
            match (left, right):
                case ("old", "old"):
                    return fn(item, item)
                case ("old", x):
                    return fn(item, int(x))
                case (x, "old"):
                    return fn(item, int(x))
                case (x, y):
                    return fn(int(x), int(y))
        return operation

def solve (is_part_1):
    monkeys = [Monkey(monkey_string) for monkey_string in input.split("\n\n")]
    worry_divisor = prod([ monkey.div for monkey in monkeys])

    for _ in range(20 if is_part_1 else 10000):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.pop()
                if is_part_1:
                    item = monkey.op(item) // 3
                else:
                    item = monkey.op(item) % worry_divisor
                dest = monkey.true if item % monkey.div == 0 else monkey.false
                monkeys[dest].items.append(item)
                monkey.seen += 1

    return prod(sorted([monkey.seen for monkey in monkeys])[-2:])

print(f"part1: {solve(True)}")
print(f"part2: {solve(False)}")
