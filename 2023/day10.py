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
    "|": lambda v: v,
    "-": lambda v: v,
    "L": lambda v: 1j if v.real else -1,
    "J": lambda v: -1j if v.real else -1,
    "7": lambda v: -1j if v.real else 1,
    "F": lambda v: 1j if v.real else 1,
    "S": lambda v: 1  # looked at input to choose start vector
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
    curr = start
    v = 1
    loop = set()
    while curr != start or not loop:
        loop.add(curr)
        v = V[board[curr]](v)
        curr += v

    expanded_board = set()
    for pos in loop:
        for d in BLOCKS[board[pos]]:
            expanded_board.add(3 * pos + d)

    MAX_REAL = max(x.real for x in board)
    MAX_IMAG = max(x.imag for x in board)
    can_reach_edge = {}
    for pos in board.keys() ^ loop:
        if pos in can_reach_edge:
            continue

        can_reach_edge_from_pos = False
        poss = [pos * 3]
        seen = set()
        while poss:
            a = poss.pop()
            if a.real > MAX_REAL * 3 or a.imag > MAX_IMAG * 3 or a.real < 0 or a.imag < 0:
                can_reach_edge_from_pos = True
                continue

            for d in (1, -1, 1j, -1j):
                aa = a + d
                if aa in expanded_board or aa in seen:
                    continue
                seen.add(aa)
                poss.append(aa)
        for pos in seen:
            if pos / 3 not in board:
                continue
            can_reach_edge[pos / 3] = can_reach_edge_from_pos

    can_reach_edge = set(pos for pos in can_reach_edge if can_reach_edge[pos])

    enclosed = board.keys() ^ (can_reach_edge | loop)
    return len(loop), len(enclosed)


print("ex:", main(ex))
print("ex:", main(open("day10.input").read()))
