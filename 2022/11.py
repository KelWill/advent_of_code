import itertools
import sys

input = open("11.input" if len(sys.argv) == 1 else sys.argv[1]).read()
data = [x for x in input.split("\n")]

"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
"""

def parse_monkey (s):
  for row in s.split("\n"):
    row = row.strip()
    if row.startswith("Monkey"):
      _, monkey_num = row.split(" ")
      monkey_num = int(monkey_num[:-1])
    elif row.startswith("Starting"):
      _, numbers = row.split(": ")
      items = list(map(int, numbers.split(", ")))
    elif row.startswith("Operation"):
      _, operation = row.split(" = ")
    elif row.startswith("Test:"):
      _, test_n = row.split("by")
      test_n = int(test_n)
    elif row.startswith("If true"):
      _, true_dest = row.split("monkey ")
      true_dest = int(true_dest)
    elif row.startswith("If false"):
      _, false_dest = row.split("monkey ")
      false_dest = int(false_dest)

  return {
    "monkey": monkey_num,
    "numbers": items,
    "operation": operation,
    "test_n": test_n,
    "true_dest": true_dest,
    "false_dest": false_dest,
    "inspections": 0
  }

monkeys = [parse_monkey(monkey_string) for monkey_string in input.split("\n\n")]

worry_divisor = 1
for monkey in monkeys:
  worry_divisor *= monkey["test_n"]

round = 0
for n in range(10000):
  for monkey in monkeys:
    while len(monkey["numbers"]):
      old = monkey["numbers"].pop()
      worry_level = eval(monkey["operation"])
      worry_level = worry_level % worry_divisor
      if worry_level % monkey["test_n"] == 0:
        monkeys[monkey["true_dest"]]["numbers"].append(worry_level)
      else:
        monkeys[monkey["false_dest"]]["numbers"].append(worry_level)
      monkey["inspections"] += 1

print(sorted([monkey["inspections"] for monkey in monkeys]))
