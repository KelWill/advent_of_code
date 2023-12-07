from collections import Counter

ex = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

order_part_1 = {k: i for i, k in enumerate(
    "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", "))}
order_part_2 = {k: i for i, k in enumerate(
    "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", "))}


def get_hand_score(hand):
    counts = Counter(hand)
    joker_count = counts.pop("J") if "J" in counts else 0
    if joker_count >= 4:
        return 0

    key = max((counts[c], c) for c in counts)[1]
    counts[key] += joker_count
    vals = list(counts.values())
    return [5 in vals, 4 in vals, 3 in vals and 2 in vals, 3 in vals, vals.count(2) == 2, 2 in vals, True].index(True)


def main(s):
    hands = [[] for _i in range(7)]
    for row in s.split("\n"):
        hand, bid = row.split(" ")
        hand_order = tuple([order_part_2[char] for char in hand])
        hands[get_hand_score(hand)].append((hand_order, int(bid), hand))

    hands = sum([sorted(x) for x in hands], [])
    return sum(hand[1] * (i + 1) for i, hand in enumerate(reversed(hands)))


print("ex:", main(ex))
print("real:", main(open("./day7.input").read()))
