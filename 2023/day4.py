import re

ex = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def main(s):
    score = 0
    scores = []
    for row in s.split("\n"):
        _card, row = row.split(":")
        winners, yours = row.split("|")
        matches = set(re.findall(r'\d+', winners)
                      ) & set(re.findall(r'\d+', yours))
        scores.append([1, len(matches)])
        if len(matches):
            score += 2 ** (len(matches) - 1)

    def calc_part_2(scores):
        for i, score in enumerate(scores):
            count, wins = score
            for j in range(i + 1, i + 1 + wins):
                scores[j][0] += count

        return sum(count for count, _wins in scores)

    return (score, calc_part_2(scores))


input = open("day4.input").read()
print(main(ex), main(input))
