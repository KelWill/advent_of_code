import re
from collections import defaultdict


def gm(reg, s):
    return re.match(reg, s).groups()


def gi(reg, s):
    return map(int, re.match(reg, s).groups())


def get_ints(s):
    return map(int, re.findall(r'\d+', s))


ex = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""


def main(s: str):
    bots = defaultdict(list)
    rules = {}
    dest = {
        "bot": bots,
        "output": defaultdict(list)
    }
    for row in s.split("\n"):
        if row.startswith("value"):
            v, b = map(int, gm(r'value (\d+) .+ (\d+)', row))
            bots[b].append(v)
        else:
            bot, low_type, low, high_type, high = gm(
                r'bot (\d+) .+ (bot|output) (\d+) .+ (bot|output) (\d+)', row)
            rules[int(bot)] = (low_type, int(low), high_type, int(high))

    while [b for b in bots.values() if len(b) == 2]:
        k, b = [(k, b) for (k, b) in bots.items() if len(b) == 2][0]
        low = min(b)
        high = max(b)
        [low_type, low_dest, high_type, high_dest] = rules[k]
        dest[low_type][low_dest].append(low)
        dest[high_type][high_dest].append(high)
        bots[k] = []

    prod = 1
    for i in range(3):
        prod *= dest["output"][i][0]
    return prod


print(
    "ex:",
    main(ex),
    "\ninput:",
    main(open("day10input").read())
)
