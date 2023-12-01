from collections import defaultdict
ex = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2"""


def main(e):
    bots = defaultdict(list)
    values = defaultdict(list)
    outputs = {}
    for s in e.split("\n"):
        if s.startswith("value"):
            a = s.split(" ")
            v = int(a[1])
            bot = int(a[-1])
            values[v] = bot
        else:
            a = s.split(" ")
            [_b, bot, gives, low, to, output_or_bot_low, low_bot,
                _a, high, to, output_or_bot_high, high_bot] = a
            bots[bot] = {"chips": []}
            bots[bot]["lo2w"] = (output_or_bot_low, low_bot)
            bots[bot]["high"] = (output_or_bot_high, high_bot)

    def process_chips(bot, bot_num):
        if len(bot["chips"]) != 2:
            return
        low = min(bot["chips"])
        high = max(bot["chips"])
        high_type, high_bot = bot["high"]
        low_type, low_bot = bot["low"]
        bot["chips"] = []

        if low == 17 and high == 61:
            print(bot, bot_num)

        if high_type == "output":
            if not str(high_bot) in outputs:
                outputs[str(high_bot)] = []
            outputs[str(high_bot)].append(high)
        else:
            bots[str(high_bot)]["chips"].append(high)
            process_chips(bots[str(high_bot)], high_bot)
        if low_type == "output":
            if not str(low_bot) in outputs:
                outputs[str(low_bot)] = []
            outputs[str(low_bot)].append(low)
        else:
            bots[str(low_bot)]["chips"].append(low)
            process_chips(bots[low_bot], low_bot)

    for k in values:
        bot = values[k]
        bots[str(bot)]["chips"].append(k)
        process_chips(bots[str(bot)], bot)
    print(outputs[str(0)][0] * outputs[str(1)][0] * outputs[str(2)][0])


main(ex)
main(open("day10input").read())
