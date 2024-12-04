from collections import defaultdict

ex = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
real = open("./day4.input").read()


def spells_xmas (words, pos):
    directions = [dr + dc * 1j for dr in (1, -1, 0) for dc in (1, -1, 0) if dr or dc]
    words = ["".join(words[pos + x * dd] for x in range(4)) for dd in directions]
    return sum(word == "XMAS" for word in words)

def mas_count (words, pos):
    if words[pos] != "A":
        return 0
    diagonal = [words[pos - 1 - 1j] + words[pos + 1 + 1j], words[pos + 1 - 1j] + words[pos - 1 + 1j]]
    return all(w == "SM" or w == "MS" for w in diagonal)

def main (s):
    lines = s.split("\n")
    words = defaultdict(str) | { r + c * 1j: lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))}
    p1, p2 = 0, 0
    positions = list(words.keys())
    for pos in positions:
        p1 += spells_xmas(words, pos)
        p2 += mas_count(words, pos)

    return p1, p2

print(main(ex))
print(main(real))

