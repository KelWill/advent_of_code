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


def spells_xmas (words, starting_pos):
    count = 0    
    directions = []
    for dr in ((1, -1, 0)):
        for dc in ((1, -1, 0)):
            if dr or dc:
                directions.append((dr, dc))
    for dr, dc in directions:
        pos = starting_pos
        word = words[pos]
        while words[pos]:
            pos = (pos[0] + dr, pos[1] + dc)
            word += words[pos]
            if word == "XMAS":
                count += 1
                break
            if not "XMAS".startswith(word):
                break
    return count

def mas_count (words, pos):
    if words[pos] != "A":
        return 0
    r, c = pos
    diagonal = [words[r - 1, c - 1] + words[r + 1, c + 1], words[r + 1, c - 1] + words[r - 1, c + 1]]
    return all(w == "SM" or w == "MS" for w in diagonal)


xcheck = """.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""

def main (s):
    lines = s.split("\n")
    words = defaultdict(str) | {(r, c): lines[r][c] for r in range(len(lines)) for c in range(len(lines[0]))}
    p1, p2 = 0, 0
    positions = list(words.keys())
    for pos in positions:
        p1 += spells_xmas(words, pos)
        p2 += mas_count(words, pos)

    return p1, p2

print(main(ex))
print(main(real))

