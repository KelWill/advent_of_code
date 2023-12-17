ex = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

V = {
    "|": (1, -1),
    "-": (1j, -1j),
    "L": (1j, -1),
    "J": (-1j, -1),
    "7": (-1j, 1),
    "F": (1j, 1),
    "S": (1, -1j),
}

BLOCKS = {
    "|": (1j, 1 + 1j, 2 + 1j),
    "-": (1, 1 + 1j, 1 + 2j),
    "L": (1j, 1 + 1j, 1 + 2j),
    "J": (1j, 1 + 1j, 1),
    "7": (1, 1 + 1j, 2 + 1j),
    "F": (1 + 2j, 1 + 1j, 2 + 1j),
}


def main(s):
    board = s.split("\n")
    board = {r + c * 1j: board[r][c] for r in range(len(board))
             for c in range(len(board[r]))}
    start = next(b for b in board if board[b] == "S")
    board[start] = "7"
    loop = set()
    todo = [start]
    while todo:
        curr = todo.pop()
        loop |= {curr}
        todo += list({curr + d for d in V[board[curr]]} - loop)

    enclosed = 0
    parity_changes = {pos: pos in loop and board[pos] in [
        "|", "L", "J"] for pos in board}
    parity = 0
    for pos in board:
        parity += parity_changes[pos]
        enclosed += not pos in loop and parity % 2

    return enclosed


print("ex:", main(ex))
print("real:", main(open("day10.input").read()))
